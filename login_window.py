import hashlib
import os

from PySide6.QtCore import Signal
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QWidget

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

        self.tip_btn.clicked.connect(self.tip_show)

    def tip_show(self):
        """显示密码提示信息"""
        try:
            query = QSqlQuery()
            query.exec("SELECT tip FROM users LIMIT 1")
            if query.next():
                tip_text = query.value(0)
                if tip_text and tip_text.strip():
                    self.tiplb.setText(f"提示: {tip_text}")
                else:
                    self.tiplb.setText("暂无提示信息")
            else:
                self.tiplb.setText("暂无提示信息")
        except Exception as e:
            self.tiplb.setText(f"获取提示信息失败: {str(e)}")

    def hash_password(self, password, salt=None):
        """对密码进行哈希加密"""
        if salt is None:
            salt = os.urandom(32)  # 生成随机盐值

        pwdhash = hashlib.pbkdf2_hmac('sha256',
                                      password.encode('utf-8'),
                                      salt,
                                      100000)  # 100000次迭代
        return pwdhash, salt

    def verify_password(self, stored_password, stored_salt, provided_password):
        """验证密码"""
        pwdhash, _ = self.hash_password(provided_password, stored_salt)
        return pwdhash == stored_password

    def login(self):
        account = self.account_le.text().strip()
        password = self.password_le.text().strip()

        # 确保数据库中有用户，如果没有则创建默认用户
        self.ensure_default_user_exists()

        if not account or not password:
            self.tiplb.setText("用户名和密码不能为空")
            return

        query = QSqlQuery()
        query.prepare("SELECT password, salt FROM users WHERE username = ?")
        query.addBindValue(account)

        if query.exec() and query.next():
            stored_password = query.value(0)
            stored_salt = query.value(1)

            # 将存储的字符串转换为bytes
            try:
                salt_bytes = bytes.fromhex(stored_salt)
                pwd_bytes = bytes.fromhex(stored_password)

                if self.verify_password(pwd_bytes, salt_bytes, password):
                    self.login_success.emit()  # 发射成功信号
                    self.close()  # 关闭登录窗口
                else:
                    self.account_le.clear()
                    self.password_le.clear()
                    self.tiplb.setText("用户名或密码错误")
            except ValueError:
                # 如果是旧的明文密码，进行兼容处理
                if stored_password == password:
                    # 将明文密码转换为加密密码
                    self.update_to_hashed_password(account, password)
                    self.login_success.emit()
                    self.close()
                else:
                    self.account_le.clear()
                    self.password_le.clear()
                    self.tiplb.setText("用户名或密码错误")
        else:
            # 兼容默认空账号密码的情况
            if account == "" and password == "":
                self.login_success.emit()
                self.close()
            else:
                self.account_le.clear()
                self.password_le.clear()
                self.tiplb.setText("用户名或密码错误")

    def update_to_hashed_password(self, username, password):
        """将明文密码更新为加密密码"""
        pwdhash, salt = self.hash_password(password)
        query = QSqlQuery()
        query.prepare("UPDATE users SET password=?, salt=? WHERE username=?")
        query.addBindValue(pwdhash.hex())
        query.addBindValue(salt.hex())
        query.addBindValue(username)
        query.exec()

    def ensure_default_user_exists(self):
        """确保默认用户存在"""
        query = QSqlQuery()
        query.exec("SELECT COUNT(*) FROM users")
        if query.next() and query.value(0) == 0:
            # 创建默认用户 (用户名: admin, 密码: admin123)
            username = "admin"
            password = "admin123"

            # 对密码进行加密
            pwdhash, salt = self.hash_password(password)

            query.prepare("INSERT INTO users (username, password, salt, phone_number, tip) VALUES (?, ?, ?, ?, ?)")
            query.addBindValue(username)
            query.addBindValue(pwdhash.hex())
            query.addBindValue(salt.hex())
            query.addBindValue("xxxxxxxxxxxxx")
            query.addBindValue("默认管理员账户")

            if query.exec():
                print("默认用户创建成功")
            else:
                print(f"默认用户创建失败: {query.lastError().text()}")
