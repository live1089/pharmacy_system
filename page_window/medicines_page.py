from data.sqlite_data import MedicineCategoriesModel, DrugRormulationModel, DrugUnitModel, SpecificationModel
from ui_app.drug_add_ui import Ui_Dialog
from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit, QDialog
from ui_app.drug_attribute_ui import Ui_class_dialog
from ui_app.drug_rormulation_ui import Ui_RormuDialog
from ui_app.drug_specification_ui import Ui_SpecificationDialog
from ui_app.drug_unit_ui import Ui_UnitDialog

# 药品页面
class MedicinesPage(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()

    def bind_event(self):
        self.drug_add_save_btn.clicked.connect(self.save)

    def save(self):
        drug_name = self.drug_name_line_edit.text()

# 类别页面
class DrugAttributePage(QDialog, Ui_class_dialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.db = parent.db
        self.bind_event()
        self.get_drug_attribute_model()

    def bind_event(self):
        pass

    def get_drug_attribute_model(self):
        self.drug_attribute_model = MedicineCategoriesModel(self, self.db)
        self.class_set_tableView.setModel(self.drug_attribute_model)

        for col in self.drug_attribute_model.hidden_columns:
            self.class_set_tableView.hideColumn(col)

        return self.drug_attribute_model



# 药品
class DrugRormulationPage(QDialog, Ui_RormuDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.db = parent.db
        # self.bind_event()
        self.get_drug_rormulateon_model()



    def get_drug_rormulateon_model(self):
        self.drug_rormulateon = DrugRormulationModel(self, self.db)
        self.rormulation_set_tableView.setModel(self.drug_rormulateon)

        for col in self.drug_rormulateon.hidden_columns:
            self.rormulation_set_tableView.hideColumn(col)

        return self.drug_rormulateon


class DrugUnitPage(QDialog, Ui_UnitDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.db = parent.db
        # self.bind_event()
        self.get_drug_unit_model()

    def get_drug_unit_model(self):
        self.drug_unit = DrugUnitModel(self, self.db)
        self.unit_set_tableView.setModel(self.drug_unit)

        for col in self.drug_unit.hidden_columns:
            self.unit_set_tableView.hideColumn(col)

        return self.drug_unit



class DrugSpecificationPage(QDialog, Ui_SpecificationDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.db = parent.db
        # self.bind_event()
        self.get_drug_specification_model()

    def get_drug_specification_model(self):
        self.drug_specification = SpecificationModel(self, self.db)
        self.specification_tableView.setModel(self.drug_specification)

        for col in self.drug_specification.hidden_columns:
            self.specification_tableView.hideColumn(col)

        return self.drug_specification