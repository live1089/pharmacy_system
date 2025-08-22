from ui_app.inventory_count_entry_ui import Ui_InventoryCountDialog
from PySide6.QtCore import QDate, QDateTime
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox


class InventoryCountPage(QDialog, Ui_InventoryCountDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.check_id = None
        self.load_data()

    def bind_event(self):
        self.buttonBox.accepted.connect(self.save)

    def load_data(self):
        query = QSqlQuery()
        query.prepare("SELECT medicine_id FROM inventory_check")

    def save(self):
        pass
