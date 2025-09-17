"""
Author: live1089 a5u3580@163.com
Date: 2025-06-11 17:10:47
LastEditors: live1089 a5u3580@163.com
LastEditTime: 2025-06-11 17:18:55
FilePath: \\Pharmacy_drug_management_system\\main.py
"""

# 导入pyside6库
from PySide6.QtWidgets import (QApplication)
# 主题
from qtmodern.styles import dark

import login_window
if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(dark(app))
    LoginWindow = login_window.LoginWindow()
    LoginWindow.show()
    app.exec()