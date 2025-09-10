"""
Author: live1089 a5u3580@163.com
Date: 2025-06-11 17:10:47
LastEditors: live1089 a5u3580@163.com
LastEditTime: 2025-06-11 17:18:55
FilePath: \\Pharmacy_drug_management_system\\main.py
"""
from enum import Enum

from PySide6.QtCore import Signal, QTimer
from PySide6.QtSql import QSqlQuery
# 导入pyside6库
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QDialog)
# 主题
from qtmodern.styles import dark
from qtmodern.styles import light
# 数据库
import data.sqlite_data
from data.sqlite_data import DrugDicModel, SupplierModel, PurchaseOrderModel, StockInMainModel, StockInDetailModel, \
    InventoryDatchModel, StockOutMainModel, InventoryCheckModel, ShelvesDrugModel, InventoryModel
# 外部UI
import ui_app.log_in_ui
import ui_app.mainwondows_ui
from page_window.inventory_count_page import InventoryCountPage
from page_window.medicines_page import MedicinesPage, DrugAttributePage, DrugRormulationPage, DrugUnitPage, \
    DrugSpecificationPage, class_set_page, delete_selected_rows
from page_window.purchase_page import PurAddPage, AnOrderPage
from page_window.sell_medicines_page import sell_drug_ui_dialog
from page_window.shelves_drug_page import ShelvesDrugPage
from page_window.stock_medicines_page import StockMedicinesPage, StockLocationPage, StockInAllPage
from page_window.stock_out_page import StockOutPage, StockOutAddDrugPage
from page_window.supplier_medicines_page import SupplierDrugPage, get_selected_logical_rows
from ui_app.add_an_order_ui import Ui_AnOrderDialog


# 其他工具


# from icon_data import icon_data  # 导入生成的图标数据
class PageMap(Enum):
    shelves_drug_tableView = 0  # 药品
    supplier_tableView = 1  # 供应商
    stock_in_tabWidget = 2  # 入库
    inventory_tableView = 3  # 库存
    sales_records_tableView = 4  # 销售
    expiring_drugs_tableView = 5  # 临期
    stock_out_tabWidget = 6  # 出库
    order_tabWidget = 7  # 采购订单
    drugs_on_shelves_tableView = 8  # 最近添加
    inventory_check_tableView = 9  # 库存盘点
    customers_tableView = 10  # 会员客户
    user_tableWidget = 11  # 本地用户
    drug_dic_tableView = 12  # 药品字典


class MainWindow(QMainWindow, ui_app.mainwondows_ui.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind_event()
        self.sub_window_event()
        self.db = data.sqlite_data.DatabaseInit()
        self.sqlite_data()
        class_set_page(self)
        self.actiond.triggered.connect(self.set_dark_theme)
        self.actionlight.triggered.connect(self.set_light_theme)

        # 初始化药品有效期监控数据
        self.initialize_expiring_medicines_monitor()

        # 初始化上架药品信息数据
        self.initialize_shelves_drug_information()

        # 从数据库读取临期提醒阈值并设置到界面
        self.load_expiry_threshold_from_db()

        # 添加定时器定期更新有效期天数
        self.expiry_timer = QTimer(self)
        self.expiry_timer.timeout.connect(self.update_expiry_days)
        # 每天更新一次有效期天数
        self.expiry_timer.start(24 * 60 * 60 * 1000)  # 24小时(毫秒)

        # 程序启动时立即更新一次
        self.update_expiry_days()

    def initialize_shelves_drug_information(self):
        """初始化已有的上架药品信息数据"""
        query = QSqlQuery(self.db)

        # 检查 drug_information_shelves 表是否为空
        query.exec("SELECT COUNT(*) FROM drug_information_shelves")
        if query.next() and query.value(0) == 0:
            print("drug_information_shelves 表为空，开始初始化数据...")
            # 如果上架信息表为空，则初始化所有已有的上架数据
            sql = """
                INSERT OR REPLACE INTO drug_information_shelves 
                (drug_information_shelves_id, drug, expiration_date, purchase_date, shelves_sum, 
                 warehouse_inventory_sum, shelves_location, warehouse_inventory_location, approval_number, manufacturer, batch, supplier)
                SELECT 
                    md.dic_id,
                    md.trade_name,
                    sm.validity,
                    po.order_date,
                    COALESCE(SUM(sd.shelves_number), 0),
                    COALESCE((SELECT SUM(s.quantity) 
                             FROM stock s 
                             WHERE s.drug_id = md.dic_id), 0),
                    COALESCE(wsp.location, ''),
                    COALESCE((SELECT GROUP_CONCAT(wsp2.location, ', ') 
                    FROM warehouse_shelf_position wsp2 
                    JOIN stock s ON s.location = wsp2.warehouse_shelf_id 
                    WHERE s.drug_id = md.dic_id), ''),
                    md.approval_number,
                    md.manufacturer,
                    sm.batch,
                    su.name
                FROM medicine_dic md
                JOIN stock_out_detail sod ON md.dic_id = sod.medicine_id
                JOIN stock_out_main som ON sod.out_id = som.out_id
                JOIN shelves_drug sd ON sd.out_batch = sod.detail_id
                JOIN stock_in_main sm ON sod.stock_batch = sm.in_id
                JOIN purchase_order po ON sm.order_id = po.order_id
                JOIN supplier su ON po.supplier_id = su.supplier_id
                LEFT JOIN warehouse_shelf_position wsp ON sd.location_id = wsp.warehouse_shelf_id
                GROUP BY md.dic_id, sm.validity, po.order_date, md.approval_number, 
                         md.manufacturer, sm.batch, po.supplier_id, wsp.location
            """

            query.exec(sql)

            if query.lastError().isValid():
                print(f"初始化上架药品信息失败: {query.lastError().text()}")
            else:
                print("已初始化上架药品信息数据")

            # 调试信息
            query.exec("SELECT drug, warehouse_inventory_sum FROM drug_information_shelves")
            while query.next():
                print(f"药品: {query.value(0)}, 仓库库存: {query.value(1)}")

    # -------------------------------------------------------------------------------------------------------------------------------

    def initialize_expiring_medicines_monitor(self):  # 初始化已有的药品数据到有效期监控表
        query = QSqlQuery(self.db)

        # 检查 expiring_medicines 表是否为空
        query.exec("SELECT COUNT(*) FROM expiring_medicines")
        if query.next() and query.value(0) == 0:
            # 如果监控表为空，则初始化所有已有的库存数据
            query.exec("""
                INSERT OR REPLACE INTO expiring_medicines 
                (batch_id, medicine_name, expiry_date, days_until_expiry, current_stock, alert_threshold, status, last_updated)
                SELECT 
                    sm.in_id,
                    md.trade_name,
                    sm.validity,
                    CAST(julianday(sm.validity) - julianday('now') AS INTEGER),
                    COALESCE(s.quantity, 0),
                    30,
                    CASE 
                        WHEN CAST(julianday(sm.validity) - julianday('now') AS INTEGER) < 0 THEN '过期'
                        ELSE '正常'
                    END,
                    datetime('now', '+8 hours')
                FROM stock_in_main sm
                JOIN stock_in_detail sd ON sm.in_id = sd.in_id
                JOIN purchase_detail pd ON sd.purchase_detail_id = pd.detail_id
                JOIN medicine_dic md ON pd.medicine_id = md.dic_id
                LEFT JOIN stock s ON s.batch = sm.in_id
                WHERE sm.validity IS NOT NULL
            """)

            if query.lastError().isValid():
                print(f"初始化监控数据失败: {query.lastError().text()}")
            else:
                print("已初始化药品有效期监控数据")

    def load_expiry_threshold_from_db(self):  # 从数据库加载临期提醒阈值
        query = QSqlQuery(self.db)
        # 获取第一个记录的预警阈值作为默认值
        query.exec("SELECT alert_threshold FROM expiring_medicines LIMIT 1")

        if query.next():
            threshold = query.value(0)
            if threshold is not None:
                self.expiring_drugs_lineEdit_day.setText(str(threshold))

    def update_medicine_status(self):  # 更新所有药品的状态
        query = QSqlQuery(self.db)

        # 更新 expiring_medicines 表中的 status 字段
        query.exec("""
            UPDATE expiring_medicines
            SET status = CASE
                WHEN days_until_expiry < 0 THEN '过期'
                ELSE '正常'
            END,
            last_updated = datetime('now', '+8 hours')
        """)

        print("药品状态更新完成")

    def update_expiry_days(self):  # 更新所有药品的有效期天数和状态
        query = QSqlQuery(self.db)

        # 更新 expiring_medicines 表中的 days_until_expiry 字段和状态
        query.exec("""
            UPDATE expiring_medicines 
            SET days_until_expiry = CAST(julianday(expiry_date) - julianday('now') AS INTEGER),
                status = CASE 
                    WHEN CAST(julianday(expiry_date) - julianday('now') AS INTEGER) < 0 THEN '过期'
                    ELSE '正常'
                END,
                last_updated = datetime('now', '+8 hours')
        """)

        # 删除已经过期很久的记录(过期超过30天)
        query.exec("""
            DELETE FROM expiring_medicines 
            WHERE days_until_expiry < -30
        """)

        print("有效期天数和状态更新完成")

        # 检查是否有即将过期的药品
        self.check_expiring_soon_medicines()

    def check_expiring_soon_medicines(self):  # 检查即将过期的药品并提醒
        # 首先从界面获取当前设置的阈值
        try:
            default_threshold = int(self.expiring_drugs_lineEdit_day.text())
        except ValueError:
            default_threshold = 60  # 默认值

        query = QSqlQuery(self.db)
        query.prepare("""
            SELECT medicine_name, expiry_date, days_until_expiry, current_stock, alert_threshold
            FROM expiring_medicines 
            WHERE days_until_expiry <= COALESCE(alert_threshold, ?)
            AND days_until_expiry >= -30  -- 仍然显示过期不超过30天的药品
            ORDER BY days_until_expiry ASC
        """)
        query.addBindValue(default_threshold)

        if query.exec():
            expiring_soon_medicines = []
            while query.next():
                medicine_name = query.value(0)
                expiry_date = query.value(1)
                days_until_expiry = query.value(2)
                current_stock = query.value(3)
                alert_threshold = query.value(4) or default_threshold

                expiring_soon_medicines.append({
                    'name': medicine_name,
                    'expiry_date': expiry_date,
                    'days_until_expiry': days_until_expiry,
                    'current_stock': current_stock,
                    'alert_threshold': alert_threshold
                })

            # 如果有即将过期的药品，显示提醒
            if expiring_soon_medicines:
                self.show_expiry_warning(expiring_soon_medicines)

    def save_expiry_threshold(self):  # 保存临期提醒阈值
        try:
            threshold_days = int(self.expiring_drugs_lineEdit_day.text())
            if threshold_days < 0:
                QMessageBox.warning(self, "输入错误", "临期提醒天数不能为负数")
                return

            # 更新数据库中所有记录的预警阈值
            query = QSqlQuery(self.db)
            query.prepare("UPDATE expiring_medicines SET alert_threshold = ?")
            query.addBindValue(threshold_days)

            if query.exec():
                QMessageBox.information(self, "成功", f"已将临期提醒阈值设置为{threshold_days}天")
                # 重新加载临期药品数据
                data.sqlite_data.get_expiring_medicine_model(self)
            else:
                QMessageBox.critical(self, "数据库错误", f"更新失败: {query.lastError().text()}")

        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的数字")

    def show_expiry_warning(self, medicines):  # 显示药品即将过期的警告
        if len(medicines) > 0:
            warning_msg = "以下药品即将过期，请及时处理：\n\n"
            for med in medicines:
                warning_msg += f"• {med['name']} - 剩余{med['days_until_expiry']}天 - 库存:{med['current_stock']}\n"

            # 可以使用状态栏显示或者弹出消息框
            self.statusbar.showMessage(warning_msg, 20000)  # 显示20秒

            # 对于紧急情况(7天内过期)，可以弹出消息框
            urgent_medicines = [med for med in medicines if med['days_until_expiry'] <= 7]
            if urgent_medicines:
                urgent_msg = "紧急提醒：以下药品将在7天内过期！\n\n"
                for med in urgent_medicines:
                    urgent_msg += f"• {med['name']} - 剩余{med['days_until_expiry']}天 - 库存:{med['current_stock']}\n"

                QMessageBox.warning(self, "药品临期紧急提醒", urgent_msg)

    # ------------------------------------------------------------------------------------------------------------

    def sqlite_data(self):
        # data.sqlite_data.get_medicines_model(self)  # 药品
        data.sqlite_data.get_sales_model(self)  # 销售
        data.sqlite_data.get_expiring_medicine_model(self)  # 临期
        data.sqlite_data.get_supplier_model(self)  # 供应商
        data.sqlite_data.get_inventory_model(self)  # 库存
        data.sqlite_data.get_stock_in_main_model(self)  # 入库
        data.sqlite_data.get_stock_in_detail_model(self)  # 入库明细
        data.sqlite_data.get_stock_out_main_model(self)  # 出库
        data.sqlite_data.get_stock_out_detail_model(self)  # 出库明细
        data.sqlite_data.get_purchase_order_model(self)  # 采购订单
        data.sqlite_data.get_purchase_order_detail_model(self)  # 采购订单明细
        data.sqlite_data.get_inventory_check(self)  # 库存盘点
        data.sqlite_data.get_medicine_dic_model(self)  # 药品字典
        data.sqlite_data.get_shelves_drug_model(self)  # 上架药品
        data.sqlite_data.get_shelves_drug_message_model(self)

        self.stock_in_tabWidget.currentChanged.connect(self.tab_changed)  # 入库标签切换时触发

    def tab_changed(self, index):
        """标签切换时触发"""
        print(f"已切换到标签页: {index} ({self.stock_in_tabWidget.tabText(index)})")

    # 添加暗色主题设置方法
    def set_dark_theme(self):
        """设置暗色主题"""
        QApplication.instance().setStyleSheet(dark(QApplication.instance()))

    # 添加浅色主题设置方法
    def set_light_theme(self):
        """设置浅色主题"""
        QApplication.instance().setStyleSheet(light(QApplication.instance()))

    def bind_event(self):
        self.medicine.clicked.connect(lambda: self.show_page_by_name(PageMap.shelves_drug_tableView.value))
        self.sales_records.clicked.connect(lambda: self.show_page_by_name(PageMap.sales_records_tableView.value))
        self.expiring_medicine.clicked.connect(lambda: self.show_page_by_name(PageMap.expiring_drugs_tableView.value))
        self.pharmacy_operation_record.clicked.connect(
            lambda: self.show_page_by_name(PageMap.inventory_tableView.value))
        self.supplier.clicked.connect(lambda: self.show_page_by_name(PageMap.supplier_tableView.value))
        self.drug_inbound.clicked.connect(lambda: self.show_page_by_name(PageMap.stock_in_tabWidget.value))
        self.drug_outbound.clicked.connect(lambda: self.show_page_by_name(PageMap.stock_out_tabWidget.value))
        self.drugs_on_shelves.clicked.connect(lambda: self.show_page_by_name(PageMap.drugs_on_shelves_tableView.value))
        self.medicine_purchase.clicked.connect(lambda: self.show_page_by_name(PageMap.order_tabWidget.value))
        self.inventory_record.clicked.connect(lambda: self.show_page_by_name(PageMap.inventory_check_tableView.value))
        self.member_customer.clicked.connect(lambda: self.show_page_by_name(PageMap.customers_tableView.value))
        self.user_information.clicked.connect(lambda: self.show_page_by_name(PageMap.user_tableWidget.value))
        self.drug_dic_btn.clicked.connect(lambda: self.show_page_by_name(PageMap.drug_dic_tableView.value))
        self.add_stock_location_btn.clicked.connect(self.add_stock_location)
        self.stock_in_all_btn.clicked.connect(self.stock_in_all)
        self.drug_dic_del_btn.clicked.connect(self.del_dic)
        self.supplier_del_btn.clicked.connect(self.supplier_del)
        self.supplier_mod_btn.clicked.connect(self.supplier_mod)
        self.purchase_del_btn.clicked.connect(self.purchase_del)
        self.purchase_mod_btn.clicked.connect(self.purchase_modify)
        self.stock_del_btn.clicked.connect(self.stock_del)
        self.stock_mod_btn.clicked.connect(self.stock_mod)
        self.stock_out_mod_btn.clicked.connect(self.stock_out_mod)
        self.stock_out_del_btn.clicked.connect(self.stock_out_del)
        self.inventory_check_del_btn.clicked.connect(self.inventory_check_del)
        self.inventory_check_mod_btn.clicked.connect(self.inventory_check_mod)
        self.shelves_del_btn.clicked.connect(self.shelves_del)
        self.shelves_mod_btn.clicked.connect(self.shelves_mod)
        self.inventory_del_btn.clicked.connect(self.inventory_del)
        self.expiring_drugs_save_btn.clicked.connect(self.save_expiry_threshold)

        self.drug_ref_btn.clicked.connect(self.drug_ref)
        self.ex_ref_btn.clicked.connect(self.ex_ref)

    def drug_ref(self):
        data.sqlite_data.get_shelves_drug_message_model(self)

    def ex_ref(self):
        data.sqlite_data.get_expiring_medicine_model(self)

    def stock_in_all(self):
        self.stock_all = StockInAllPage(self)
        self.stock_all.exec()

    def add_stock_location(self):
        self.stock_location = StockLocationPage(self)
        self.stock_location.exec()

    def del_dic(self):
        self.dic = DrugDicModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.drug_dic_tableView,
            model=self.dic,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_medicine_dic_model(self)
            self.drug_dic_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    def supplier_mod(self):
        selected_rows = get_selected_logical_rows(self.supplier_tableView)
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请先选择要修改的供应商记录")
            return

        # 获取选中行的supplier_id
        model = self.supplier_tableView.model()
        if model and len(selected_rows) > 0:
            # 假设supplier_id在第一列（索引为0）
            supplier_id = model.data(model.index(selected_rows[0], 0))

            self.sup = SupplierDrugPage(self)
            self.sup.show_mod_supplier_data(supplier_id)  # 先填充数据
            if self.sup.exec() == QDialog.DialogCode.Accepted:  # 如果成功保存
                data.sqlite_data.get_supplier_model(self)  # 刷新供应商列表

    def supplier_del(self):
        self.supp = SupplierModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.supplier_tableView,
            model=self.supp,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_supplier_model(self)
            self.supplier_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    def purchase_del(self):
        # 获取当前采购标签页的索引
        current_order_tab_index = self.order_tabWidget.currentIndex()
        if current_order_tab_index == 0:  # 采购订单表
            self.pur = PurchaseOrderModel(self, self.db)
            success, msg = delete_selected_rows(
                self=self,
                tableView=self.purchase_order_tableView,
                model=self.pur,
                db=self.db,
            )
            if success:
                QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
                data.sqlite_data.get_purchase_order_model(self)
                self.purchase_order_tableView.clearSelection()
            else:
                QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

        elif current_order_tab_index == 1:  # 采购明细表
            from data.sqlite_data import PurchaseDetailModel
            self.pur_detail = PurchaseDetailModel(self, self.db)
            success, msg = delete_selected_rows(
                self=self,
                tableView=self.purchase_detail_tableView,
                model=self.pur_detail,
                db=self.db,
            )
            if success:
                QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
                data.sqlite_data.get_purchase_order_detail_model(self)
                self.purchase_detail_tableView.clearSelection()
            else:
                QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    def stock_del(self):
        # 获取当前采购标签页的索引
        current_order_tab_index = self.stock_in_tabWidget.currentIndex()
        if current_order_tab_index == 0:
            self.stock = StockInMainModel(self, self.db)
            success, msg = delete_selected_rows(
                self=self,
                tableView=self.main_tableView,
                model=self.stock,
                db=self.db,
            )
            if success:
                QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
                data.sqlite_data.get_stock_in_main_model(self)
                self.main_tableView.clearSelection()
            else:
                QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

        if current_order_tab_index == 1:
            self.stock = StockInDetailModel(self, self.db)
            success, msg = delete_selected_rows(
                self=self,
                tableView=self.detail_tableView,
                model=self.stock,
                db=self.db,
            )
            if success:
                QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
                data.sqlite_data.get_stock_in_detail_model(self)
                self.detail_tableView.clearSelection()
            else:
                QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    def stock_out_del(self):
        # 获取当前出库标签页的索引
        current_tab_index = self.stock_out_tabWidget.currentIndex()

        if current_tab_index == 0:  # 出库主表
            self.stock = StockOutMainModel(self, self.db)
            success, msg = delete_selected_rows(
                self=self,
                tableView=self.stock_out_main_tableView,
                model=self.stock,
                db=self.db,
            )
            if success:
                QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
                data.sqlite_data.get_stock_out_main_model(self)
                self.stock_out_main_tableView.clearSelection()
            else:
                QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

        elif current_tab_index == 1:  # 出库明细表
            from data.sqlite_data import StockOutDetailModel
            self.stock_detail = StockOutDetailModel(self, self.db)
            success, msg = delete_selected_rows(
                self=self,
                tableView=self.stock_out_detail_tableView,
                model=self.stock_detail,
                db=self.db,
            )
            if success:
                QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
                data.sqlite_data.get_stock_out_detail_model(self)
                self.stock_out_detail_tableView.clearSelection()
            else:
                QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    def inventory_check_del(self):
        self.inventory_check_model = InventoryCheckModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.inventory_check_tableView,
            model=self.inventory_check_model,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_inventory_check(self)
            self.inventory_check_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    def shelves_del(self):
        self.shelves = ShelvesDrugModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.drugs_on_shelves_tableView,
            model=self.shelves,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_shelves_drug_model(self)
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    def inventory_del(self):
        self.inventory = InventoryModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.inventory_tableView,
            model=self.inventory,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_inventory_model(self)
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    def stock_mod(self):
        selected_rows = get_selected_logical_rows(self.main_tableView)
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请先选择要修改的记录")
            return

        model = self.main_tableView.model()
        if model and len(selected_rows) > 0:
            stock_in_id = model.data(model.index(selected_rows[0], 0))

            self.sup = StockMedicinesPage(self)
            self.sup.load_order_data(stock_in_id)  # 先填充数据
            if self.sup.exec() == QDialog.DialogCode.Accepted:  # 如果成功保存
                data.sqlite_data.get_stock_in_main_model(self)
                data.sqlite_data.get_stock_in_detail_model(self)

    def shelves_mod(self):
        selected_rows = get_selected_logical_rows(self.drugs_on_shelves_tableView)
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请先选择要修改的记录")
            return
        model = self.drugs_on_shelves_tableView.model()
        if model and len(selected_rows) > 0:
            shelves_id = model.data(model.index(selected_rows[0], 0))
            self.shelves = ShelvesDrugPage(self)
            self.shelves.update_load_data(shelves_id)
            self.shelves.exec()
            data.sqlite_data.get_shelves_drug_model(self)

    def purchase_modify(self):
        """修改采购订单"""
        current_order_tab_index = self.order_tabWidget.currentIndex()

        if current_order_tab_index == 0:  # 采购订单表
            selected_rows = get_selected_logical_rows(self.purchase_order_tableView)
            if not selected_rows:
                QMessageBox.warning(self, "警告", "请先选择要修改的采购订单记录")
                return

            # 获取选中行的order_id
            model = self.purchase_order_tableView.model()
            if model and len(selected_rows) > 0:
                order_id = model.data(model.index(selected_rows[0], 0))  # 假设ID在第一列

                self.pu = AnOrderPage(self)
                self.pu.load_order(order_id)  # 加载订单数据
                self.pu.exec()

                # 更新数据
                data.sqlite_data.get_purchase_order_model(self)
                data.sqlite_data.get_purchase_order_detail_model(self)

        if current_order_tab_index == 1:  # 采购订单明细表
            selected_rows = get_selected_logical_rows(self.purchase_detail_tableView)
            if not selected_rows:
                QMessageBox.warning(self, "警告", "请先选择要修改的药品订单记录")
                return
            model = self.purchase_detail_tableView.model()
            if model and len(selected_rows) > 0:
                detail_id = model.data(model.index(selected_rows[0], 0))
                self.pu = PurAddPage(self)
                self.pu.load_order_data(detail_id)
                self.pu.exec()
                data.sqlite_data.get_purchase_order_model(self)
                data.sqlite_data.get_purchase_order_detail_model(self)

    def stock_out_mod(self):
        current_tab_index = self.stock_out_tabWidget.currentIndex()
        if current_tab_index == 0:
            selected_rows = get_selected_logical_rows(self.stock_out_main_tableView)
            if not selected_rows:
                QMessageBox.warning(self, "警告", "请先选择要修改的出库订单记录")
                return
            model = self.stock_out_main_tableView.model()
            if model and len(selected_rows) > 0:
                out_id = model.data(model.index(selected_rows[0], 0))
                self.so = StockOutPage(self)
                self.so.load_stock_out_data(out_id)
                self.so.exec()
                data.sqlite_data.get_stock_out_main_model(self)
                data.sqlite_data.get_stock_out_detail_model(self)
        if current_tab_index == 1:
            selected_rows = get_selected_logical_rows(self.stock_out_detail_tableView)
            if not selected_rows:
                QMessageBox.warning(self, "警告", "请先选择要修改的出库订单记录")
                return
            model = self.stock_out_detail_tableView.model()
            if model and len(selected_rows) > 0:
                detail_id = model.data(model.index(selected_rows[0], 0))
                self.so = StockOutAddDrugPage(self)
                self.so.load_stock_out_update_data(detail_id)
                self.so.exec()
                data.sqlite_data.get_stock_out_main_model(self)
                data.sqlite_data.get_stock_out_detail_model(self)

    def inventory_check_mod(self):
        selected_rows = get_selected_logical_rows(self.inventory_check_tableView)
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请先选择要修改的盘点记录")
            return
        model = self.inventory_check_tableView.model()
        if model and len(selected_rows) > 0:
            check_id = model.data(model.index(selected_rows[0], 0))
            self.ic = InventoryCountPage(self)
            self.ic.load_check_out_data(check_id)
            self.ic.exec()
            data.sqlite_data.get_inventory_check(self)

    # -------------------------------------------------------------------------------------------------------------------------------
    # 添加跳出子窗口事件
    def sub_window_event(self):
        self.drug_add_btn.clicked.connect(self.drug_adds)
        self.drugs_set_btn.clicked.connect(self.drug_attribute)
        self.dosage_set_btn.clicked.connect(self.drug_rormulation)
        self.unit_set_btn.clicked.connect(self.drug_unit)
        self.specifications_set_btn.clicked.connect(self.drug_specification)
        self.sell_drug_dtn.clicked.connect(self.sell_drug_func)
        self.supplier_add_btn.clicked.connect(self.supplier_add)
        self.stock_in_btn.clicked.connect(self.stock_in)
        self.purchase_add_btn.clicked.connect(self.purchase_add)
        self.add_an_order_btn.clicked.connect(self.add_an_order)
        self.stock_out_add_btn.clicked.connect(self.stock_out)
        self.stock_out_add_drug_btn.clicked.connect(self.stock_out_add_drug)
        self.inventory_check_add_btn.clicked.connect(self.inventory_check_add)
        self.shelves_add_btn.clicked.connect(self.shelves_add)

    def shelves_add(self):
        self.shelves = ShelvesDrugPage(self)
        self.shelves.exec()
        data.sqlite_data.get_shelves_drug_model(self)

    # 药品添加
    def drug_adds(self):
        self.drug_add = MedicinesPage(self)
        self.drug_add.exec()

    def drug_attribute(self):
        self.drug_att = DrugAttributePage(self)
        self.drug_att.exec()
        # self.drug_att.show()

    def drug_rormulation(self):
        self.drug_ror = DrugRormulationPage(self)
        self.drug_ror.exec()

    def drug_unit(self):
        self.drug_un = DrugUnitPage(self)
        self.drug_un.exec()

    def drug_specification(self):
        self.drug_sp = DrugSpecificationPage(self)
        self.drug_sp.exec()

    def sell_drug_func(self):
        self.sell_d = sell_drug_ui_dialog(self)
        self.sell_d.show()

    def supplier_add(self):
        self.sup = SupplierDrugPage(self)
        self.sup.load_supplier_time()
        self.sup.exec()
        data.sqlite_data.get_supplier_model(self)

    def stock_in(self):
        self.stock_inbo = StockMedicinesPage(self)
        self.stock_inbo.exec()
        data.sqlite_data.get_stock_in_main_model(self)
        data.sqlite_data.get_stock_in_detail_model(self)

    def purchase_add(self):
        self.pu = PurAddPage(self)
        self.pu.exec()
        data.sqlite_data.get_purchase_order_detail_model(self)

    def add_an_order(self):
        self.puan = AnOrderPage(self)
        self.puan.exec()
        data.sqlite_data.get_purchase_order_model(self)

    def stock_out(self):
        self.stock_out_page = StockOutPage(self)
        self.stock_out_page.exec()
        data.sqlite_data.get_stock_out_main_model(self)
        data.sqlite_data.get_stock_out_detail_model(self)

    def stock_out_add_drug(self):
        self.stock_out_add_dr = StockOutAddDrugPage(self)
        self.stock_out_add_dr.exec()
        data.sqlite_data.get_stock_out_main_model(self)
        data.sqlite_data.get_stock_out_detail_model(self)

    def inventory_check_add(self):
        self.inventory_check_add_page = InventoryCountPage(self)
        self.inventory_check_add_page.exec()
        data.sqlite_data.get_inventory_check(self)

    def show_page_by_name(self, page_name):
        """通过页面名称切换页面"""
        if page_name in PageMap:
            # 切换到目标页面
            self.stackedWidget.setCurrentIndex(page_name)
            # 这里可以添加页面切换时的额外逻辑
            print(f"已切换到页面: {page_name}")
        else:
            print(f"错误: 找不到页面 '{page_name}'")

        if page_name == PageMap.drug_dic_tableView.value:
            data.sqlite_data.get_medicine_dic_model(self)
        if page_name == PageMap.stock_in_tabWidget.value:
            data.sqlite_data.get_stock_in_main_model(self)
            data.sqlite_data.get_stock_in_detail_model(self)
            # data.sqlite_data.get_inventory_datch_model(self)
        if page_name == PageMap.stock_out_tabWidget.value:
            data.sqlite_data.get_stock_out_main_model(self)
            data.sqlite_data.get_stock_out_detail_model(self)
        if page_name == PageMap.order_tabWidget.value:
            data.sqlite_data.get_purchase_order_model(self)
            data.sqlite_data.get_purchase_order_detail_model(self)
        if page_name == PageMap.inventory_check_tableView.value:
            data.sqlite_data.get_inventory_check(self)
        if page_name == PageMap.shelves_drug_tableView.value:
            data.sqlite_data.get_shelves_drug_message_model(self)
            class_set_page(self)
        if page_name == PageMap.inventory_tableView.value:
            data.sqlite_data.get_inventory_model(self)
        if page_name == PageMap.sales_records_tableView.value:
            data.sqlite_data.get_sales_model(self)
        if page_name == PageMap.expiring_drugs_tableView.value:
            data.sqlite_data.get_expiring_medicine_model(self)
        if page_name == PageMap.supplier_tableView.value:
            data.sqlite_data.get_supplier_model(self)


class LoginWindow(QWidget, ui_app.log_in_ui.Ui_Form):
    login_success = Signal()  # 自定义信号，用于通知登录成功

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind_event()

    def bind_event(self):
        self.log_on_btn.clicked.connect(self.login)
        self.mainwindow = MainWindow()
        # 连接信号：登录成功后显示主窗口
        self.login_success.connect(self.mainwindow.show)

    def login(self):
        account = self.account_le.text().strip()
        password = self.password_le.text().strip()
        query = QSqlQuery()
        # query.exec(f"SELECT * FROM users WHERE account='{account}' AND password='{password}'")
        if account == "" and password == "":
            # if query.exec(f"SELECT * FROM users WHERE account='{account}' AND password='{password}'"):
            self.login_success.emit()  # 发射成功信号
            self.close()  # 关闭登录窗口
            # print("支持的数据库驱动:", QSqlDatabase.drivers())
        else:
            self.account_le.clear()
            self.password_le.clear()
            self.tiplb.setText("用户名或密码错误")


if __name__ == "__main__":
    app = QApplication([])
    # icon_bytes = QByteArray(base64.b64decode(icon_data))
    # pixmap = QPixmap()
    # pixmap.loadFromData(icon_bytes, "ICO")  # 指定格式为 ICO
    # icon = QIcon(pixmap)

    # 设置主题
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    # dark(app)
    # 暗色主题
    app.setStyleSheet(dark(app))
    # 亮色主题
    # app.setStyleSheet(light(app))

    # app.setWindowIcon(icon)
    LoginWindow = LoginWindow()
    # window.setWindowIcon(icon)
    LoginWindow.show()
    app.exec()
