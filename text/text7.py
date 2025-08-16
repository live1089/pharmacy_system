import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableView, QPushButton,
    QVBoxLayout, QWidget, QHeaderView, QDialog,
    QFormLayout, QLineEdit, QDialogButtonBox, QMessageBox
)
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtCore import Qt


class DatabaseManager:
    """数据库管理类，处理所有数据库操作"""

    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("contacts.db")

        if not self.db.open():
            QMessageBox.critical(
                None, "数据库错误",
                f"无法打开数据库: {self.db.lastError().text()}"
            )
            sys.exit(1)

        # 创建表结构
        query = QSqlQuery()
        query.exec("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                notes TEXT
            )
        """)

    def get_model(self):
        """返回用于表视图的模型"""
        model = QSqlTableModel()
        model.setTable("contacts")  # 设置模型对应的数据表为 contacts
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(1, Qt.Horizontal, "姓名")
        model.setHeaderData(2, Qt.Horizontal, "电话")
        model.setHeaderData(3, Qt.Horizontal, "邮箱")
        model.setHeaderData(4, Qt.Horizontal, "备注")
        return model


class ContactDialog(QDialog):
    """添加/编辑联系人的对话框"""

    def __init__(self, parent=None, contact_id=None):
        super().__init__(parent)
        self.setWindowTitle("添加联系人" if contact_id is None else "编辑联系人")
        self.contact_id = contact_id

        layout = QFormLayout(self)

        self.name_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.notes_edit = QLineEdit()

        layout.addRow("姓名:", self.name_edit)
        layout.addRow("电话:", self.phone_edit)
        layout.addRow("邮箱:", self.email_edit)
        layout.addRow("备注:", self.notes_edit)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

        # 如果是编辑模式，加载现有数据
        if contact_id:
            query = QSqlQuery()
            query.prepare("SELECT * FROM contacts WHERE id = ?")
            query.addBindValue(contact_id)
            query.exec()
            if query.next():
                self.name_edit.setText(query.value("name"))
                self.phone_edit.setText(query.value("phone"))
                self.email_edit.setText(query.value("email"))
                self.notes_edit.setText(query.value("notes"))

    def get_data(self):
        """返回对话框中的数据"""
        return {
            "name": self.name_edit.text(),
            "phone": self.phone_edit.text(),
            "email": self.email_edit.text(),
            "notes": self.notes_edit.text()
        }


class MainWindow(QMainWindow):
    """主应用程序窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("联系人管理")
        self.resize(800, 600)

        # 初始化数据库
        self.db_manager = DatabaseManager()

        # 创建UI
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # 创建按钮
        button_layout = QVBoxLayout()

        self.add_btn = QPushButton("添加联系人")
        self.add_btn.clicked.connect(self.add_contact)

        self.edit_btn = QPushButton("编辑联系人")
        self.edit_btn.clicked.connect(self.edit_contact)

        self.delete_btn = QPushButton("删除联系人")
        self.delete_btn.clicked.connect(self.delete_contact)

        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.edit_btn)
        button_layout.addWidget(self.delete_btn)

        # 创建表格视图
        self.table_view = QTableView()
        self.table_view.setModel(self.db_manager.get_model())
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setColumnHidden(0, True)  # 隐藏ID列

        # 添加控件到布局
        layout.addLayout(button_layout)
        layout.addWidget(self.table_view)

        self.setCentralWidget(central_widget)

    def get_selected_id(self):
        """获取选中行的ID"""
        selection = self.table_view.selectionModel().selectedRows(0)
        if selection:
            return selection[0].data()
        return None

    def add_contact(self):
        """添加新联系人"""
        dialog = ContactDialog(self)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()

            query = QSqlQuery()
            query.prepare("""
                INSERT INTO contacts (name, phone, email, notes)
                VALUES (?, ?, ?, ?)
            """)
            query.addBindValue(data["name"])
            query.addBindValue(data["phone"])
            query.addBindValue(data["email"])
            query.addBindValue(data["notes"])

            if not query.exec():
                QMessageBox.critical(
                    self, "数据库错误",
                    f"添加联系人失败: {query.lastError().text()}"
                )
            else:
                # 刷新模型以显示新数据
                self.table_view.model().select()

    def edit_contact(self):
        """编辑现有联系人"""
        contact_id = self.get_selected_id()
        if not contact_id:
            QMessageBox.warning(self, "选择错误", "请先选择一个联系人")
            return

        dialog = ContactDialog(self, contact_id)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()

            query = QSqlQuery()
            query.prepare("""
                UPDATE contacts 
                SET name = ?, phone = ?, email = ?, notes = ?
                WHERE id = ?
            """)
            query.addBindValue(data["name"])
            query.addBindValue(data["phone"])
            query.addBindValue(data["email"])
            query.addBindValue(data["notes"])
            query.addBindValue(contact_id)

            if not query.exec():
                QMessageBox.critical(
                    self, "数据库错误",
                    f"更新联系人失败: {query.lastError().text()}"
                )
            else:
                # 刷新模型以显示更新后的数据
                self.table_view.model().select()

    def delete_contact(self):
        """删除选中的联系人"""
        contact_id = self.get_selected_id()
        if not contact_id:
            QMessageBox.warning(self, "选择错误", "请先选择一个联系人")
            return

        reply = QMessageBox.question(
            self, "确认删除",
            "确定要删除此联系人吗?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            query = QSqlQuery()
            query.prepare("DELETE FROM contacts WHERE id = ?")
            query.addBindValue(contact_id)

            if not query.exec():
                QMessageBox.critical(
                    self, "数据库错误",
                    f"删除联系人失败: {query.lastError().text()}"
                )
            else:
                # 刷新模型以显示更新后的数据
                self.table_view.model().select()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 检查SQLite驱动是否可用
    if "QSQLITE" not in QSqlDatabase.drivers():
        QMessageBox.critical(
            None, "驱动错误",
            "SQLite驱动(QSQLITE)不可用，无法运行此应用"
        )
        sys.exit(1)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())