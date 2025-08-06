from ui_app.sell_drug_ui import Ui_SellDialog
from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit, QDialogButtonBox, QVBoxLayout


class sell_drug_ui_dialog(QDialog, Ui_SellDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.load_combo()

    def bind_event(self):
        pass

    def load_combo(self):
        pass
