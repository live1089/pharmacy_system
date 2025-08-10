from PySide6.QtCore import QDateTime, QDate
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox

from ui_app.stock_page_ui import Ui_StockDialog


class StockMedicinesPage(QDialog, Ui_StockDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.load_stock_data()

    def bind_event(self):
        self.stock_save_btn.clicked.connect(self.save)

    def save(self):
        batch = self.batch_spin_box.value()  # 获取批号
        inbound_amount = self.inbound_amount_spin_box.value()  # 获取入库金额
        inbound_date = self.inbound_date_time_edit.dateTime().toString("yyyy-MM-dd hh:mm:ss")  # 获取入库时间
        operator = self.operator_combox.itemData(self.operator_combox.currentIndex())  # 获取操作员
        purchase_order = self.purchase_order_combox.itemData(self.purchase_order_combox.currentIndex())  # 获取采购订单
        invoice = self.Invoice_line_edit.text()  # 获取发票号
        remarks = self.warehousing_remarks_plain_text_edit.toPlainText()  # 入库备注
        supplier = self.supplier_stock_combox.itemData(self.supplier_stock_combox.currentIndex())

        query = QSqlQuery()
        query.prepare(
            "Insert into stock_in_main(order_id, supplier_id, in_date, operator_id, total_amount, invoice_number, remarks) "
            "values (?,?,?,?,?,?,?)")
        query.addBindValue(purchase_order)
        query.addBindValue(supplier)
        query.addBindValue(inbound_date)
        query.addBindValue(operator)
        query.addBindValue(inbound_amount)
        query.addBindValue(invoice)
        query.addBindValue(remarks)
        if not query.exec():
            QMessageBox.critical(self, "数据库错误", f"添加入库单失败: {query.lastError().text()}")
        else:
            QMessageBox.information(self, "成功", "添加入库单成功")
            self.exec()

    def load_stock_data(self):
        self.inbound_date_time_edit.setDateTime(QDateTime.currentDateTime())
        query = QSqlQuery("SELECT supplier_id, name FROM supplier")
        while query.next():
            supplier_id = query.value(0)
            supplier_name = query.value(1)
            self.supplier_stock_combox.addItem(supplier_name, supplier_id)

        query = QSqlQuery("SELECT order_id, order_date FROM purchase_order")
        while query.next():
            order_id = query.value(0)
            order_number = query.value(1)
            self.purchase_order_combox.addItem(order_number, order_id)

        query = QSqlQuery("SELECT users_id, username FROM users")
        while query.next():
            operator_id = query.value(0)
            operator_name = query.value(1)
            self.operator_combox.addItem(operator_name, operator_id)
