"""
Author: live1089 a5u3580@163.com
Date: 2025-06-11 17:10:47
LastEditors: live1089 a5u3580@163.com
LastEditTime: 2025-06-11 17:18:55
FilePath: \\Pharmacy_drug_management_system\\main.py
"""
from enum import Enum

# 主题
import qdarkstyle
from qtmodern.styles import dark, light

# 外部UI
import ui_app.log_in_ui
import ui_app.mainwondows_ui
# 导入pyside6库
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog,
                               QLabel, QLineEdit, QPushButton,
                               QVBoxLayout, QMessageBox, QTableView)
from PySide6.QtCore import QCoreApplication, Qt, QByteArray, Signal
from PySide6.QtGui import QIcon, QPixmap

# 数据库
import data.sqlite_data
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
# 其他工具
import base64


# from icon_data import icon_data  # 导入生成的图标数据
class PageMap(Enum):
    drug_selection_tableView = 0     # 药品
    supplier_tableView = 1           # 供应商
    stock_in_tabWidget = 2           # 入库
    inventory_tableView = 3          # 库存
    sales_records_tableView = 4      # 销售
    expiring_drugs_tableView = 5     # 临期
    stock_out_tabWidget = 6          # 出库
    order_tabWidget = 7              # 采购订单
    recently_added_tableView = 8     # 最近添加
    inventory_check_tableView = 9    # 库存盘点
    customers_tableView = 10         # 会员客户
    user_tableWidget = 11            # 本地用户



class MainWindow(QMainWindow, ui_app.mainwondows_ui.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind_event()
        self.db = data.sqlite_data.DatabaseInit()
        data.sqlite_data.get_medicines_model(self)
        data.sqlite_data.get_sales_model(self)
        data.sqlite_data.get_expiring_medicine_model(self)
        data.sqlite_data.get_supplier_model(self)
        data.sqlite_data.get_inventory_model(self)
        data.sqlite_data.get_stock_in_main_model(self)
        data.sqlite_data.get_stock_in_detail_model(self)
        data.sqlite_data.get_inventory_datch_model(self)
        data.sqlite_data.get_stock_out_main_model(self)
        data.sqlite_data.get_stock_out_detail_model(self)
        data.sqlite_data.get_purchase_order_model(self)
        data.sqlite_data.get_purchase_order_detail_model(self)
        data.sqlite_data.get_inventory_check(self)
        self.stock_in_tabWidget.currentChanged.connect(self.tab_changed)

        # # 创建模型并设置表名
        # self.model = QSqlTableModel(self, self.db)
        # self.model.setTable("medicines")
        # self.model.select()
        # # 将模型设置到表格视图
        # self.drug_selection_tableView.setModel(self.model)

    # def page_switch(self, page_name):
    #     self.medicine.clicked.connect(lambda: self.show_page_by_name(page_name))
    def tab_changed(self, index):
        """标签切换时触发"""
        print(f"已切换到标签页: {index} ({self.stock_in_tabWidget.tabText(index)})")
    def bind_event(self):
        self.medicine.clicked.connect(lambda: self.show_page_by_name(PageMap.drug_selection_tableView.value))
        self.sales_records.clicked.connect(lambda: self.show_page_by_name(PageMap.sales_records_tableView.value))
        self.expiring_medicine.clicked.connect(lambda: self.show_page_by_name(PageMap.expiring_drugs_tableView.value))
        self.pharmacy_operation_record.clicked.connect(lambda: self.show_page_by_name(PageMap.inventory_tableView.value))
        self.supplier.clicked.connect(lambda: self.show_page_by_name(PageMap.supplier_tableView.value))
        self.drug_inbound.clicked.connect(lambda: self.show_page_by_name(PageMap.stock_in_tabWidget.value))
        self.drug_outbound.clicked.connect(lambda: self.show_page_by_name(PageMap.stock_out_tabWidget.value))
        self.recently_added.clicked.connect(lambda: self.show_page_by_name(PageMap.recently_added_tableView.value))
        self.medicine_purchase.clicked.connect(lambda: self.show_page_by_name(PageMap.order_tabWidget.value))
        self.inventory_record.clicked.connect(lambda: self.show_page_by_name(PageMap.inventory_check_tableView.value))
        self.member_customer.clicked.connect(lambda: self.show_page_by_name(PageMap.customers_tableView.value))
        self.user_information.clicked.connect(lambda: self.show_page_by_name(PageMap.user_tableWidget.value))

    def show_page_by_name(self, page_name):
        """通过页面名称切换页面"""
        if page_name in PageMap:
            # 切换到目标页面
            self.stackedWidget.setCurrentIndex(page_name)

            # 这里可以添加页面切换时的额外逻辑
            print(f"已切换到页面: {page_name}")
        else:
            print(f"错误: 找不到页面 '{page_name}'")


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
        if account == "" and password == "":
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
