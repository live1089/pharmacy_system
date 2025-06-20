import sys
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtWidgets import QMessageBox


class DatabaseInit(QSqlDatabase, QMessageBox):
    def __init__(self):
        super().__init__()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("pharmacy.db")
        if not self.db.open():
            QMessageBox.critical(self, "错误", "无法打开数据库")
            sys.exit(1)

    def create_table(self):
        query = QSqlQuery()
        query.exec("""
        CREATE TABLE IF NOT EXISTS drugs (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            stock INTEGER DEFAULT 0,
            price REAL,
            expiry_date DATE
        )
        """)
        return True