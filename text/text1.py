from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog,
                               QLabel, QLineEdit, QPushButton,
                               QVBoxLayout, QMessageBox)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.setGeometry(100, 100, 800, 600)

        label = QLabel("欢迎使用主程序！", self)
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录")
        self.setFixedSize(300, 150)

        self.init_ui()
        self.attempts = 0
        self.max_attempts = 3

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("请输入密码:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("登录")
        self.login_button.clicked.connect(self.check_password)

        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_password(self):
        # 这里设置你的正确密码
        correct_password = "123456"

        if self.password_input.text() == correct_password:
            self.accept()  # 关闭对话框并返回QDialog.Accepted
        else:
            self.attempts += 1
            remaining = self.max_attempts - self.attempts

            if remaining > 0:
                self.label.setText(f"密码错误，还剩{remaining}次尝试:")
                self.password_input.clear()
            else:
                QMessageBox.critical(self, "错误", "尝试次数过多，程序将退出")
                self.reject()  # 关闭对话框并返回QDialog.Rejected


if __name__ == "__main__":
    app = QApplication([])

    login = LoginDialog()
    result = login.exec()

    if result == QDialog.Accepted:
        main_window = MainWindow()
        main_window.show()
        app.exec()
    else:
        app.quit()