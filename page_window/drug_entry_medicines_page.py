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
        in_id = self.in_id_combox.itemData(self.in_id_combox.currentIndex())                 # 获取入库单ID
        stock_drug = self.stock_drug_combox.itemData(self.stock_drug_combox.currentIndex())  # 获取药品ID
        expiration_date = self.expiration_date_edit.dateTime().toString("yyyy-MM-dd")        # 获取有效期
        purchase = self.purchase_unit_price_spin_box.value()                                 # 获取采购单价
        incoming_quantity = self.incoming_quantity_spin_box.value()                          # 获取入库数量
        actual_quantity = self.actual_incoming_quantity_spin_box.value()                     # 获取实际入库数量

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            # 插入入库明细数据
            query.prepare(
                "INSERT INTO stock_in_detail(in_id, medicine_id, dic_id, quantity, actual_quantity) "
                "VALUES (?,?,?,?,?)")
            query.addBindValue(in_id)
            query.addBindValue(stock_drug)
            query.addBindValue(purchase)
            query.addBindValue(stock_drug)
            query.addBindValue(incoming_quantity)
            query.addBindValue(actual_quantity)

            if not query.exec():
                raise Exception(f"添加入库明细失败: {query.lastError().text()}")

            # 获取刚刚插入的明细ID
            query.exec("SELECT last_insert_rowid()")
            if query.next():
                detail_id = query.value(0)
            else:
                raise Exception("无法获取插入的明细ID")

            # 插入库存批次数据
            query.prepare(
                "INSERT INTO inventory_batch(batch_number, buy_detail_id, in_detail_id, medicine_id, expiry_date, inventory_id, location, created_at, last_updated) "
                "VALUES (?,?,?,?,?,?,?,?,?)")
            # 这里需要生成或获取批号，暂时使用简单方式生成
            batch_number = f"BN{QDate.currentDate().toString('yyyyMMdd')}{detail_id}"
            query.addBindValue(batch_number)
            query.addBindValue(detail_id)
            query.addBindValue(stock_drug)
            query.addBindValue(expiration_date)
            query.addBindValue(actual_quantity)

            if not query.exec():
                raise Exception(f"添加库存批次失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "添加入库单和库存批次成功")
            self.accept()  # 关闭对话框

        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
