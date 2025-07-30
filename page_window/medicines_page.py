from PySide6.QtSql import QSqlQuery

from data.sqlite_data import MedicineCategoriesModel, DrugRormulationModel, DrugUnitModel, SpecificationModel
from ui_app.drug_add_ui import Ui_Dialog
from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit, QDialog, QDialogButtonBox, QVBoxLayout
from ui_app.drug_attribute_ui import Ui_class_dialog
from ui_app.drug_rormulation_ui import Ui_RormuDialog
from ui_app.drug_specification_ui import Ui_SpecificationDialog
from ui_app.drug_unit_ui import Ui_UnitDialog


class PopupDialog(QDialog):
    def __init__(self, parent=None, title="输入数据"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(320, 188)

        # 设置布局
        layout = QVBoxLayout()

        # 添加输入框
        self.input_lineEdit = QLineEdit()
        self.input_lineEdit.setPlaceholderText("请输入内容...")
        layout.addWidget(self.input_lineEdit)

        # 添加按钮组
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class SpecificationDialog(QDialog):
    def __init__(self, parent=None, title="输入数据"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(320, 188)

        # 设置布局
        layout = QVBoxLayout()

        # 添加输入框
        self.input_lineEdit_uint = QLineEdit()
        self.input_lineEdit_uint.setPlaceholderText("请输入包装单位")
        self.input_lineEdit_quan = QLineEdit()
        self.input_lineEdit_quan.setPlaceholderText("请输入包装数量")
        layout.addWidget(self.input_lineEdit_uint)
        layout.addWidget(self.input_lineEdit_quan)

        # 添加按钮组
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


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


# 类别属性页面
class DrugAttributePage(QDialog, Ui_class_dialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.db = parent.db
        self.bind_event()
        self.get_drug_attribute_model()

    def bind_event(self):
        self.add_btn.clicked.connect(self.add_drug_attribute)
        self.refresh_btn.clicked.connect(self.get_drug_attribute_model)

    def add_drug_attribute(self):
        dialog = PopupDialog(self, "输入药品分类")
        if dialog.exec() == QDialog.DialogCode.Accepted:
            input_text = dialog.input_lineEdit.text()
            query = QSqlQuery()
            query.prepare("INSERT INTO MedicineCategories (category_name) VALUES (?)")
            query.addBindValue(input_text)
            if not query.exec():
                QMessageBox.critical(self, "数据库错误", f"添加分类失败: {query.lastError().text()}")
            else:
                QMessageBox.information(self, "成功", "分类添加成功")
                print(f"输入药品属性: {input_text}")

    def get_drug_attribute_model(self):
        self.drug_attribute_model = MedicineCategoriesModel(self, self.db)
        self.class_set_tableView.setModel(self.drug_attribute_model)
        for col in self.drug_attribute_model.hidden_columns:
            self.class_set_tableView.hideColumn(col)
        return self.drug_attribute_model


# 药品剂型
class DrugRormulationPage(QDialog, Ui_RormuDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.db = parent.db
        self.bind_event()
        self.get_drug_rormulateon_model()

    def get_drug_rormulateon_model(self):
        self.drug_rormulateon = DrugRormulationModel(self, self.db)
        self.rormulation_set_tableView.setModel(self.drug_rormulateon)
        for col in self.drug_rormulateon.hidden_columns:
            self.rormulation_set_tableView.hideColumn(col)
        return self.drug_rormulateon

    def bind_event(self):
        self.add_btn.clicked.connect(self.add_drug_rormulateon)
        self.refresh_btn.clicked.connect(self.get_drug_rormulateon_model)

    def add_drug_rormulateon(self):
        dialog = PopupDialog(self, "输入药品剂型")
        if dialog.exec() == QDialog.DialogCode.Accepted:
            input_text = dialog.input_lineEdit.text()
            query = QSqlQuery()
            query.prepare("INSERT INTO drug_formulation (formulation_name) VALUES (?)")
            query.addBindValue(input_text)

            if not query.exec():
                QMessageBox.critical(self, "数据库错误", f"添加剂型失败: {query.lastError().text()}")
            else:
                QMessageBox.information(self, "成功", "剂型添加成功")
                print(f"输入药品剂型: {input_text}")


class DrugUnitPage(QDialog, Ui_UnitDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.db = parent.db
        self.bind_event()
        self.get_drug_unit_model()

    def get_drug_unit_model(self):
        self.drug_unit = DrugUnitModel(self, self.db)
        self.unit_set_tableView.setModel(self.drug_unit)
        for col in self.drug_unit.hidden_columns:
            self.unit_set_tableView.hideColumn(col)
        return self.drug_unit

    def bind_event(self):
        self.add_btn.clicked.connect(self.add_drug_unit)
        self.refresh_btn.clicked.connect(self.get_drug_unit_model)

    def add_drug_unit(self):
        dialog = PopupDialog(self, "输入药品单位")
        if dialog.exec() == QDialog.DialogCode.Accepted:
            input_text = dialog.input_lineEdit.text()
            query = QSqlQuery()
            query.prepare("INSERT INTO drug_unit (unit_name) VALUES (?)")
            query.addBindValue(input_text)
            if not query.exec():
                QMessageBox.critical(self, "数据库错误", f"添加单位失败: {query.lastError().text()}")
            else:
                QMessageBox.information(self, "成功", "单位添加成功")
                print(f"输入药品单位: {input_text}")


class DrugSpecificationPage(QDialog, Ui_SpecificationDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.db = parent.db
        self.bind_event()
        self.get_drug_specification_model()

    def get_drug_specification_model(self):
        self.drug_specification = SpecificationModel(self, self.db)
        self.specification_tableView.setModel(self.drug_specification)
        for col in self.drug_specification.hidden_columns:
            self.specification_tableView.hideColumn(col)
        return self.drug_specification

    def bind_event(self):
        self.add_btn.clicked.connect(self.add_drug_specification)
        self.refresh_btn.clicked.connect(self.get_drug_specification_model)

    def add_drug_specification(self):
        dialog = SpecificationDialog(self, "输入药品规格")
        if dialog.exec_() == QDialog.DialogCode.Accepted:
            input_uint = dialog.input_lineEdit_uint.text()
            input_quan = dialog.input_lineEdit_quan.text()
            query = QSqlQuery()
            query.prepare("INSERT INTO Specification (packaging_quantity, packaging_unit) VALUES (?, ?)")
            query.addBindValue(input_quan)
            query.addBindValue(input_uint)
            if not query.exec():
                QMessageBox.critical(self, "数据库错误", f"添加规格失败: {query.lastError().text()}")
            else:
                QMessageBox.information(self, "成功", "规格添加成功")

            print(f"输入包装单位: {input_uint}，输入包装数量: {input_quan}")


def calss_page(self):
    self.drug_spec = SpecificationModel(self, self.db)
    self.spec_table_view.setModel(self.drug_spec)
    for col in self.drug_spec.hidden_columns:
        self.spec_table_view.hideColumn(col)

    self.drug_attr = MedicineCategoriesModel(self, self.db)
    self.drug_attr_table_view.setModel(self.drug_attr)
    for col in self.drug_attr.hidden_columns:
        self.drug_attr_table_view.hideColumn(col)

    self.drug_units = DrugUnitModel(self, self.db)
    self.unit_table_view.setModel(self.drug_units)
    for col in self.drug_units.hidden_columns:
        self.unit_table_view.hideColumn(col)


    self.drug_ror = DrugRormulationModel(self, self.db)
    self.dosage_table_view.setModel(self.drug_ror)
    for col in self.drug_ror.hidden_columns:
        self.dosage_table_view.hideColumn(col)

    return self.drug_spec, self.drug_attr, self.drug_units, self.drug_ror
