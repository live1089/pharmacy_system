import random
from datetime import datetime

from PySide6.QtCore import QDateTime, QDate
from PySide6.QtSql import QSqlQuery

from data.sqlite_data import get_sales_lists_model, get_sales_model
from page_window.tools import install_enter_key_filter
from ui_app.sell_drug_ui import Ui_SellDialog
from ui_app.sell_list_ui import Ui_SellListDialog
from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit, QDialogButtonBox, QVBoxLayout


# 销售单列表
class SellListDialog(QDialog, Ui_SellListDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.load_data()
        self.ignore_cargo_return()

    def ignore_cargo_return(self):
        install_enter_key_filter(self.sell_list_lineEdit)
        install_enter_key_filter(self.sell_user_comboBox)
        install_enter_key_filter(self.sell_dateTimeEdit)

    def bind_event(self):
        self.sell_list_save_btn.clicked.connect(self.save)

    def save(self):
        self.create_sell_list()

    def load_data(self):
        self.sell_dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        query = QSqlQuery("SELECT users_id, username FROM users")
        while query.next():
            users_id = query.value(0)
            username = query.value(1)
            self.sell_user_comboBox.addItem(username, users_id)
        # 获取当前日期和时间
        now = datetime.now()

        # 格式化日期和时间部分
        date_part = now.strftime("%Y-%m-%d")
        # time_part = now.strftime("%H:%M:%S")

        # 流水号（这里用固定值模拟）
        sequence_number = random.randint(1000, 9999)

        # 拼接成最终的业务编号
        # sell_list = f"SELL-BH-{date_part}-{time_part}-{sequence_number}"
        sell_list = f"SELL-BH-{date_part}-{sequence_number}"
        self.sell_list_lineEdit.setText(sell_list)

    def create_sell_list(self):
        sell_list = self.sell_list_lineEdit.text()
        sell_user = self.sell_user_comboBox.itemData(self.sell_user_comboBox.currentIndex())
        sell_date = self.sell_dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return
        try:
            query.prepare(
                "INSERT INTO sales(sale_no, cashier_id, sale_date) "
                "VALUES (?,?,?)")
            query.addBindValue(sell_list)
            query.addBindValue(sell_user)
            query.addBindValue(sell_date)

            if not query.exec():
                raise Exception(f"添加失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "添加成功")
            self.accept()  # 关闭对话框
            # get_sales_lists_model(self)
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))


# 销售药品
class SellDrugUiDialog(QDialog, Ui_SellDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.detail_id = None
        self.load_data()
        self.ignore_cargo_return()

    def ignore_cargo_return(self):
        install_enter_key_filter(self.sell_list_combox)
        install_enter_key_filter(self.sell_drug_combox)
        install_enter_key_filter(self.number_spinBox)
        install_enter_key_filter(self.price_doubleSpinBox)
        install_enter_key_filter(self.lump_sum_doubleSpinBox)

    def bind_event(self):
        self.sell_sure_btn.clicked.connect(self.save)
        self.sell_drug_combox.currentIndexChanged.connect(self.load_price_data)
        self.number_spinBox.valueChanged.connect(self.load_total_amount)

    def load_price_data(self, index):
        query = QSqlQuery(f"SELECT price FROM medicine_dic WHERE dic_id = {self.sell_drug_combox.itemData(index)}")
        if query.next():
            price = query.value(0)
            self.price_doubleSpinBox.setValue(price)

    def load_total_amount(self):
        price = self.price_doubleSpinBox.value()
        number = self.number_spinBox.value()
        self.lump_sum_doubleSpinBox.setValue(price * number)
    def save(self):
        if self.detail_id:
            self.update_sell_drug()
        else:
            self.create_sell_drug()

    def load_data(self):
        query = QSqlQuery("SELECT dic_id, trade_name FROM medicine_dic")
        while query.next():
            drug_id = query.value(0)
            drug_name = query.value(1)
            self.sell_drug_combox.addItem(drug_name, drug_id)
        query = QSqlQuery("SELECT sales_id, sale_no FROM sales ORDER BY sales_id DESC")
        while query.next():
            sales_id = query.value(0)
            sale_no = query.value(1)
            self.sell_list_combox.addItem(sale_no, sales_id)

    def create_sell_drug(self):
        sell_list = self.sell_list_combox.itemData(self.sell_list_combox.currentIndex())
        drug_id = self.sell_drug_combox.itemData(self.sell_drug_combox.currentIndex())
        number = self.number_spinBox.value()
        price = self.price_doubleSpinBox.value()
        lump_sum = self.lump_sum_doubleSpinBox.value()
        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return
        try:
            query.prepare(
                "INSERT INTO sale_details(sales_id, medicine_id, quantity, price, total_amount) "
                "VALUES (?,?,?,?,?)")
            query.addBindValue(sell_list)
            query.addBindValue(drug_id)
            query.addBindValue(number)
            query.addBindValue(price)
            query.addBindValue(lump_sum)
            if not query.exec():
                raise Exception(f"添加失败: {query.lastError().text()}")
            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "添加成功")
            self.accept()  # 关闭对话框
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))

    def show_mod_sell_data(self, detail_id):
        self.detail_id = detail_id
        self.sell_sure_btn.setText("更新药品")
        detail_query = QSqlQuery()
        detail_query.prepare("""
                SELECT sales_id, medicine_id, quantity, price, total_amount 
                FROM sale_details 
                WHERE detail_id = ?
        """)
        detail_query.addBindValue(detail_id)
        if detail_query.exec() and detail_query.next():
            sell_list = detail_query.value(0)
            drug_id = detail_query.value(1)
            number = detail_query.value(2)
            price = detail_query.value(3)
            lump_sum = detail_query.value(4)

            self.sell_list_combox.setCurrentIndex(self.sell_list_combox.findData(sell_list))
            self.sell_drug_combox.setCurrentIndex(self.sell_drug_combox.findData(drug_id))
            self.number_spinBox.setValue(number)
            self.price_doubleSpinBox.setValue(price)
            self.lump_sum_doubleSpinBox.setValue(lump_sum)

    def update_sell_drug(self):
        sell_list = self.sell_list_combox.itemData(self.sell_list_combox.currentIndex())
        drug_id = self.sell_drug_combox.itemData(self.sell_drug_combox.currentIndex())
        number = self.number_spinBox.value()
        price = self.price_doubleSpinBox.value()
        lump_sum = self.lump_sum_doubleSpinBox.value()

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            query.prepare(
                "UPDATE sale_details "
                "SET  sales_id=?, medicine_id=?, quantity=?, price=?, total_amount=?"
                "WHERE sale_details.detail_id=?")

            query.addBindValue(sell_list)
            query.addBindValue(drug_id)
            query.addBindValue(number)
            query.addBindValue(price)
            query.addBindValue(lump_sum)
            query.addBindValue(self.detail_id)

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