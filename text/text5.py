# from PySide6.QtWidgets import QApplication, QStackedWidget, QPushButton, QLabel, QVBoxLayout, QWidget
#
# app = QApplication([])
#
# # 创建堆叠窗口和两个页面
# stacked_widget = QStackedWidget()
#
# page1 = QWidget()
# layout1 = QVBoxLayout()
# layout1.addWidget(QLabel("这是页面 1"))
# button_to_page2 = QPushButton("切换到页面 2")
# layout1.addWidget(button_to_page2)
# page1.setLayout(layout1)
#
# page2 = QWidget()
# layout2 = QVBoxLayout()
# layout2.addWidget(QLabel("这是页面 2"))
# button_to_page1 = QPushButton("返回页面 1")
# layout2.addWidget(button_to_page1)
# page2.setLayout(layout2)
#
# # 添加页面到堆叠窗口
# stacked_widget.addWidget(page1)
# stacked_widget.addWidget(page2)
#
# # 绑定按钮信号
# button_to_page2.clicked.connect(lambda: stacked_widget.setCurrentIndex(1))
# button_to_page1.clicked.connect(lambda: stacked_widget.setCurrentIndex(0))
#
# stacked_widget.show()
# app.exec()



# from PySide6.QtWidgets import QApplication, QTableView
# from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
#
# app = QApplication([])
#
# # 1. 连接数据库
# db = QSqlDatabase.addDatabase("QSQLITE")
# db.setDatabaseName("text.db")  # 数据库文件
# if not db.open():
#     print("数据库连接失败！")
#     exit()
#
# # 2. 创建数据模型并绑定表
# model = QSqlTableModel()
# model.setTable("drugs")  # 假设表已存在
# model.select()  # 加载数据
#
# query = QSqlQuery()
#
# # 创建药品表
# query.exec("""
# CREATE TABLE IF NOT EXISTS drugs (
#     id TEXT PRIMARY KEY,
#     name TEXT NOT NULL,
#     stock INTEGER DEFAULT 0,
#     price REAL,
#     expiry_date DATE
# )
# """)
#
# # 检查是否成功
# if not query.isActive():
#     print("建表失败:", query.lastError().text())
# else:
#     print("药品表创建成功！")
#
# db.close()
#
# # 3. 显示数据到表格
# view = QTableView()
# view.setModel(model)
# view.show()
#
# app.exec()


import sqlite3
print(sqlite3.sqlite_version)
















