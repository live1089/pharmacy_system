# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
药品管理系统主入口文件
"""

import os
import sys

import qdarktheme
from PySide6.QtWidgets import QApplication

from login_window import LoginWindow

# 添加当前目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# 确保data目录存在
data_dir = os.path.join(current_dir, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# 确保backups目录存在
backups_dir = os.path.join(current_dir, 'backups')
if not os.path.exists(backups_dir):
    os.makedirs(backups_dir)


def main():
    app = QApplication(sys.argv)

    # 应用暗色主题
    app.setStyleSheet(qdarktheme.load_stylesheet())

    # 创建并显示登录窗口
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
