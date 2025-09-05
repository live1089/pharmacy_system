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
        self.inventory_count_drug_comboBox.currentIndexChanged.connect(self.update_actual_quantity)

    def update_actual_quantity(self, index):
        """
        当药品下拉框选择发生变化时，更新实际库存数量显示
        """
        # 获取选中的药品ID
        medicine_id = self.inventory_count_drug_comboBox.itemData(index)

        if medicine_id is not None:
            # 查询该药品的实际库存数量
            query = QSqlQuery()
            query.prepare("""
                SELECT COALESCE(SUM(quantity), 0) 
                FROM stock 
                WHERE drug_id = ?
            """)
            query.addBindValue(medicine_id)

            if query.exec() and query.next():
                actual_quantity = query.value(0)
                # 更新标签显示
                self.actual_quantity_lab.setText(str(actual_quantity))
            else:
                # 如果查询失败，显示0或错误信息
                self.actual_quantity_lab.setText("0")
        else:
            # 如果没有选中有效项，显示默认值
            self.actual_quantity_lab.setText("0")

    def bind_event(self):
        self.inventory_count_save_btn.clicked.connect(self.save)

    def load_data(self):
        self.inventory_count_dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        query = QSqlQuery("SELECT dic_id, trade_name FROM medicine_dic")
        while query.next():
            drug_id = query.value(0)
            drug_name = query.value(1)
            self.inventory_count_drug_comboBox.addItem(drug_name, drug_id)

        query = QSqlQuery("SELECT users_id, username FROM users")
        while query.next():
            operator_id = query.value(0)
            operator_name = query.value(1)
            self.inventory_count_user_comboBox.addItem(operator_name, operator_id)

        query = QSqlQuery("SELECT in_id, batch FROM stock_in_main")
        while query.next():
            drug_id = query.value(0)
            drug_name = query.value(1)
            self.inventory_count_drug_comboBox.addItem(drug_name, drug_id)

        query = QSqlQuery("SELECT warehouse_shelf_id, location FROM warehouse_shelf_position")
        while query.next():
            shelf_id = query.value(0)
            shelf_name = query.value(1)
            self.inventory_count_location_combox.addItem(shelf_name, shelf_id)

    def save(self):
        if self.check_id:
            self.update_check_out()
        else:
            self.create_check_out()

    def load_check_out_data(self, check_id):
        self.check_id = check_id
        self.inventory_count_save_btn.setText("更新入库")
        query = QSqlQuery()
        query.prepare(" SELECT medicine_id, recorded_quantity, actual_quantity, check_date, discrepancy_reason "
                      " FROM inventory_check "
                      " WHERE check_id = ? ")
        query.addBindValue(check_id)
        if query.exec():
            query.first()
            medicine = query.value(0)  # 药品
            recorded_quantity = query.value(1)  # 数量
            actual_quantity = query.value(2)  # 实际数量
            check_date = query.value(3)  # 盘点日期
            discrepancy_reason = query.value(4)  # 不一致原因

            self.inventory_count_drug_comboBox.setCurrentIndex(self.inventory_count_drug_comboBox.findData(medicine))
            self.inventory_count_number_suspinBox.setValue(recorded_quantity)
            self.actual_quantity_lab.setText(actual_quantity)
            datetime_value = QDateTime.currentDateTime()  # 默认值
            if check_date:
                if isinstance(check_date, str):
                    datetime_value = QDateTime.fromString(check_date, "yyyy-MM-dd hh:mm:ss")
                else:
                    datetime_value = check_date
            self.inventory_count_dateTimeEdit.setDateTime(datetime_value)
            self.inventory_count_plainTextEdit.setPlainText(discrepancy_reason)

    def update_check_out(self):
        if not self.check_id:
            QMessageBox.critical(self, "错误", "无法找到要修改的出库单")
            return
        inventory_count_drug = self.inventory_count_drug_comboBox.itemData(
            self.inventory_count_user_comboBox.currentIndex())
        actual_quantity = self.actual_quantity_lab.text()
        inventory_count_number = self.inventory_count_number_suspinBox.value()
        inventory_count = self.inventory_count_dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        inventory_count_remark = self.inventory_count_plainTextEdit.toPlainText()

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        try:
            if not query.exec("BEGIN"):
                raise Exception(f"无法开始事务: {query.lastError().text()}")

            query.prepare(
                "UPDATE inventory_check "
                "SET medicine_id=?, recorded_quantity=?, actual_quantity=?, check_date=?, discrepancy_reason=? "
                "WHERE check_id = ?")
            query.addBindValue(inventory_count_drug)
            query.addBindValue(inventory_count_number)
            query.addBindValue(actual_quantity)
            query.addBindValue(inventory_count)
            query.addBindValue(inventory_count_remark)
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
            self.inventory_count_user_comboBox.currentIndex())
        actual_quantity = self.actual_quantity_lab.text()
        inventory_count_number = self.inventory_count_number_suspinBox.value()
        inventory_count = self.inventory_count_dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        inventory_count_remark = self.inventory_count_plainTextEdit.toPlainText()

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            query.prepare(
                "Insert into inventory_check(medicine_id, recorded_quantity, actual_quantity, check_date, discrepancy_reason) "
                "values (?,?,?,?,?)")
            query.addBindValue(inventory_count_drug)
            query.addBindValue(inventory_count_number)
            query.addBindValue(actual_quantity)
            query.addBindValue(inventory_count)
            query.addBindValue(inventory_count_remark)
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
