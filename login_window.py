from PySide6.QtCore import Signal
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QWidget, QMessageBox
from ui_app.log_in_ui import Ui_Form


class LoginWindow(QWidget, Ui_Form):
    login_success = Signal()  # 自定义信号，用于通知登录成功

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind_event()

    def bind_event(self):
        self.log_on_btn.clicked.connect(self.login)
        from main_window import MainWindow
        self.mainwindow = MainWindow()
        # 连接信号：登录成功后显示主窗口
        self.login_success.connect(self.mainwindow.show)

    def login(self):
        account = self.account_le.text().strip()
        password = self.password_le.text().strip()
        query = QSqlQuery()
        # query.exec(f"SELECT * FROM users WHERE account='{account}' AND password='{password}'")
        if account == "" and password == "":
            # if query.exec(f"SELECT * FROM users WHERE account='{account}' AND password='{password}'"):
            self.login_success.emit()  # 发射成功信号
            self.close()  # 关闭登录窗口
            # print("支持的数据库驱动:", QSqlDatabase.drivers())
        else:
            self.account_le.clear()
            self.password_le.clear()
            self.tiplb.setText("用户名或密码错误")
