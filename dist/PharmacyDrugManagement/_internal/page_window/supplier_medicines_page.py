from datetime import datetime

from PySide6.QtCore import QDateTime
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit, QPlainTextEdit, QDateTimeEdit

from page_window.tools import install_enter_key_filter
from ui_app.supplier_drug_ui import Ui_SupDialog


class SupplierDrugPage(QDialog, Ui_SupDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.supplier_id = None
        self.bind_event()
        self.ignore_cargo_return()

    def ignore_cargo_return(self):
        install_enter_key_filter(self.supplier_line_edit)
        install_enter_key_filter(self.update_time)
        install_enter_key_filter(self.contact_line_edit)
        install_enter_key_filter(self.updater_line_edit)
        install_enter_key_filter(self.phone_line_edit)
        install_enter_key_filter(self.create_time)
        install_enter_key_filter(self.creator_line_edit)
        install_enter_key_filter(self.address_line_edit)
        install_enter_key_filter(self.email_line_edit)
        install_enter_key_filter(self.plainTextEdit_remark)

    def bind_event(self):
        self.supplier_save_btn.clicked.connect(self.save)

    def save(self):
        if self.supplier_id:
            self.update_supplier()
        else:
            self.create_supplier()

    def create_supplier(self):
        create_time = self.create_time.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        update_time = self.update_time.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        supp = self.supplier_line_edit.text()
        contact = self.contact_line_edit.text()
        updater = self.updater_line_edit.text()
        creator = self.creator_line_edit.text()
        phone = self.phone_line_edit.text()
        address = self.address_line_edit.text()
        email = self.email_line_edit.text()
        remark = self.plainTextEdit_remark.toPlainText()

        query = QSqlQuery()

        query.prepare(
            "INSERT INTO supplier (name, contact_person, phone, address, email, remarks, update_at, update_by, create_at, created_by)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

        query.addBindValue(supp)
        query.addBindValue(contact)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(email)
        query.addBindValue(remark)
        query.addBindValue(update_time)
        query.addBindValue(updater)
        query.addBindValue(create_time)
        query.addBindValue(creator)
        if not query.exec():
            QMessageBox.critical(self, "数据库错误", f"添加供应商失败: {query.lastError().text()}")
        else:
            QMessageBox.information(self, "成功", "添加供应商成功")

    def update_supplier(self):
        """更新供应商信息"""
        update_time = self.update_time.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        supp = self.supplier_line_edit.text()
        contact = self.contact_line_edit.text()
        updater = self.updater_line_edit.text()
        phone = self.phone_line_edit.text()
        address = self.address_line_edit.text()
        email = self.email_line_edit.text()
        remark = self.plainTextEdit_remark.toPlainText()

        query = QSqlQuery()
        query.prepare("""
                    UPDATE supplier 
                    SET name=?, contact_person=?, phone=?, address=?, email=?, remarks=?, update_at=?, update_by=?
                    WHERE supplier_id=?
                """)

        query.addBindValue(supp)
        query.addBindValue(contact)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(email)
        query.addBindValue(remark)
        query.addBindValue(update_time)
        query.addBindValue(updater)
        query.addBindValue(self.supplier_id)

        if not query.exec():
            QMessageBox.critical(self, "数据库错误", f"更新供应商失败: {query.lastError().text()}")
        else:
            QMessageBox.information(self, "成功", "更新供应商成功")
            self.accept()  # 关闭对话框
    def load_supplier_time(self):
        self.create_time.setDateTime(QDateTime.currentDateTime())
        self.update_time.setDateTime(QDateTime.currentDateTime())

    def show_mod_supplier_data(self, supplier_id):
        """根据供应商ID填充数据到UI控件"""
        # 保存供应商ID用于更新操作
        self.supplier_id = supplier_id

        # 修改保存按钮文本
        self.supplier_save_btn.setText("更新")

        # 使用参数化查询防止SQL注入
        query = QSqlQuery()
        query.prepare("SELECT * FROM supplier WHERE supplier_id = ?")
        query.addBindValue(supplier_id)

        if not query.exec():
            QMessageBox.critical(self, "错误", f"查询失败: {query.lastError().text()}")
            return

        if query.next():
            # 成功查询到数据，填充到对应控件
            self.supplier_line_edit.setText(query.value("name") or "")
            self.contact_line_edit.setText(query.value("contact_person") or "")
            self.phone_line_edit.setText(query.value("phone") or "")
            self.address_line_edit.setText(query.value("address") or "")
            self.email_line_edit.setText(query.value("email") or "")
            self.plainTextEdit_remark.setPlainText(query.value("remarks") or "")

            self.update_time.setDateTime(QDateTime.currentDateTime())

            # 处理创建时间
            create_at = query.value("create_at")
            if create_at:
                if isinstance(create_at, str):
                    qdatetime = QDateTime.fromString(create_at, "yyyy-MM-dd HH:mm:ss")
                    if qdatetime.isValid():
                        self.create_time.setDateTime(qdatetime)
                elif isinstance(create_at, QDateTime):
                    self.create_time.setDateTime(create_at)

            # 如果数据库中有更新人和创建人信息，则使用数据库中的值
            # 否则可以保留用户手动输入的值
            updater = query.value("update_by")
            creator = query.value("created_by")
            if updater:
                self.updater_line_edit.setText(updater)
            if creator:
                self.creator_line_edit.setText(creator)
        else:
            QMessageBox.warning(self, "警告", "未找到对应的供应商记录")



def get_selected_logical_rows(tableView):
    """获取视图中的选中行（逻辑行）"""
    selection_model = tableView.selectionModel()
    if not selection_model:
        return []

    selected_rows = set()
    for index in selection_model.selectedRows():
        if index.isValid():
            selected_rows.add(index.row())

    return sorted(selected_rows)


