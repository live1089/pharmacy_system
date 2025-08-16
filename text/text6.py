import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget,
    QPushButton, QLineEdit, QLabel, QHBoxLayout, QMessageBox
)
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 初始化数据库
        self.init_database()

        # 设置窗口标题和大小
        self.setWindowTitle("PySide6 SQLite CRUD 示例")
        self.resize(600, 400)

        # 创建中心部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建表格视图
        self.table_view = QTableView()
        layout.addWidget(self.table_view)

        # 创建表单布局
        form_layout = QHBoxLayout()
        layout.addLayout(form_layout)

        # 创建输入框和标签
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        form_layout.addWidget(QLabel("姓名:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("年龄:"))
        form_layout.addWidget(self.age_input)

        # 创建按钮布局
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # 创建按钮
        self.add_button = QPushButton("添加")
        self.add_button.clicked.connect(self.add_user)
        self.delete_button = QPushButton("删除")
        self.delete_button.clicked.connect(self.delete_user)
        self.update_button = QPushButton("更新")
        self.update_button.clicked.connect(self.update_user)
        self.query_button = QPushButton("查询")
        self.query_button.clicked.connect(self.query_users)

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.query_button)

        # 初始化表格模型
        self.model = QSqlTableModel()
        self.model.setTable("users")
        self.model.select()
        self.table_view.setModel(self.model)

    def init_database(self):
        """初始化数据库"""
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("example.db")
        if not db.open():
            QMessageBox.critical(self, "错误", "无法打开数据库")
            sys.exit(1)

        query = QSqlQuery()
        query.exec("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
        """)

# 添加用户
    def add_user(self):
        """添加用户"""
        name = self.name_input.text()
        age = self.age_input.text()
        if not name or not age:
            QMessageBox.warning(self, "警告", "姓名和年龄不能为空")
            return

        query = QSqlQuery()
        query.prepare("INSERT INTO users (name, age) VALUES (:name, :age)")
        query.bindValue(":name", name)
        query.bindValue(":age", int(age))
        if not query.exec():
            QMessageBox.critical(self, "错误", query.lastError().text())
        else:
            QMessageBox.information(self, "成功", "用户添加成功")
            self.model.select()

# 删除用户
    def delete_user(self):
        """删除用户"""
        selected = self.table_view.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self, "警告", "请选择要删除的行")
            return

        row = selected[0].row()
        user_id = self.model.data(self.model.index(row, 0))  # 获取选中行的 ID

        query = QSqlQuery()
        query.prepare("DELETE FROM users WHERE id = :id")
        query.bindValue(":id", user_id)
        if not query.exec_():
            QMessageBox.critical(self, "错误", query.lastError().text())
        else:
            QMessageBox.information(self, "成功", "用户删除成功")
            self.model.select()

    def update_user(self):
        """更新用户"""
        selected = self.table_view.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self, "警告", "请选择要更新的行")
            return

        row = selected[0].row()
        user_id = self.model.data(self.model.index(row, 0))  # 获取选中行的 ID

        name = self.name_input.text()
        age = self.age_input.text()
        if not name or not age:
            QMessageBox.warning(self, "警告", "姓名和年龄不能为空")
            return

        query = QSqlQuery()
        query.prepare("UPDATE users SET name = :name, age = :age WHERE id = :id")
        query.bindValue(":name", name)
        query.bindValue(":age", int(age))
        query.bindValue(":id", user_id)
        if not query.exec():
            QMessageBox.critical(self, "错误", query.lastError().text())
        else:
            QMessageBox.information(self, "成功", "用户更新成功")
            self.model.select()

    def query_users(self):
        """查询用户"""
        query = QSqlQuery()
        query.exec("SELECT * FROM users")
        while query.next():
            print(f"ID: {query.value(0)}, Name: {query.value(1)}, Age: {query.value(2)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

