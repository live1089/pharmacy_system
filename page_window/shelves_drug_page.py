from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox

from page_window.tools import install_enter_key_filter
from ui_app.shelves_drug_ui import Ui_ShelvesDialog


class ShelvesDrugPage(QDialog, Ui_ShelvesDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_events()  # 修改为 bind_events
        self.shelves_id = None
        self.load_data()
        self.ignore_cargo_return()

    def ignore_cargo_return(self):
        install_enter_key_filter(self.stock_out_list_combox)
        install_enter_key_filter(self.stock_out_batch_combox)
        install_enter_key_filter(self.shelves_drug_combox)
        install_enter_key_filter(self.shelves_number_spinBox)
        install_enter_key_filter(self.shelves_location_combox)

    def bind_events(self):  # 修改方法名
        """绑定所有事件"""
        self.shelves_add_save_btn.clicked.connect(self.save)
        # 添加上架药品出库单选择变化事件
        self.stock_out_list_combox.currentIndexChanged.connect(self.on_outbound_changed)
        # 添加出库批次选择变化事件
        self.stock_out_batch_combox.currentIndexChanged.connect(self.on_batch_changed)

    def on_outbound_changed(self, index):
        """当出库单选择变化时，更新药品列表和批次列表"""
        if index >= 0:
            out_id = self.stock_out_list_combox.itemData(index)
            self.load_drugs_by_outbound(out_id)
            self.load_batches_by_outbound(out_id)

    def on_batch_changed(self, index):
        """当出库批次选择变化时，自动加载对应的药品信息"""
        if index >= 0:
            detail_id = self.stock_out_batch_combox.itemData(index)
            self.load_drug_by_batch(detail_id)

    def load_drugs_by_outbound(self, out_id):
        """根据出库单ID加载对应的药品"""
        # 清空当前药品列表
        self.shelves_drug_combox.clear()

        # 查询该出库单对应的药品
        query = QSqlQuery()
        query.prepare("""
            SELECT DISTINCT md.dic_id, md.trade_name
            FROM stock_out_detail sod
            JOIN medicine_dic md ON sod.medicine_id = md.dic_id
            WHERE sod.out_id = ?
        """)
        query.addBindValue(out_id)

        if query.exec():
            while query.next():
                dic_id = query.value(0)
                trade_name = query.value(1)
                self.shelves_drug_combox.addItem(trade_name, dic_id)
        else:
            print(f"查询药品失败: {query.lastError().text()}")

    def load_batches_by_outbound(self, out_id):
        """根据出库单ID加载对应的出库批次"""
        # 清空当前批次列表
        self.stock_out_batch_combox.clear()
        self.shelves_number_spinBox.clear()

        # 查询该出库单对应的批次
        query = QSqlQuery()
        query.prepare("""
            SELECT detail_id, out_batch 
            FROM stock_out_detail 
            WHERE out_id = ?
        """)
        query.addBindValue(out_id)

        if query.exec():
            while query.next():
                detail_id = query.value(0)
                out_batch = query.value(1)
                self.stock_out_batch_combox.addItem(out_batch, detail_id)
        else:
            print(f"查询批次失败: {query.lastError().text()}")

    def load_drug_by_batch(self, detail_id):
        """根据出库批次ID加载对应的药品信息和数量"""
        if detail_id is not None:
            # 查询该批次对应的药品信息
            query = QSqlQuery()
            query.prepare("""
                SELECT md.dic_id, md.trade_name, sod.quantity
                FROM stock_out_detail sod
                JOIN medicine_dic md ON sod.medicine_id = md.dic_id
                WHERE sod.detail_id = ?
            """)
            query.addBindValue(detail_id)

            if query.exec() and query.next():
                medicine_id = query.value(0)
                medicine_name = query.value(1)
                quantity = query.value(2)

                # 设置药品下拉框
                index = self.shelves_drug_combox.findData(medicine_id)
                if index >= 0:
                    self.shelves_drug_combox.setCurrentIndex(index)

                # 设置数量
                self.shelves_number_spinBox.setValue(quantity or 0)
            else:
                print(f"查询批次对应的药品信息失败: {query.lastError().text()}")

    def load_data(self):
        """加载初始数据"""
        # 加载出库单列表（上架类型）
        query = QSqlQuery("SELECT out_id, outbound_number FROM stock_out_main WHERE out_type = '上架'")
        while query.next():
            out_id = query.value(0)
            outbound_number = query.value(1)
            self.stock_out_list_combox.addItem(outbound_number, out_id)

        # 加载货位信息
        query = QSqlQuery("SELECT warehouse_shelf_id, location FROM warehouse_shelf_position")
        while query.next():
            shelf_id = query.value(0)
            shelf_name = query.value(1)
            self.shelves_location_combox.addItem(shelf_name, shelf_id)

    def save(self):
        if self.shelves_id:
            self.update_stock_shelves()
        else:
            self.create_stock_shelves()

    def create_stock_shelves(self):
        stock_out_list = self.stock_out_list_combox.itemData(self.stock_out_list_combox.currentIndex())
        stock_out_batch = self.stock_out_batch_combox.itemData(self.stock_out_batch_combox.currentIndex())
        shelves_drug = self.shelves_drug_combox.itemData(self.shelves_drug_combox.currentIndex())
        shelves_number = self.shelves_number_spinBox.value()
        shelves_location = self.shelves_location_combox.itemData(self.shelves_location_combox.currentIndex())

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            query.prepare(
                "Insert into shelves_drug(outbound_number, out_batch, drug, shelves_number, location_id) "
                "values (?,?,?,?,?)")
            query.addBindValue(stock_out_list)
            query.addBindValue(stock_out_batch)
            query.addBindValue(shelves_drug)
            query.addBindValue(shelves_number)
            query.addBindValue(shelves_location)
            if not query.exec():
                raise Exception(f"添加上架药品失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "添加成功")
            self.accept()  # 关闭对话框
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
        finally:
            query.finish()

    def update_load_data(self, shelves_id):
        self.stock_in_id = shelves_id
        self.shelves_add_save_btn.setText("更新")
        query = QSqlQuery()
        query.prepare("SELECT outbound_number, out_batch, drug, shelves_number, location_id "
                      "FROM shelves_drug "
                      "WHERE shelves_drug.shelves_id = ?")
        query.addBindValue(shelves_id)
        while query.next():
            query.first()
            outbound_number = query.value(0)
            out_batch = query.value(1)
            drug = query.value(2)
            shelves_number = query.value(3)
            location_id = query.value(4)

            self.stock_out_list_combox.setCurrentIndex(self.stock_out_list_combox.findData(outbound_number))
            self.stock_out_batch_combox.setCurrentIndex(self.stock_out_batch_combox.findData(out_batch))
            self.shelves_drug_combox.setCurrentIndex(self.shelves_drug_combox.findData(drug))
            self.shelves_number_spinBox.setValue(shelves_number)
            self.shelves_location_combox.setCurrentIndex(self.shelves_location_combox.findData(location_id))

    def update_stock_shelves(self):
        stock_out_list = self.stock_out_list_combox.itemData(self.stock_out_list_combox.currentIndex())
        stock_out_batch = self.stock_out_batch_combox.itemData(self.stock_out_batch_combox.currentIndex())
        shelves_drug = self.shelves_drug_combox.itemData(self.shelves_drug_combox.currentIndex())
        shelves_number = self.shelves_number_spinBox.value()
        shelves_location = self.shelves_location_combox.itemData(self.shelves_location_combox.currentIndex())

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        try:
            if not query.exec("BEGIN"):
                raise Exception(f"无法开始事务: {query.lastError().text()}")

            # 更新主表
            query.prepare("""
                UPDATE shelves_drug
                SET outbound_number=?, out_batch=?, drug=?, shelves_number=?, location_id=?
                WHERE shelves_id = ?
            """)
            query.addBindValue(stock_out_list)
            query.addBindValue(stock_out_batch)
            query.addBindValue(shelves_drug)
            query.addBindValue(shelves_number)
            query.addBindValue(shelves_location)
            query.addBindValue(self.shelves_id)

            if not query.exec():
                raise Exception(f"更新失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "更新成功")
            self.accept()  # 关闭对话框
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
        finally:
            # 显式清理资源
            query.finish()
