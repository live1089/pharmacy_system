"""
Author: live1089 a5u3580@163.com
Date: 2025-06-11 17:10:47
LastEditors: live1089 a5u3580@163.com
LastEditTime: 2025-06-11 17:18:55
FilePath: \\Pharmacy_drug_management_system\\main.py
"""

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


class MainWindow(QMainWindow, ui_app.mainwondows_ui.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind_event()
        self.db = data.sqlite_data.DatabaseInit()
        data.sqlite_data.get_medicines_model(self)
        data.sqlite_data.get_supplier_model(self)

        # # 创建模型并设置表名
        # self.model = QSqlTableModel(self, self.db)
        # self.model.setTable("medicines")
        # self.model.select()
        # # 将模型设置到表格视图
        # self.drug_selection_tableView.setModel(self.model)

    def bind_event(self):
        self.drug_selection.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.sales_records.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.expiring_drugs.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        # self.inventory_stock.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        # self.supplier_info.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        # self.drug_inbound.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        # self.drug_outbound.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        # self.recently_added.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))


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
