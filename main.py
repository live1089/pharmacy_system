"""
Author: live1089 a5u3580@163.com
Date: 2025-06-11 17:10:47
LastEditors: live1089 a5u3580@163.com
LastEditTime: 2025-06-11 17:18:55
FilePath: \Pharmacy_drug_management_system\main.py
"""
# 主题
import qdarkstyle
# 外部UI
import ui_app.log_in_ui
# 导入pyside6库
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget
from PySide6.QtCore import QCoreApplication, Qt, QByteArray
from PySide6.QtGui import QIcon, QPixmap
# 其他工具
import base64
# from icon_data import icon_data  # 导入生成的图标数据


class LoginWindow(QWidget, ui_app.log_in_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind_event()
        # self.account_password = []

    def  bind_event(self):
        self.log_on_btn.clicked.connect(self.login)
        # self.account_le.textChanged.connect(self.check_input)
        # self.password_le.textChanged.connect(self.check_input)


    # def  check_input(self):
    #     self.account_password = [
    #         self.account_le.text().strip(),
    #         self.password_le.text().strip()
    #     ]

    def  login(self):
        # account = self.account_password[0]
        # password = self.account_password[1]
        account = self.account_le.text().strip()
        password = self.password_le.text().strip()
        if account == "123" and password == "123":
            print("账号：", account)
            print("密码：", password)
            self.tiplb.setText("登录成功")
        else:
            self.tiplb.setText("用户名或密码错误")


if __name__ == "__main__":
    app = QApplication([])
    # icon_bytes = QByteArray(base64.b64decode(icon_data))
    # pixmap = QPixmap()
    # pixmap.loadFromData(icon_bytes, "ICO")  # 指定格式为 ICO
    # icon = QIcon(pixmap)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    # app.setWindowIcon(icon)
    window = LoginWindow()
    # window.setWindowIcon(icon)
    window.show()
    app.exec()


