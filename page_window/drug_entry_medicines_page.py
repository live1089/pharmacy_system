from PySide6.QtCore import QDate
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox

from ui_app.drug_entry_ui import Ui_DrugEntryDialog


class DrugEntryPage(QDialog, Ui_DrugEntryDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.load_stock_data()

    def bind_event(self):
        self.drug_entry_save_btn.clicked.connect(self.save)

    def load_stock_data(self):
        self.expiration_date_edit.setDate(QDate.currentDate())
        self.stock_drug_combox.clear()

        query = QSqlQuery("SELECT dic_id, trade_name FROM medicine_dic")
        while query.next():
            drug_stock_id = query.value(0)
            drug_stock_name = query.value(1)
            self.stock_drug_combox.addItem(drug_stock_name, drug_stock_id)

        query = QSqlQuery("SELECT in_id FROM stock_in_main")
        while query.next():
            in_id = query.value(0)
            self.in_id_combox.addItem(str(in_id), in_id)

    def save(self):
        in_id = self.in_id_combox.itemData(self.in_id_combox.currentIndex())
        stock_drug = self.stock_drug_combox.itemData(self.stock_drug_combox.currentIndex())  # 获取药品名称
        expiration_date = self.expiration_date_edit.dateTime().toString("yyyy-MM-dd")  # 获取有效期
        purchase = self.purchase_unit_price_spin_box.value()  # 获取采购单价
        incoming_quantity = self.incoming_quantity_spin_box.value() # 获取入库数量
        actual_quantity = self.actual_incoming_quantity_spin_box.value()


        query = QSqlQuery()
        query.prepare(
            "Insert into stock_in_detail(in_id, medicine_id, purchase_price, dic_id, quantity, actual_quantity)"
            "values (?,?,?,?,?,?)")
        query.addBindValue(in_id)
        query.addBindValue(stock_drug)
        query.addBindValue(purchase)
        query.addBindValue(stock_drug)
        query.addBindValue(incoming_quantity)
        query.addBindValue(actual_quantity)

        if not query.exec():
            QMessageBox.critical(self, "数据库错误", f"添加入库单失败: {query.lastError().text()}")
        else:
            QMessageBox.information(self, "成功", "添加入库单成功")
            self.exec()

        # query = QSqlQuery()
        # query.prepare(
        #     "Insert into inventory_batch(batch_id, medicine_id, in_detail_id, current_quantity)"
        #     "values (?,?,?,?)")
