# from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QLineEdit, QPushButton
# from PySide6.QtCore import Qt, Signal
#
#
# class LoginWindow(QWidget):
#     login_success = Signal()  # 自定义信号，用于通知登录成功
#
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("登录")
#         self.setFixedSize(300, 150)
#
#         layout = QVBoxLayout()
#         self.password_input = QLineEdit()
#         self.password_input.setEchoMode(QLineEdit.Password)
#         btn_login = QPushButton("登录")
#         btn_login.clicked.connect(self.check_password)
#
#         layout.addWidget(self.password_input)
#         layout.addWidget(btn_login)
#         self.setLayout(layout)
#
#     def check_password(self):
#         if self.password_input.text() == "123456":  # 假设密码是123456
#             self.login_success.emit()  # 发射成功信号
#             self.close()  # 关闭登录窗口
#         else:
#             self.password_input.clear()
#             self.password_input.setPlaceholderText("密码错误，请重试")
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("主窗口")
#         self.resize(800, 600)
#
#
# if __name__ == "__main__":
#     import sys
#     from PySide6.QtWidgets import QApplication
#
#     app = QApplication(sys.argv)
#
#     # 创建窗口
#     login_window = LoginWindow()
#     main_window = MainWindow()
#
#     # 连接信号：登录成功后显示主窗口
#     login_window.login_success.connect(main_window.show)
#
#     # 显示登录窗口（非模态）
#     login_window.show()
#
#     sys.exit(app.exec())


from PySide6.QtWidgets import (QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget,
                               QMessageBox, QAbstractItemView, QPushButton, QHeaderView)
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("数据库行删除示例")
        self.setGeometry(100, 100, 800, 600)

        # 初始化UI
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # 创建表格视图
        self.tableView = QTableView()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 整行选择
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)  # 单选模式
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 添加删除按钮
        self.deleteButton = QPushButton("删除选中行")
        self.deleteButton.clicked.connect(self.delete_selected_row)
        self.deleteButton.setEnabled(False)  # 初始禁用

        # 添加到布局
        self.layout.addWidget(self.tableView)
        self.layout.addWidget(self.deleteButton)
        self.central_widget.setLayout(self.layout)

        # 初始化数据库
        self.init_db()
        self.setup_model()

        # 监听选择变化
        self.tableView.selectionModel().selectionChanged.connect(self.update_button_state)

    def init_db(self):
        # 创建SQLite数据库连接
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("example.db")

        if not self.db.open():
            QMessageBox.critical(self, "数据库错误", "无法打开数据库")
            return False

        # 创建示例表（如果不存在）
        query = QSqlQuery()
        query.exec("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT,
                salary REAL
            )
        """)

        # 插入一些示例数据
        query.exec("INSERT INTO employees (name, department, salary) VALUES ('张三', '技术部', 15000)")
        query.exec("INSERT INTO employees (name, department, salary) VALUES ('李四', '市场部', 12000)")
        query.exec("INSERT INTO employees (name, department, salary) VALUES ('王五', '人事部', 11000)")

        return True

    def setup_model(self):
        # 创建SQL表模型
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("employees")
        self.model.select()  # 从数据库加载数据

        # 设置表格标题
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "姓名")
        self.model.setHeaderData(2, Qt.Horizontal, "部门")
        self.model.setHeaderData(3, Qt.Horizontal, "薪资")

        # 应用到视图
        self.tableView.setModel(self.model)

    def update_button_state(self, selected):
        # 根据选择状态启用/禁用删除按钮
        has_selection = bool(selected.indexes())
        self.deleteButton.setEnabled(has_selection)

    def delete_selected_row(self):
        # 获取当前选择
        selection = self.tableView.selectionModel().selectedRows()

        if not selection:
            QMessageBox.warning(self, "提示", "请先选择要删除的行")
            return

        # 确认对话框
        reply = QMessageBox.question(
            self, "确认删除",
            "确定要删除选中的行吗？此操作无法撤销！",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        # 删除所有选中行（单行模式实际只会删一行）
        for index in selection:
            row = index.row()

            # 从模型中移除行
            if not self.model.removeRow(row):
                QMessageBox.critical(self, "错误", "删除失败: " + self.model.lastError().text())
                return

            # 提交到数据库
            if not self.model.submitAll():
                QMessageBox.critical(self, "错误", "数据库提交失败: " + self.model.lastError().text())
                self.model.revertAll()  # 撤销更改
                return

            # 刷新视图（因为删除后行号变化）
            self.model.select()

        QMessageBox.information(self, "成功", "已成功删除选中的行")

        # 重置按钮状态
        self.deleteButton.setEnabled(False)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()