# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
# from qtmodern.windows import ModernWindow
# from qtmodern.styles import dark, light
#
# app = QApplication(sys.argv)
#
# # 创建普通窗口
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("原始窗口")
#         self.setGeometry(100, 100, 300, 200)
#         btn = QPushButton("普通按钮", self)
#         btn.move(100, 80)
#
# # 转换为 Modern 风格窗口
# window = MainWindow()
# modern_window = ModernWindow(window)  # 包裹原始窗口
# modern_window.show()
#
# # 应用暗色主题
# # app.setStyleSheet(dark(app))
#
# # 亮色主题
# app.setStyleSheet(light(app))
# sys.exit(app.exec())

# from qtmodern.styles import dark, light
#
# # 暗色主题
# app.setStyleSheet(dark(app))
#
# # 亮色主题
# app.setStyleSheet(light(app))

#-------------------------------------------------------------------------------------------

import sys
from PySide6 import QtWidgets
# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

# # create the application and the main window
# app = QtWidgets.QApplication(sys.argv)
# window = QtWidgets.QMainWindow()
#
# # setup stylesheet
# apply_stylesheet(app, theme='dark_teal.xml')
#
# # run
# window.show()
# app.exec()


# import sys
#
# from PySide6.QtWidgets import QApplication
# from qframelesswindow import FramelessWindow
#
#
# class Window(FramelessWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent=parent)
#         self.setWindowTitle("PySide6-Frameless-Window")
#         self.titleBar.raise_()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Window()
#     demo.show()
#     app.exec()

# --------------------------------------------------------------------------------------------------
import sys
import sqlite3
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QComboBox, QPushButton, QVBoxLayout, QWidget, QLabel
)


# 创建模拟数据库（实际应用中替换为你的数据库连接）
def create_sample_db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE products
                 (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
    c.execute("INSERT INTO products VALUES (1, '笔记本电脑', 5999)")
    c.execute("INSERT INTO products VALUES (2, '智能手机', 3999)")
    c.execute("INSERT INTO products VALUES (3, '平板电脑', 2999)")
    c.execute("INSERT INTO products VALUES (4, '智能手表', 1599)")
    conn.commit()
    return conn


class MainWindow(QMainWindow):
    def __init__(self, db_conn):
        super().__init__()
        self.db_conn = db_conn
        self.setWindowTitle("数据库选择器")
        self.resize(400, 200)

        # 创建UI元素
        self.combo_box = QComboBox()
        self.status_label = QLabel("请从下拉列表中选择一项")
        refresh_button = QPushButton("刷新数据")
        refresh_button.clicked.connect(self.populate_combo)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.status_label)
        layout.addWidget(refresh_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # 初始填充数据
        self.populate_combo()

        # 连接选择改变信号
        self.combo_box.currentIndexChanged.connect(self.selection_changed)

    def populate_combo(self):
        """从数据库填充下拉框数据"""
        self.combo_box.clear()  # 清空现有项

        # 从数据库查询数据
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT id, name, price FROM products")
        products = cursor.fetchall()

        # 填充下拉框
        for product in products:
            product_id, name, price = product
            # 添加带格式化的显示文本，并存储ID在用户数据中
            self.combo_box.addItem(f"{name} - ¥{price:.2f}", product_id)

        # 设置初始选择状态
        self.status_label.setText("数据已加载，请选择")

    def selection_changed(self, index):
        """当用户选择改变时触发"""
        if index >= 0:  # 确保有效选择
            selected_id = self.combo_box.itemData(index)  # 获取关联的ID
            self.status_label.setText(f"已选择产品ID: {selected_id}")

            # 实际应用中可以查询数据库获取完整信息
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT * FROM products WHERE id = ?", (selected_id,))
            product_info = cursor.fetchone()

            if product_info:
                self.status_label.setText(
                    f"选择的产品: ID={product_info[0]}, 名称={product_info[1]}, 价格=¥{product_info[2]:.2f}"
                )


# 启动应用
if __name__ == "__main__":
    # 创建并初始化数据库
    db_connection = create_sample_db()

    app = QApplication(sys.argv)
    window = MainWindow(db_connection)
    window.show()
    sys.exit(app.exec())

    # 实际应用中记得关闭数据库连接
    db_connection.close()