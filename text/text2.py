from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Qt, Signal


class LoginWindow(QWidget):
    login_success = Signal()  # 自定义信号，用于通知登录成功

    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        btn_login = QPushButton("登录")
        btn_login.clicked.connect(self.check_password)

        layout.addWidget(self.password_input)
        layout.addWidget(btn_login)
        self.setLayout(layout)

    def check_password(self):
        if self.password_input.text() == "123456":  # 假设密码是123456
            self.login_success.emit()  # 发射成功信号
            self.close()  # 关闭登录窗口
        else:
            self.password_input.clear()
            self.password_input.setPlaceholderText("密码错误，请重试")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.resize(800, 600)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    # 创建窗口
    login_window = LoginWindow()
    main_window = MainWindow()

    # 连接信号：登录成功后显示主窗口
    login_window.login_success.connect(main_window.show)

    # 显示登录窗口（非模态）
    login_window.show()

    sys.exit(app.exec())