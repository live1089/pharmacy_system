import hashlib
import os

from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox

from page_window.system_formatting import complete_factory_reset
from page_window.tools import install_enter_key_filter
from ui_app.current_account_ui import Ui_CurrentDialog
from ui_app.user_set_ui import Ui_Dialog
from ui_app.sys_form_ui import Ui_SysDialog


class UserSetPage(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.ignore_cargo_return()
        self.load_current_user_data()

    def ignore_cargo_return(self):
        install_enter_key_filter(self.user_name_lineEdit)
        install_enter_key_filter(self.phone_number_lineEdit)
        install_enter_key_filter(self.old_password_lineEdit)
        install_enter_key_filter(self.new_password_lineEdit)
        install_enter_key_filter(self.tip_textEdit)

    def load_current_user_data(self):
        """加载当前用户数据"""
        query = QSqlQuery()
        query.exec("SELECT username, phone_number, tip FROM users LIMIT 1")
        if query.next():
            self.user_name_lineEdit.setText(query.value(0))
            self.phone_number_lineEdit.setText(query.value(1))
            self.tip_textEdit.setText(query.value(2))

    def bind_event(self):
        if hasattr(self, 'user_save_btn'):
            self.user_save_btn.clicked.connect(self.save_user_info)

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

    def save_user_info(self):
        """保存用户信息"""
        user_name = self.user_name_lineEdit.text().strip()
        phone = self.phone_number_lineEdit.text().strip()
        old_password = self.old_password_lineEdit.text().strip()
        new_password = self.new_password_lineEdit.text().strip()
        tip = self.tip_textEdit.toPlainText().strip()

        # 验证输入
        if not user_name:
            QMessageBox.warning(self, "输入错误", "用户名不能为空")
            return

        if not old_password:
            QMessageBox.warning(self, "输入错误", "请输入旧密码")
            return

        if not new_password:
            QMessageBox.warning(self, "输入错误", "请输入新密码")
            return

        # 验证旧密码
        if not self.verify_old_password(old_password):
            QMessageBox.warning(self, "密码错误", "旧密码不正确")
            return

        # 更新用户信息
        self.update_user_info(user_name, phone, new_password, tip)

    def verify_old_password(self, old_password):
        """验证旧密码"""
        query = QSqlQuery()
        query.prepare("SELECT password, salt FROM users LIMIT 1")
        if query.exec() and query.next():
            stored_password = query.value(0)
            stored_salt = query.value(1)
            # 将存储的 QByteArray 转换为 bytes
            if isinstance(stored_salt, str):
                salt_bytes = bytes.fromhex(stored_salt)
            else:
                salt_bytes = stored_salt
            if isinstance(stored_password, str):
                pwd_bytes = bytes.fromhex(stored_password)
            else:
                pwd_bytes = stored_password
            return self.verify_password(pwd_bytes, salt_bytes, old_password)
        return False

    def update_user_info(self, user_name, phone, new_password, tip):
        """更新用户信息"""
        # 对新密码进行加密
        pwdhash, salt = self.hash_password(new_password)

        query = QSqlQuery()
        query.prepare("UPDATE users SET username=?, password=?, salt=?, phone_number=?, tip=? WHERE users_id=1")
        query.addBindValue(user_name)
        query.addBindValue(pwdhash.hex())  # 转换为十六进制字符串存储
        query.addBindValue(salt.hex())  # 转换为十六进制字符串存储
        query.addBindValue(phone)
        query.addBindValue(tip)

        if query.exec():
            QMessageBox.information(self, "成功", "用户信息更新成功")
            self.accept()  # 关闭对话框
        else:
            QMessageBox.critical(self, "数据库错误", f"更新失败: {query.lastError().text()}")


class CurrentUserPage(QDialog, Ui_CurrentDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.load_user_data()

    def load_user_data(self):
        query = QSqlQuery("SELECT username FROM users LIMIT 1")
        if query.exec() and query.next():
            username = query.value(0)
            self.current_user_lineEdit.setText(username)

        query = QSqlQuery("SELECT phone_number FROM users LIMIT 1")
        if query.exec() and query.next():
            phone_number = query.value(0)
            self.current_phone_lineEdit.setText(phone_number)


import window_methods as wim


class SystemPage(QDialog, Ui_SysDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()

    def bind_event(self):
        self.system_formatting_btn.clicked.connect(self.system_formatting)

        self.back_data_btn.clicked.connect(lambda: wim.backup_database_event(self))
        self.action_restore_btn.clicked.connect(lambda: wim.restore_database_event(self))
        self.action_auto_backup_btn.clicked.connect(lambda: wim.auto_backup_database_event(self))

    def system_formatting(self):
        """系统格式化"""
        complete_factory_reset(self, self.ui.db)
