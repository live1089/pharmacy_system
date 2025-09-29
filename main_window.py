from enum import Enum

from PySide6.QtCore import QTimer, QDate, QDateTime
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMainWindow, QMessageBox

import qdarktheme
from qdarktheme.qtpy.QtWidgets import QApplication
from qtmodern.styles import dark

import data.sqlite_data
import query_methods as qu
import window_methods as wim
from page_window.medicines_page import class_set_page
from ui_app.mainwondows_ui import Ui_mainWindow

# 其他工具
start_times = QDateTime.currentDateTime().addDays(-30).date().toString("yyyy-MM-dd")
end_times = QDateTime.currentDateTime().addDays(+1).date().toString("yyyy-MM-dd")


class PageMap(Enum):
    shelves_drug_tableView = 0  # 药品
    supplier_tableView = 1  # 供应商
    stock_in_tabWidget = 2  # 入库
    inventory_tableView = 3  # 库存操作记录
    stock_tabWidget = 4  # 库存余量
    expiring_drugs_tableView = 5  # 临期
    stock_out_tabWidget = 6  # 出库
    order_tabWidget = 7  # 采购订单
    drugs_on_shelves_tableView = 8  # 最近添加
    inventory_check_tableView = 9  # 库存盘点
    drug_dic_tableView = 11  # 药品字典


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = data.sqlite_data.DatabaseInit()
        self.bind_event()
        wim.sub_window_event(self)
        # 首先设置查询时间
        self.set_query_time()

        # 然后加载数据
        self.sqlite_data()

        class_set_page(self)
        self.actiond.triggered.connect(self.set_grey_theme)
        self.actionlight.triggered.connect(self.set_light_theme)
        self.actionm.triggered.connect(self.set_dark_theme)

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

        # 添加库存预警检查定时器
        self.stock_warning_timer = QTimer(self)
        self.stock_warning_timer.timeout.connect(self.check_stock_warnings)
        self.stock_warning_timer.start(30 * 60 * 1000)  # 每30分钟检查一次

        # 程序启动时立即检查一次
        self.check_stock_warnings()

    def set_query_time(self):
        # 采购 - 设置默认为最近30天
        self.purchase_order_dateEdit_start.setDate(QDate.currentDate().addDays(-30))
        self.purchase_order_dateEdit_deadline.setDate(QDate.currentDate().addDays(+1))

        # 入库 - 默认最近30天
        self.storage_dateEdit_start.setDate(QDate.currentDate().addDays(-30))
        self.storage_dateEdit_deadline_end.setDate(QDate.currentDate().addDays(+1))

        # 入库记录 - 设置默认为最近30天
        self.inventory_dateEdit_start.setDate(QDate.currentDate().addDays(-30))
        self.inventory_dateEdit_deadline.setDate(QDate.currentDate().addDays(+1))

        # 出库 - 设置默认为最近30天
        self.stock_out_dateEdit_start.setDate(QDate.currentDate().addDays(-30))
        self.stock_out_dateEdit_deadline.setDate(QDate.currentDate().addDays(+1))

        # 库存盘点 - 设置默认为最近30天
        self.inventory_check_dateEdit_start.setDate(QDate.currentDate().addDays(-30))
        self.inventory_check_dateEdit_deadline.setDate(QDate.currentDate().addDays(+1))

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
                    COALESCE((SELECT SUM(s.quantity) FROM stock s WHERE s.batch = sm.in_id), 0),
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
                WHERE sm.validity IS NOT NULL
                GROUP BY sm.in_id, md.trade_name, sm.validity
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
            default_threshold = 30  # 使用默认值30天而不是60天

        query = QSqlQuery(self.db)
        query.prepare("""
            SELECT medicine_name, expiry_date, days_until_expiry, current_stock, alert_threshold
            FROM expiring_medicines 
            WHERE days_until_expiry <= COALESCE(alert_threshold, ?)
            AND days_until_expiry >= -30  -- 仍然显示过期不超过30天的药品
            AND current_stock > 0  -- 只提醒还有库存的药品
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
        data.sqlite_data.get_expiring_medicine_model(self)  # 临期
        data.sqlite_data.get_supplier_model(self)  # 供应商
        data.sqlite_data.get_inventory_model(self, start_times, end_times)  # 库存
        data.sqlite_data.get_stock_in_main_model(self, start_times, end_times)  # 入库
        data.sqlite_data.get_stock_in_detail_model(self, start_times, end_times)  # 入库明细
        data.sqlite_data.get_stock_out_main_model(self, start_times, end_times)  # 出库
        data.sqlite_data.get_stock_out_detail_model(self, start_times, end_times)  # 出库明细
        data.sqlite_data.get_purchase_order_model(self, start_times, end_times)  # 采购订单
        data.sqlite_data.get_purchase_order_detail_model(self, start_times, end_times)  # 采购订单明细
        data.sqlite_data.get_inventory_check(self, start_times, end_times)  # 库存盘点
        data.sqlite_data.get_medicine_dic_model(self)  # 药品字典
        data.sqlite_data.get_shelves_drug_model(self)  # 上架药品

        data.sqlite_data.get_stock_in_all_model(self)
        data.sqlite_data.get_shelves_stock_model(self)
        data.sqlite_data.setup_warning_display(self)
        data.sqlite_data.setup_warning_stock(self)
        data.sqlite_data.get_shelves_drug_message_model(self)

        self.stock_in_tabWidget.currentChanged.connect(self.tab_changed)  # 入库标签切换时触发

    def tab_changed(self, index):
        """标签切换时触发"""
        print(f"已切换到标签页: {index} ({self.stock_in_tabWidget.tabText(index)})")

    # -------------------------------------------------------------------------------------------------------------

    # 添加暗色主题设置方法
    def set_grey_theme(self):
        """设置暗色主题"""
        QApplication.instance().setStyleSheet(dark(QApplication.instance()))

    # 添加浅色主题设置方法
    def set_light_theme(self):
        """设置浅色主题"""
        QApplication.instance().setStyleSheet(qdarktheme.load_stylesheet("light"))

    def set_dark_theme(self):
        QApplication.instance().setStyleSheet(qdarktheme.load_stylesheet("dark"))

    # -------------------------------------------------------------------------------------------------------------
    def bind_event(self):
        self.medicine.clicked.connect(lambda: self.show_page_by_name(PageMap.shelves_drug_tableView.value))
        self.expiring_medicine.clicked.connect(lambda: self.show_page_by_name(PageMap.expiring_drugs_tableView.value))
        self.pharmacy_operation_record.clicked.connect(
            lambda: self.show_page_by_name(PageMap.inventory_tableView.value))
        self.supplier.clicked.connect(lambda: self.show_page_by_name(PageMap.supplier_tableView.value))
        self.drug_inbound.clicked.connect(lambda: self.show_page_by_name(PageMap.stock_in_tabWidget.value))
        self.drug_outbound.clicked.connect(lambda: self.show_page_by_name(PageMap.stock_out_tabWidget.value))
        self.drugs_on_shelves.clicked.connect(lambda: self.show_page_by_name(PageMap.drugs_on_shelves_tableView.value))
        self.medicine_purchase.clicked.connect(lambda: self.show_page_by_name(PageMap.order_tabWidget.value))
        self.inventory_record.clicked.connect(lambda: self.show_page_by_name(PageMap.inventory_check_tableView.value))
        self.drug_dic_btn.clicked.connect(lambda: self.show_page_by_name(PageMap.drug_dic_tableView.value))

        self.add_stock_location_btn.clicked.connect(lambda: wim.add_stock_location(self))
        self.stock_in_all_btn.clicked.connect(lambda: self.show_page_by_name(PageMap.stock_tabWidget.value))
        # self.stock_in_all_btn.clicked.connect(lambda: wim.stock_in_all(self))
        self.drug_dic_del_btn.clicked.connect(lambda: wim.del_dic(self))
        self.supplier_del_btn.clicked.connect(lambda: wim.supplier_del(self))
        self.supplier_mod_btn.clicked.connect(lambda: wim.supplier_mod(self))
        self.purchase_del_btn.clicked.connect(lambda: wim.purchase_del(self))
        self.purchase_mod_btn.clicked.connect(lambda: wim.purchase_modify(self))
        self.stock_del_btn.clicked.connect(lambda: wim.stock_del(self))
        self.stock_mod_btn.clicked.connect(lambda: wim.stock_mod(self))
        self.stock_out_mod_btn.clicked.connect(lambda: wim.stock_out_mod(self))
        self.stock_out_del_btn.clicked.connect(lambda: wim.stock_out_del(self))
        self.inventory_check_del_btn.clicked.connect(lambda: wim.inventory_check_del(self))
        self.inventory_check_mod_btn.clicked.connect(lambda: wim.inventory_check_mod(self))
        self.shelves_del_btn.clicked.connect(lambda: wim.shelves_del(self))
        self.shelves_mod_btn.clicked.connect(lambda: wim.shelves_mod(self))
        self.inventory_del_btn.clicked.connect(lambda: wim.inventory_del(self))
        self.drug_revise_btn.clicked.connect(lambda: wim.drug_revise(self))
        self.expiring_drugs_save_btn.clicked.connect(self.save_expiry_threshold)
        self.drug_ref_btn.clicked.connect(self.drug_ref)
        self.ex_ref_btn.clicked.connect(self.ex_ref)

        self.purchase_order_btn.clicked.connect(lambda: qu.pur_order(self))
        self.stock_out_query_btn.clicked.connect(lambda: qu.stock_out_query(self))
        self.inventory_check_query_btn.clicked.connect(lambda: qu.inventory_check_query(self))
        self.inventory_btn.clicked.connect(lambda: qu.inventory_record_query(self))
        self.supplier_query_btn.clicked.connect(lambda: qu.supplier_query(self))
        self.drug_selection_query_btn.clicked.connect(lambda: qu.drug_selection_query(self))
        self.stock_in_query_btn.clicked.connect(lambda: qu.stock_in_query(self))
        self.storage_btn.clicked.connect(lambda: qu.storage_query(self))
        self.purchase_order_select_btn.clicked.connect(lambda: qu.purchase_order_select(self))
        self.stock_out_list_select_btn.clicked.connect(lambda: qu.stock_out_number_select(self))
        self.shelves_select_btn.clicked.connect(lambda: qu.shelves_select(self))
        self.clear_btn.clicked.connect(lambda: self.clean_up_system_data())

        self.display_area_inquiry_btn.clicked.connect(lambda: qu.display_area_inquiry(self))
        self.drug_library_query_btn.clicked.connect(lambda: qu.drug_library_query(self))

    # 添加清理系统数据的方法
    def clean_up_system_data(self):
        """
        清理系统垃圾数据
        """
        reply = QMessageBox.question(
            self,
            '确认清理',
            '确定要清理系统垃圾数据吗？\n此操作将删除过期和无用的数据记录。',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                from data.clean_up_useless_data import clean_up_useless_data
                clean_up_useless_data(self)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"清理功能执行失败: {str(e)}")

    def drug_ref(self):
        data.sqlite_data.get_shelves_drug_message_model(self)

    def ex_ref(self):
        data.sqlite_data.get_expiring_medicine_model(self)

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
            data.sqlite_data.get_stock_in_main_model(self, start_times, end_times)
            data.sqlite_data.get_stock_in_detail_model(self, start_times, end_times)
        if page_name == PageMap.stock_out_tabWidget.value:
            data.sqlite_data.get_stock_out_main_model(self, start_times, end_times)
            data.sqlite_data.get_stock_out_detail_model(self, start_times, end_times)
        if page_name == PageMap.order_tabWidget.value:
            data.sqlite_data.get_purchase_order_model(self, start_times, end_times)
            data.sqlite_data.get_purchase_order_detail_model(self, start_times, end_times)
        if page_name == PageMap.inventory_check_tableView.value:
            data.sqlite_data.get_inventory_check(self, start_times, end_times)
        if page_name == PageMap.shelves_drug_tableView.value:
            data.sqlite_data.get_shelves_drug_message_model(self)
            class_set_page(self)
        if page_name == PageMap.inventory_tableView.value:
            data.sqlite_data.get_inventory_model(self, start_times, end_times)
        if page_name == PageMap.stock_tabWidget.value:
            data.sqlite_data.get_stock_in_all_model(self)
            data.sqlite_data.get_shelves_stock_model(self)
            data.sqlite_data.setup_warning_display(self)
            data.sqlite_data.setup_warning_stock(self)
        if page_name == PageMap.expiring_drugs_tableView.value:
            data.sqlite_data.get_expiring_medicine_model(self)
        if page_name == PageMap.supplier_tableView.value:
            data.sqlite_data.get_supplier_model(self)

    # 检查库存预警
    def check_stock_warnings(self):
        query = QSqlQuery()
        query.prepare(
            "SELECT medicine_dic.dic_id, display_area_threshold, pharmacy_threshold "
            "FROM medicine_dic")

        if query.exec():
            has_data = False
            while query.next():
                has_data = True
                dic_id = query.value(0)
                display_area_threshold = query.value(1) if query.value(1) is not None else 0
                pharmacy_threshold = query.value(2) if query.value(2) is not None else 0

                # 为每个药品检查库存预警
                try:
                    stock_warning_model = qu.get_low_stock_warning(self, pharmacy_threshold)
                    display_area_model = qu.get_low_exhibition_area_warning(self, display_area_threshold)

                    # 如果有预警数据，显示提醒
                    if stock_warning_model.rowCount() > 0:
                        warning_msg = f"药库库存预警：有{stock_warning_model.rowCount()}种药品库存偏低，请及时补货！"
                        QMessageBox.warning(self, "库存预警", warning_msg, QMessageBox.StandardButton.Ok)
                        break  # 避免重复提示

                    if display_area_model.rowCount() > 0:
                        warning_msg = f"陈列区库存预警：有{display_area_model.rowCount()}种药品库存偏低，请及时补货！"
                        QMessageBox.warning(self, "库存预警", warning_msg, QMessageBox.StandardButton.Ok)
                        break
                except Exception as e:
                    print(f"检查库存预警时出错: {e}")

            # 如果没有任何数据
            if not has_data:
                # 使用默认阈值检查
                try:
                    warning_model = qu.get_low_stock_warning(self, 0)
                    display_area_model = qu.get_low_exhibition_area_warning(self, 0)
                    if warning_model.rowCount() > 0:
                        warning_msg = (f"库存预警：有{warning_model.rowCount()}，"
                                       f"陈列区预警：有{display_area_model.rowCount()} 种药品库存偏低，请及时补货！")
                        QMessageBox.warning(self, "库存预警", warning_msg, QMessageBox.StandardButton.Ok)
                except Exception as e:
                    print(f"检查库存预警时出错: {e}")
