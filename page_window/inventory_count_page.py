from PySide6 import QtCore

from ui_app.inventory_count_entry_ui import Ui_InventoryCountDialog
from PySide6.QtCore import QDate, QDateTime
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox


class InventoryCountPage(QDialog, Ui_InventoryCountDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.check_id = None
        self.load_data()
        # self.inventory_count_drug_comboBox.currentIndexChanged.connect(self.update_actual_quantity)

    def bind_event(self):
        self.inventory_count_save_btn.clicked.connect(self.save)

    def load_data(self):
        self.inventory_count_dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # 加载药品数据
        query = QSqlQuery("SELECT dic_id, trade_name FROM medicine_dic")
        while query.next():
            drug_id = query.value(0)
            drug_name = query.value(1)
            self.inventory_count_drug_comboBox.addItem(drug_name, drug_id)

        # 加载用户数据
        query = QSqlQuery("SELECT users_id, username FROM users")
        while query.next():
            operator_id = query.value(0)
            operator_name = query.value(1)
            self.inventory_count_user_comboBox.addItem(operator_name, operator_id)

        # 加载库存批次数据（修复：应该添加到批次下拉框）
        query = QSqlQuery("SELECT in_id, batch FROM stock_in_main")
        while query.next():
            batch_id = query.value(0)
            batch_name = query.value(1)
            self.inventory_count_batch_combox.addItem(batch_name, batch_id)

        # 加载货位数据
        query = QSqlQuery("SELECT warehouse_shelf_id, location FROM warehouse_shelf_position")
        while query.next():
            shelf_id = query.value(0)
            shelf_name = query.value(1)
            self.inventory_count_location_combox.addItem(shelf_name, shelf_id)

        # 连接批次选择变化信号
        self.inventory_count_batch_combox.currentIndexChanged.connect(self.update_drug_info_from_batch)

    def update_drug_info_from_batch(self, index):
        """
        当选择库存批次时，自动更新对应的药品信息和库存数量
        """
        if index < 0:
            return

        batch_id = self.inventory_count_batch_combox.itemData(index)
        if batch_id is None:
            return

        # 查询该批次对应的药品信息和库存数量
        query = QSqlQuery()
        query.prepare("""
            SELECT 
                pd.medicine_id,
                md.trade_name,
                COALESCE(s.quantity, 0) as stock_quantity
            FROM stock_in_main sm
            LEFT JOIN stock_in_detail sd ON sm.in_id = sd.in_id
            LEFT JOIN purchase_detail pd ON sd.purchase_detail_id = pd.detail_id
            LEFT JOIN medicine_dic md ON pd.medicine_id = md.dic_id
            LEFT JOIN stock s ON s.batch = sm.in_id
            WHERE sm.in_id = ?
            LIMIT 1
        """)
        query.addBindValue(batch_id)

        if query.exec() and query.next():
            medicine_id = query.value(0)
            medicine_name = query.value(1)
            stock_quantity = query.value(2)

            # 更新药品下拉框选择
            drug_index = self.inventory_count_drug_comboBox.findData(medicine_id)
            if drug_index >= 0:
                self.inventory_count_drug_comboBox.setCurrentIndex(drug_index)

            # 更新库存数量显示
            self.actual_quantity_lab.setText(str(stock_quantity))

            # 同时更新盘点数量为当前库存数量（可选）
            self.inventory_count_number_suspinBox.setValue(int(stock_quantity))


    def save(self):
        if self.check_id:
            self.update_check_out()
        else:
            self.create_check_out()

    def load_check_out_data(self, check_id):
        self.check_id = check_id
        self.inventory_count_save_btn.setText("更新入库")
        query = QSqlQuery()
        query.prepare(" SELECT medicine_id, inventory_of_batches, inventory_of_location, recorded_quantity, actual_quantity, check_date, inventory_check.user_id, discrepancy_reason "
                      " FROM inventory_check "
                      " WHERE check_id = ? ")
        query.addBindValue(check_id)
        if query.exec():
            query.first()
            medicine = query.value(0)  # 药品
            inventory_of_batches = query.value(1)
            inventory_of_location = query.value(2)
            recorded_quantity = query.value(3)  # 数量
            actual_quantity = query.value(4)  # 库存数量
            check_date = query.value(5)  # 盘点日期
            user_id = query.value(6)
            discrepancy_reason = query.value(7)  # 不一致原因

            self.inventory_count_drug_comboBox.setCurrentIndex(self.inventory_count_drug_comboBox.findData(medicine))
            self.inventory_count_batch_combox.setCurrentIndex(self.inventory_count_batch_combox.findData(inventory_of_batches))
            self.inventory_count_location_combox.setCurrentIndex(self.inventory_count_location_combox.findData(inventory_of_location))
            self.inventory_count_number_suspinBox.setValue(recorded_quantity)
            self.actual_quantity_lab.setText(actual_quantity)
            datetime_value = QDateTime.currentDateTime()  # 默认值
            if check_date:
                if isinstance(check_date, str):
                    datetime_value = QDateTime.fromString(check_date, "yyyy-MM-dd hh:mm:ss")
                else:
                    datetime_value = check_date
            self.inventory_count_dateTimeEdit.setDateTime(datetime_value)
            self.inventory_count_user_comboBox.setCurrentIndex(self.inventory_count_user_comboBox.findData(user_id))
            self.inventory_count_plainTextEdit.setPlainText(discrepancy_reason)

    def update_check_out(self):
        if not self.check_id:
            QMessageBox.critical(self, "错误", "无法找到要修改的出库单")
            return
        inventory_count_drug = self.inventory_count_drug_comboBox.itemData(
            self.inventory_count_drug_comboBox.currentIndex())
        inventory_of_batches = self.inventory_count_batch_combox.itemData(
            self.inventory_count_batch_combox.currentIndex())
        inventory_of_location = self.inventory_count_location_combox.itemData(
            self.inventory_count_location_combox.currentIndex()
        )
        actual_quantity = self.actual_quantity_lab.text()
        recorded_quantity = self.inventory_count_number_suspinBox.value()
        inventory_count = self.inventory_count_dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        user_id = self.inventory_count_user_comboBox.itemData(self.inventory_count_user_comboBox.currentIndex())
        discrepancy_reason = self.inventory_count_plainTextEdit.toPlainText()

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        try:
            if not query.exec("BEGIN"):
                raise Exception(f"无法开始事务: {query.lastError().text()}")

            query.prepare(
                "UPDATE inventory_check "
                "SET medicine_id=?, inventory_of_batches=?, inventory_of_location=?, recorded_quantity=?, actual_quantity=?, check_date=?, user_id=?, discrepancy_reason=? "
                "WHERE check_id = ?")
            query.addBindValue(inventory_count_drug)
            query.addBindValue(inventory_of_batches)
            query.addBindValue(inventory_of_location)
            query.addBindValue(recorded_quantity)
            query.addBindValue(actual_quantity)
            query.addBindValue(inventory_count)
            query.addBindValue(user_id)
            query.addBindValue(discrepancy_reason)
            if not query.exec():
                raise Exception(f"更新出库单失败: {query.lastError().text()}")
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
        finally:
            # 显式清理资源
            query.finish()

    def create_check_out(self):
        inventory_count_drug = self.inventory_count_drug_comboBox.itemData(
            self.inventory_count_drug_comboBox.currentIndex())
        inventory_of_batches = self.inventory_count_batch_combox.itemData(
            self.inventory_count_batch_combox.currentIndex())
        inventory_of_location = self.inventory_count_location_combox.itemData(
            self.inventory_count_location_combox.currentIndex()
        )
        actual_quantity = self.actual_quantity_lab.text()
        recorded_quantity = self.inventory_count_number_suspinBox.value()
        inventory_count = self.inventory_count_dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        user_id = self.inventory_count_user_comboBox.itemData(self.inventory_count_user_comboBox.currentIndex())
        discrepancy_reason = self.inventory_count_plainTextEdit.toPlainText()

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            query.prepare(
                "Insert into inventory_check(medicine_id, inventory_of_batches, inventory_of_location, recorded_quantity, actual_quantity, check_date, user_id, discrepancy_reason) "
                "values (?,?,?,?,?,?,?,?)")
            query.addBindValue(inventory_count_drug)
            query.addBindValue(inventory_of_batches)
            query.addBindValue(inventory_of_location)
            query.addBindValue(recorded_quantity)
            query.addBindValue(actual_quantity)
            query.addBindValue(inventory_count)
            query.addBindValue(user_id)
            query.addBindValue(discrepancy_reason)
            if not query.exec():  # 执行INSERT语句
                raise Exception(f"插入数据失败: {query.lastError().text()}")

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
