# import sys
# from PySide6.QtWidgets import (
#     QApplication, QMainWindow, QTabWidget,
#     QWidget, QLabel, QVBoxLayout, QPushButton
# )
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("TabWidget 示例")
#         self.setGeometry(100, 100, 600, 400)
#
#         # 1. 创建 TabWidget
#         self.tab_widget = QTabWidget()
#         self.setCentralWidget(self.tab_widget)
#
#         # 2. 创建三个标签页
#         self.tab1 = self.create_tab1()
#         self.tab2 = self.create_tab2()
#         self.tab3 = self.create_tab3()
#
#         # 3. 添加标签页
#         self.tab_widget.addTab(self.tab1, "基本信息")
#         self.tab_widget.addTab(self.tab2, "高级设置")
#         self.tab_widget.addTab(self.tab3, "帮助")
#
#         # 4. 可选：监听标签切换信号
#         self.tab_widget.currentChanged.connect(self.tab_changed)
#
#     def create_tab1(self):
#         """创建第一个标签页"""
#         tab = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("这是基本信息页面"))
#         layout.addWidget(QPushButton("保存设置"))
#         tab.setLayout(layout)
#         return tab
#
#     def create_tab2(self):
#         """创建第二个标签页"""
#         tab = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("高级配置选项"))
#         layout.addWidget(QPushButton("启用高级模式"))
#         tab.setLayout(layout)
#         return tab
#
#     def create_tab3(self):
#         """创建第三个标签页"""
#         tab = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("帮助文档"))
#         layout.addWidget(QPushButton("在线帮助"))
#         tab.setLayout(layout)
#         return tab
#
#     def tab_changed(self, index):
#         """标签切换时触发"""
#         print(f"已切换到标签页: {index} ({self.tab_widget.tabText(index)})")
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())



# # 切换到第二个标签页（索引从0开始）
# self.tab_widget.setCurrentIndex(1)
#
# # 通过标签名称切换
# index = self.tab_widget.indexOf(tab_widget_instance)
# self.tab_widget.setCurrentIndex(index)


# import sys
# from PySide6.QtWidgets import (
#     QApplication, QMainWindow, QTabWidget,
#     QWidget, QVBoxLayout, QTableView, QHeaderView  # 添加了QHeaderView
# )
# from PySide6.QtCore import Qt
# from PySide6.QtGui import QStandardItemModel, QStandardItem
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Table in TabWidget 示例")
#         self.resize(800, 600)
#
#         # 创建主TabWidget
#         self.tab_widget = QTabWidget()
#         self.setCentralWidget(self.tab_widget)
#
#         # 创建包含tableView的标签页
#         self.table_tab = self.create_table_tab()
#         self.info_tab = self.create_info_tab()
#
#         # 添加标签页
#         self.tab_widget.addTab(self.table_tab, "数据表格")
#         self.tab_widget.addTab(self.info_tab, "信息详情")
#
#         # 初始化数据模型
#         self.setup_table_model()
#
#     def create_table_tab(self):
#         """创建包含表格的标签页"""
#         tab = QWidget()
#         layout = QVBoxLayout()
#
#         # 1. 创建TableView并设置属性
#         self.tableView = QTableView()
#         self.tableView.setAlternatingRowColors(True)  # 交替行颜色
#         self.tableView.setSortingEnabled(True)  # 启用排序
#
#         # 2. 添加到布局
#         layout.addWidget(self.tableView)
#         tab.setLayout(layout)
#         return tab
#
#     def create_info_tab(self):
#         """创建简单信息标签页"""
#         tab = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(QWidget())  # 实际应用中替换为实际内容
#         tab.setLayout(layout)
#         return tab
#
#     def setup_table_model(self):
#         """设置表格数据模型"""
#         # 1. 创建标准项模型 (rows, columns)
#         model = QStandardItemModel(4, 3)
#
#         # 2. 设置表头
#         model.setHeaderData(0, Qt.Horizontal, "姓名")
#         model.setHeaderData(1, Qt.Horizontal, "年龄")
#         model.setHeaderData(2, Qt.Horizontal, "职业")
#
#         # 3. 填充示例数据
#         data = [
#             ["张三", "25", "工程师"],
#             ["李四", "30", "设计师"],
#             ["王五", "45", "经理"],
#             ["赵六", "28", "分析师"]
#         ]
#
#         for row, row_data in enumerate(data):
#             for col, value in enumerate(row_data):
#                 item = QStandardItem(value)
#                 item.setEditable(False)  # 设置单元格不可编辑
#                 model.setItem(row, col, item)
#
#         # 4. 连接模型到视图
#         self.tableView.setModel(model)
#
#         # 5. 修复这里：使用QHeaderView的枚举
#         # 设置第二列拉伸填充
#         self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
#
#         # 可选：设置其他列的模式
#         # self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
#         # self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
#         # self.tableView.setColumnWidth(2, 150)  # 设置固定宽度
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())










