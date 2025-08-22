from PySide6 import QtCore
from PySide6.QtCore import QDate, QDateTime
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox
import random
from ui_app.stock_out_warehouse_ui import Ui_OutWarehouseMTDialog
from ui_app.stock_out_warehouse_drug_ui import Ui_OutWarehouseDrugDialog


class StockOutPage(QDialog, Ui_OutWarehouseMTDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.out_id = None
        self.load_data()

    def bind_event(self):
        self.out_warehouse_save_btn.clicked.connect(self.save)

    def save(self):
        if self.out_id:
            self.update_stock_out()
        else:
            self.create_stock_out()

    def load_data(self):
        self.stock_out_dateTime.setDateTime(QtCore.QDateTime.currentDateTime())
        # outbound_number = f"ON-{QDate.currentDate().toString('yyyyMMdd')}-{random.randint(1000, 9999)}"
        # self.outbound_number_lineEdit.setText(outbound_number)
        # 生成唯一的出库编号
        while True:
            outbound_number = f"ON-{QDate.currentDate().toString('yyyyMMdd')}-{random.randint(1000, 9999)}"

            # 检查该编号是否已存在
            query = QSqlQuery()
            query.prepare("SELECT COUNT(*) FROM stock_out_main WHERE outbound_number = ?")
            query.addBindValue(outbound_number)
            if query.exec():
                query.first()
                if query.value(0) == 0:  # 编号不存在
                    break

        self.outbound_number_lineEdit.setText(outbound_number)
        # 设置出库类型下拉框，同时设置 itemData
        types = ["销售", "调拨", "报损", "退货", "科室领用"]
        for type_name in types:
            self.stock_out_type_combox.addItem(type_name, type_name)  # 第二个参数是 itemData

        query = QSqlQuery("SELECT users_id, username FROM users")
        while query.next():
            operator_id = query.value(0)
            operator_name = query.value(1)
            self.stock_out_operator_combox.addItem(operator_name, operator_id)

    def load_stock_out_data(self, out_id):
        self.out_warehouse_save_btn.setText("更新入库")
        query = QSqlQuery()
        query.prepare("SELECT outbound_number, out_type, out_date, operator_id, total_amount, remarks "
                      "FROM stock_out_main "
                      "WHERE out_id = ?")
        query.addBindValue(out_id)
        if query.exec():
            query.first()
            outbound_number = query.value(0)
            stock_out_type = query.value(1)
            out_date = query.value(2)
            stock_out_operator = query.value(3)
            total_amount = query.value(4)
            stock_out_remark = query.value(5)

            self.outbound_number_lineEdit.setText(outbound_number)
            self.stock_out_type_combox.setCurrentIndex(self.stock_out_type_combox.findData(stock_out_type))
            self.stock_out_operator_combox.setCurrentIndex(self.stock_out_operator_combox.findData(stock_out_operator))
            datetime_value = QDateTime.currentDateTime()  # 默认值
            if out_date:
                if isinstance(out_date, str):
                    datetime_value = QDateTime.fromString(out_date, "yyyy-MM-dd hh:mm:ss")
                else:
                    datetime_value = out_date
            self.stock_out_dateTime.setDateTime(datetime_value)
            self.stock_out_total_amount_spinBox.setValue(total_amount)
            self.stock_out_remark_plainTextEdit.setPlainText(stock_out_remark)

    def update_stock_out(self):
        if not self.out_id:
            QMessageBox.critical(self, "错误", "无法找到要修改的出库单")
            return
        outbound_number = self.outbound_number_lineEdit.text()
        stock_out_type = self.stock_out_type_combox.itemData(self.stock_out_type_combox.currentIndex())
        stock_out_operator = self.stock_out_operator_combox.itemData(self.stock_out_operator_combox.currentIndex())
        stock_out_date = self.stock_out_dateTime.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        stock_out_total_amount = self.stock_out_total_amount_spinBox.value()
        stock_out_remark = self.stock_out_remark_plainTextEdit.toPlainText()

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        try:
            if not query.exec("BEGIN"):
                raise Exception(f"无法开始事务: {query.lastError().text()}")

            query.prepare(
                "UPDATE stock_out_main "
                "SET outbound_number = ?, out_type = ?, out_date = ?, operator_id = ?, total_amount = ?, remarks = ? "
                "WHERE out_id = ?")
            query.addBindValue(outbound_number)
            query.addBindValue(stock_out_type)
            query.addBindValue(stock_out_date)
            query.addBindValue(stock_out_operator)
            query.addBindValue(stock_out_total_amount)
            query.addBindValue(stock_out_remark)
            if not query.exec():
                raise Exception(f"更新出库单失败: {query.lastError().text()}")
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
        finally:
            # 显式清理资源
            query.finish()

    def create_stock_out(self):
        outbound_number = self.outbound_number_lineEdit.text()
        stock_out_type = self.stock_out_type_combox.currentText()
        stock_out_operator = self.stock_out_operator_combox.itemData(self.stock_out_operator_combox.currentIndex())
        stock_out_date = self.stock_out_dateTime.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        stock_out_total_amount = self.stock_out_total_amount_spinBox.value()
        stock_out_remark = self.stock_out_remark_plainTextEdit.toPlainText()

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            query.prepare(
                "Insert into stock_out_main(outbound_number, out_type, out_date, operator_id, total_amount, remarks) "
                "values (?,?,?,?,?,?)")
            query.addBindValue(outbound_number)
            query.addBindValue(stock_out_type)
            query.addBindValue(stock_out_date)
            query.addBindValue(stock_out_operator)
            query.addBindValue(stock_out_total_amount)
            query.addBindValue(stock_out_remark)
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


class StockOutAddDrugPage(QDialog, Ui_OutWarehouseDrugDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.detail_id = None
        self.load_data()

    def bind_event(self):
        self.buttonBox.accepted.connect(self.accept)

    def load_data(self):
        query = QSqlQuery("SELECT out_id, outbound_number FROM stock_out_main")
        while query.next():
            out_id = query.value(0)
            outbound_number = query.value(1)
            self.stock_out_list_combox.addItem(outbound_number, out_id)

        query = QSqlQuery("SELECT dic_id, trade_name FROM medicine_dic")
        while query.next():
            medicine_id = query.value(0)
            medicine_name = query.value(1)
            self.stock_out_drug_combox.addItem(medicine_name, medicine_id)

    # def stock_out_add_button_clicked(self):
    #     stock_out_list = self.stock_out_list_combox.itemData(self.stock_out_list_combox.currentIndex())
    #     stock_out_drug = self.stock_out_drug_combox.itemData(self.stock_out_drug_combox.currentIndex())
    #     stock_out_number = self.stock_out_number_spinBox.value()
    #
    #     query = QSqlQuery()
    #     if not query.exec("BEGIN"):
    #         QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
    #         return
    #
    #     query = QSqlQuery("SELECT * FROM inventory WHERE inventory_id = ?")
    #
    #     query = QSqlQuery("""
    #             INSERT INTO stock_out_detail(out_id, medicine_id, quantity)
    #             VALUES (?, ?, ?)
    #     """)
    #     query.addBindValue(stock_out_list)
    #     query.addBindValue(stock_out_drug)
    #     query.addBindValue(stock_out_number)
