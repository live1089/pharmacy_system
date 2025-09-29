from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox, QLineEdit, QDialog, QDialogButtonBox, QVBoxLayout

from data.sqlite_data import MedicineCategoriesModel, DrugRormulationModel, DrugUnitModel, SpecificationModel
from ui_app.drug_add_ui import Ui_Dialog
from ui_app.drug_attribute_ui import Ui_class_dialog
from ui_app.drug_rormulation_ui import Ui_RormuDialog
from ui_app.drug_specification_ui import Ui_SpecificationDialog
from ui_app.drug_unit_ui import Ui_UnitDialog


def delete_selected_rows(self, tableView, model, db, parent=None):
    """
    删除表格视图中选中的行（通用函数）

    参数:
        tableView (QTableView): 表格视图实例
        model (BaseTableModel): 数据模型实例
        db (QSqlDatabase): 数据库连接
        parent (QWidget): 父窗口，用于显示对话框

    返回:
        bool: 操作是否成功
        str: 错误消息（成功时为空）
    """
    # 1. 获取选中的行
    selection = tableView.selectionModel().selectedRows()
    if not selection:
        # QMessageBox.warning(parent, "提示", "请先选择要删除的行", QMessageBox.StandardButton.Ok)
        return False, "请先选择要删除的行"

    # 2. 确认对话框
    reply = QMessageBox.question(
        parent,
        "确认删除",
        f"确定要删除选中的 {len(selection)} 行吗？此操作无法撤销！",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )
    if reply == QMessageBox.StandardButton.No:
        return False, "用户取消操作"

    # 3. 获取主键列名
    pk_column = model.get_primary_key_column()
    if not pk_column:
        return False, "无法确定主键列"

    # 4. 收集要删除的主键值
    ids_to_delete = []
    for index in selection:
        row = index.row()
        record = model.record(row)
        pk_value = record.value(pk_column)
        if pk_value is not None:
            ids_to_delete.append(pk_value)

    if not ids_to_delete:
        return False, "无法获取选中行的主键值"

    try:
        # 构建 IN 语句
        placeholders = ", ".join(["?"] * len(ids_to_delete))

        # 构造删除语句
        query = QSqlQuery(db)
        sql = f"DELETE FROM {model.tableName()} WHERE {pk_column} IN ({placeholders})"

        if not query.prepare(sql):
            raise Exception(f"SQL准备失败: {query.lastError().text()}")

        # 绑定参数
        for i, pk_value in enumerate(ids_to_delete):
            query.bindValue(i, pk_value)

        # 执行查询
        if not query.exec():
            raise Exception(f"删除失败: {query.lastError().text()}")

        return True, f"成功删除 {len(ids_to_delete)} 行数据"

    except Exception as e:
        # 回滚事务
        db.rollback()
        return False, str(e)


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


# 药品添加页面
class MedicinesPage(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.load_medicine_combo()
        self.dic_id = None

    def bind_event(self):
        self.drug_add_save_btn.clicked.connect(self.save)

    def load_medicine_combo(self):
        """加载药品到下拉框"""
        self.drug_classify_combox.clear()
        self.pack_combox.clear()
        self.drug_unit_combox.clear()
        self.dosage_combox.clear()

        # 加载药品分类
        query = QSqlQuery("SELECT category_id, category_name FROM MedicineCategories")
        while query.next():
            drug_classify_id = query.value(0)
            drug_classify_name = query.value(1)
            self.drug_classify_combox.addItem(drug_classify_name, drug_classify_id)

        # 加载剂型
        query = QSqlQuery("SELECT formulation_id, formulation_name FROM drug_formulation")
        while query.next():
            drug_dosage_id = query.value(0)
            drug_dosage_name = query.value(1)
            self.dosage_combox.addItem(drug_dosage_name, drug_dosage_id)

        # 加载单位
        query = QSqlQuery("SELECT unit_id, unit_name FROM drug_unit")
        while query.next():
            drug_unit_id = query.value(0)
            drug_unit_name = query.value(1)
            self.drug_unit_combox.addItem(drug_unit_name, drug_unit_id)

        # 加载规格
        query = QSqlQuery("SELECT specification_id, packaging_specifications FROM Specification")
        while query.next():
            spec_id = query.value(0)
            spec_name = query.value(1)
            self.pack_combox.addItem(spec_name, spec_id)

    def save(self):
        if self.dic_id:
            self.update_drug()
        else:
            self.create_drug()

    def load_update_drug_data(self, dic_id):
        self.dic_id = dic_id
        """加载药品信息用于更新"""
        query = QSqlQuery()
        query.prepare("SELECT trade_name, generic_name, specification_id, manufacturer, formulation_id, "
                      "approval_number, category_id, unit_id, price, display_area_threshold, pharmacy_threshold "
                      "FROM medicine_dic "
                      "WHERE dic_id = ?")
        query.addBindValue(dic_id)
        if query.exec() and query.first():
            self.drug_name_line_edit.setText(query.value(0) or "")
            self.generic_name_line_edit.setText(query.value(1) or "")

            # 设置分类下拉框
            category_index = self.drug_classify_combox.findData(query.value(6))
            if category_index >= 0:
                self.drug_classify_combox.setCurrentIndex(category_index)

            # 设置规格下拉框
            spec_index = self.pack_combox.findData(query.value(2))
            if spec_index >= 0:
                self.pack_combox.setCurrentIndex(spec_index)

            # 设置剂型下拉框
            dosage_index = self.dosage_combox.findData(query.value(4))
            if dosage_index >= 0:
                self.dosage_combox.setCurrentIndex(dosage_index)

            # 设置单位下拉框
            unit_index = self.drug_unit_combox.findData(query.value(7))
            if unit_index >= 0:
                self.drug_unit_combox.setCurrentIndex(unit_index)

            self.cmsw_line_edit.setText(query.value(5) or "")
            self.price_line_edit.setText(str(query.value(8) or ""))
            self.manufacturer_line_edit.setText(query.value(3) or "")
            self.display_area_threshold_spinBox.setValue(query.value(9) or 0)
            self.pharmacy_threshold_spinBox.setValue(query.value(10) or 0)

    def update_drug(self):
        """更新药品信息"""
        # 首先验证输入
        if not self.validate_input():
            return

        drug_name = self.drug_name_line_edit.text().strip()
        drug_genre = self.generic_name_line_edit.text().strip()
        drug_class = self.drug_classify_combox.itemData(self.drug_classify_combox.currentIndex())
        drug_pack = self.pack_combox.itemData(self.pack_combox.currentIndex())
        drug_unit = self.drug_unit_combox.itemData(self.drug_unit_combox.currentIndex())
        drug_price = self.price_line_edit.text().strip()
        drug_cmsw = self.cmsw_line_edit.text().strip()
        drug_dosage = self.dosage_combox.itemData(self.dosage_combox.currentIndex())
        drug_manufactur = self.manufacturer_line_edit.text().strip()
        display_area_threshold = self.display_area_threshold_spinBox.value()
        pharmacy_threshold = self.pharmacy_threshold_spinBox.value()

        query = QSqlQuery()
        query.prepare(
            "UPDATE medicine_dic "
            "SET trade_name = ?, generic_name = ?, specification_id = ?, manufacturer = ?, formulation_id = ?, "
            "approval_number = ? ,category_id = ?, unit_id = ?, price = ? , display_area_threshold = ?, pharmacy_threshold = ? "
            "WHERE dic_id = ?"
        )
        query.addBindValue(drug_name)
        query.addBindValue(drug_genre)
        query.addBindValue(drug_pack)
        query.addBindValue(drug_manufactur)
        query.addBindValue(drug_dosage)
        query.addBindValue(drug_cmsw)
        query.addBindValue(drug_class)
        query.addBindValue(drug_unit)
        query.addBindValue(drug_price)
        query.addBindValue(display_area_threshold)
        query.addBindValue(pharmacy_threshold)
        query.addBindValue(self.dic_id)

        if not query.exec():
            QMessageBox.critical(self, "错误", f"更新失败: {query.lastError().text()}")
            return

        QMessageBox.information(self, "成功", "药品信息更新成功")
        self.accept()

    def validate_input(self):
        """验证输入数据"""
        if not self.drug_name_line_edit.text().strip():
            QMessageBox.warning(self, "输入错误", "请输入药品商品名")
            return False

        if not self.generic_name_line_edit.text().strip():
            QMessageBox.warning(self, "输入错误", "请输入药品通用名")
            return False

        if self.drug_classify_combox.currentIndex() < 0:
            QMessageBox.warning(self, "输入错误", "请选择药品分类")
            return False

        if self.pack_combox.currentIndex() < 0:
            QMessageBox.warning(self, "输入错误", "请选择规格")
            return False

        if self.dosage_combox.currentIndex() < 0:
            QMessageBox.warning(self, "输入错误", "请选择剂型")
            return False

        if self.drug_unit_combox.currentIndex() < 0:
            QMessageBox.warning(self, "输入错误", "请选择单位")
            return False

        try:
            price = float(self.price_line_edit.text() or 0)
            if price < 0:
                QMessageBox.warning(self, "输入错误", "价格不能为负数")
                return False
        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的价格")
            return False

        if not self.manufacturer_line_edit.text().strip():
            QMessageBox.warning(self, "输入错误", "请输入生产厂家")
            return False

        return True

    def create_drug(self):
        """保存药品信息"""
        # 验证输入
        if not self.validate_input():
            return
        drug_name = self.drug_name_line_edit.text()
        drug_genre = self.generic_name_line_edit.text()
        drug_class = self.drug_classify_combox.itemData(self.drug_classify_combox.currentIndex())
        drug_pack = self.pack_combox.itemData(self.pack_combox.currentIndex())
        drug_unit = self.drug_unit_combox.itemData(self.drug_unit_combox.currentIndex())
        drug_price = self.price_line_edit.text()
        drug_cmsw = self.cmsw_line_edit.text()
        drug_dosage = self.dosage_combox.itemData(self.dosage_combox.currentIndex())
        drug_manufactur = self.manufacturer_line_edit.text()
        display_area_threshold = self.display_area_threshold_spinBox.value()
        pharmacy_threshold = self.pharmacy_threshold_spinBox.value()

        query = QSqlQuery()

        query.prepare(
            "INSERT INTO medicine_dic (trade_name, generic_name, specification_id, manufacturer, formulation_id, "
            "approval_number ,category_id, unit_id, price, display_area_threshold, pharmacy_threshold)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(drug_name)
        query.addBindValue(drug_genre)
        query.addBindValue(drug_pack)
        query.addBindValue(drug_manufactur)
        query.addBindValue(drug_dosage)
        query.addBindValue(drug_cmsw)
        query.addBindValue(drug_class)
        query.addBindValue(drug_unit)
        query.addBindValue(drug_price)
        query.addBindValue(display_area_threshold)
        query.addBindValue(pharmacy_threshold)
        if not query.exec():
            QMessageBox.critical(self, "数据库错误", f"添加失败: {query.lastError().text()}")
        else:
            QMessageBox.information(self, "成功", "添加成功")
            self.accept()  # 关闭对话框


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
        self.del_btn.clicked.connect(self.delete_selected_row)

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
                self.get_drug_attribute_model()
                print(f"输入药品属性: {input_text}")

    def get_drug_attribute_model(self):
        self.drug_attribute_model = MedicineCategoriesModel(self, self.db)
        self.class_set_tableView.setModel(self.drug_attribute_model)
        for col in self.drug_attribute_model.hidden_columns:
            self.class_set_tableView.hideColumn(col)
        return self.drug_attribute_model

    def delete_selected_row(self):
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.class_set_tableView,
            model=self.drug_attribute_model,  # 您的BaseTableModel实例
            db=self.db,  # QSqlDatabase实例
            parent=self  # 父窗口
        )

        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            self.get_drug_attribute_model()
            # 可选：清除选择
            self.class_set_tableView.clearSelection()
        else:
            QMessageBox.critical(self, "错误", msg, QMessageBox.StandardButton.Ok)


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
        self.del_btn.clicked.connect(self.delete_selected_row)

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
                self.get_drug_rormulateon_model()
                print(f"输入药品剂型: {input_text}")

    def delete_selected_row(self):
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.rormulation_set_tableView,
            model=self.drug_rormulateon,  # 您的BaseTableModel实例
            db=self.db,  # QSqlDatabase实例
            parent=self  # 父窗口
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            self.get_drug_rormulateon_model()
            # 可选：清除选择
            self.rormulation_set_tableView.clearSelection()
        else:
            QMessageBox.critical(self, "错误", msg, QMessageBox.StandardButton.Ok)


# 药品单位
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
        self.del_btn.clicked.connect(self.delete_selected_row)

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
                self.get_drug_unit_model()
                print(f"输入药品单位: {input_text}")

    def delete_selected_row(self):
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.unit_set_tableView,
            model=self.drug_unit,  # 您的BaseTableModel实例
            db=self.db,  # QSqlDatabase实例
            parent=self  # 父窗口
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            self.get_drug_unit_model()
            # 可选：清除选择
            self.unit_set_tableView.clearSelection()
        else:
            QMessageBox.critical(self, "错误", msg, QMessageBox.StandardButton.Ok)


# 药品规格
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
        self.del_btn.clicked.connect(self.delete_selected_row)

    def add_drug_specification(self):
        dialog = PopupDialog(self, "输入药品规格")
        if dialog.exec_() == QDialog.DialogCode.Accepted:
            input_text = dialog.input_lineEdit.text()
            query = QSqlQuery()
            query.prepare("INSERT INTO Specification (packaging_specifications) VALUES (?)")
            query.addBindValue(input_text)
            if not query.exec():
                QMessageBox.critical(self, "数据库错误", f"添加规格失败: {query.lastError().text()}")
            else:
                QMessageBox.information(self, "成功", "规格添加成功")
                self.get_drug_specification_model()
                print(f"输入包装单位: {input_text}")

    def delete_selected_row(self):
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.specification_tableView,
            model=self.drug_specification,  # 您的BaseTableModel实例
            db=self.db,  # QSqlDatabase实例
            parent=self  # 父窗口
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            self.get_drug_specification_model()
            # 可选：清除选择
            self.specification_tableView.clearSelection()
        else:
            QMessageBox.critical(self, "错误", msg, QMessageBox.StandardButton.Ok)


def class_set_page(self):
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
