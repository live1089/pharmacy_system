import random

from PySide6.QtCore import QDate, QDateTime
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox

from ui_app.drug_purchase_add_ui import Ui_PurchaseDialog
from ui_app.add_an_order_ui import Ui_AnOrderDialog


class PurAddPage(QDialog, Ui_PurchaseDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.detail_id = None  # 用于存储编辑模式下的订单ID
        self.bind_event()
        self.load_purchase_data()

    def bind_event(self):
        self.purchase_save_btn.clicked.connect(self.save)

    def load_purchase_data(self):
        query = QSqlQuery("SELECT dic_id, trade_name FROM medicine_dic")
        while query.next():
            drug_id = query.value(0)
            drug_name = query.value(1)
            self.drug_purchase_combox.addItem(drug_name, drug_id)
        query = QSqlQuery("SELECT order_id, order_number FROM purchase_order")
        while query.next():
            order_id = query.value(0)
            order_number = query.value(1)
            self.order_number_combox.addItem(order_number, order_id)

    def load_order_data(self, detail_id):
        """加载现有订单数据用于编辑"""
        self.order_id = detail_id
        self.purchase_save_btn.setText("更新订单")  # 修改按钮文本

        # 查询订单明细信息（这里假设一个订单只对应一个药品，实际情况可能需要调整）
        detail_query = QSqlQuery()
        detail_query.prepare("""
            SELECT order_id, medicine_id, quantity, purchase_total_price, purchase_price, remarks
            FROM purchase_detail
            WHERE purchase_detail.detail_id = ?
        """)
        detail_query.addBindValue(detail_id)
        if detail_query.exec() and detail_query.next():
            order_number = detail_query.value(0)
            medicine_id = detail_query.value(1)
            quantity = detail_query.value(2)
            purchase_total_price = detail_query.value(3)
            purchase_price = detail_query.value(4)
            remarks = detail_query.value(5)

            # 设置明细数据
            # index = self.order_number_combox.findData(order_number)
            # if index >= 0:
            #     self.order_number_combox.setCurrentIndex(index)
            if order_number is not None:
                index = self.order_number_combox.findData(order_number)
                if index >= 0:
                    self.order_number_combox.setCurrentIndex(index)
                else:
                    # 如果 order_id 不存在于组合框选项中（可能已被删除），则设置为空
                    self.order_number_combox.setCurrentIndex(-1)
            else:
                self.order_number_combox.setCurrentIndex(-1)  # 设置为无选择状态
            index = self.drug_purchase_combox.findData(medicine_id)
            if index >= 0:
                self.drug_purchase_combox.setCurrentIndex(index)
            self.quantity_purchased_spin_box.setValue(quantity)
            self.total_amount_order_double.setValue(purchase_total_price)
            self.purchase_unit_price_double.setValue(purchase_price)
            self.purchase_notes_plain_text.setPlainText(remarks if remarks is not None else "")

    def save(self):
        if self.detail_id:  # 编辑模式
            self.update_order()
        else:  # 新增模式
            self.create_order()

    def create_order(self):
        """创建药品采购单"""
        drug = self.drug_purchase_combox.itemData(self.drug_purchase_combox.currentIndex())  # 药品
        order_number = self.order_number_combox.itemData(self.order_number_combox.currentIndex())  # 订单号
        quantity_purchased = self.quantity_purchased_spin_box.value()  # 购买数量
        total_amount = self.total_amount_order_double.value()  # 采购总价
        purchase_unit_price = self.purchase_unit_price_double.value()  # 采购单价
        purchase_notes = self.purchase_notes_plain_text.toPlainText()  # 备注

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            # 采购明细表
            query.prepare(
                "INSERT INTO purchase_detail(order_id, medicine_id, quantity, purchase_total_price, purchase_price, remarks) "
                "VALUES (?,?,?,?,?,?)")
            query.addBindValue(order_number)
            query.addBindValue(drug)
            query.addBindValue(quantity_purchased)
            query.addBindValue(total_amount)
            query.addBindValue(purchase_unit_price)
            query.addBindValue(purchase_notes)

            if not query.exec():
                raise Exception(f"添加失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "添加成功")
            self.accept()  # 关闭对话框

        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))

    def update_order(self):
        """更新现有订单"""
        drug = self.drug_purchase_combox.itemData(self.drug_purchase_combox.currentIndex())  # 药品
        order_number = self.order_number_combox.itemData(self.order_number_combox.currentIndex())  # 订单号
        quantity_purchased = self.quantity_purchased_spin_box.value()  # 购买数量
        total_amount = self.total_amount_order_double.value()  # 采购总价
        purchase_unit_price = self.purchase_unit_price_double.value()  # 采购单价
        purchase_notes = self.purchase_notes_plain_text.toPlainText()  # 备注

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            # 更新采购明细表（假设一个订单只有一条明细）
            query.prepare("""
                UPDATE purchase_detail 
                SET order_id=?, medicine_id=?, quantity=?, purchase_total_price=?, purchase_price=?, remarks=?
                WHERE purchase_detail.detail_id=?
            """)
            query.addBindValue(order_number)
            query.addBindValue(drug)
            query.addBindValue(quantity_purchased)
            query.addBindValue(total_amount)
            query.addBindValue(purchase_unit_price)
            query.addBindValue(purchase_notes)
            query.addBindValue(self.detail_id)

            if not query.exec():
                raise Exception(f"更新失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "更新成功")
            self.accept()  # 关闭对话框

        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))


class AnOrderPage(QDialog, Ui_AnOrderDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.order_id = None
        self.bind_event()
        self.load_an_order_data()

    def bind_event(self):
        self.order_save_btn.clicked.connect(self.save)

    # 加载要更新的订单信息
    def load_order(self, order_id):
        self.order_id = order_id
        self.order_save_btn.setText("更新订单")

        # 查询订单主表信息
        query = QSqlQuery()
        query.prepare("""
                    SELECT purchase_order.order_number, supplier_id, order_date, expected_delivery_date, total_amount, remarks
                    FROM purchase_order
                    WHERE order_id = ?
                """)
        query.addBindValue(order_id)
        if query.exec() and query.next():
            order_number = query.value(0)
            supplier = query.value(1)
            order_date = query.value(2)
            expected_delivery_date = query.value(3)
            total_amount = query.value(4)
            remarks = query.value(5)

            # 设置界面数据
            # self.lineEdit.setText(order_number)
            # self.supplier_order_comboBox.setCurrentText(str(supplier))
            # date_obj = QDate.fromString(order_date, "yyyy-MM-dd")
            # self.down_order_dateEdit.setDate(date_obj)
            # date_obj = QDate.fromString(expected_delivery_date, "yyyy-MM-dd")
            # self.up_googs_dateEdit.setDate(date_obj)
            # self.doubleSpinBox.setValue(total_amount)
            # self.plainTextEdit.setPlainText(remarks)
            # 设置界面数据
            self.lineEdit.setText(order_number if order_number is not None else "")
            self.supplier_order_comboBox.setCurrentText(str(supplier) if supplier is not None else "")
            date_obj = QDate.fromString(order_date, "yyyy-MM-dd") if order_date else QDate.currentDate()
            self.down_order_dateEdit.setDate(date_obj)
            date_obj = QDate.fromString(expected_delivery_date,
                                        "yyyy-MM-dd") if expected_delivery_date else QDate.currentDate()
            self.up_googs_dateEdit.setDate(date_obj)
            self.doubleSpinBox.setValue(total_amount if total_amount is not None else 0.0)
            self.plainTextEdit.setPlainText(remarks if remarks is not None else "")

    def save(self, /):
        if self.order_id:
            self.update_order()
        else:
            self.create_order()

    def load_an_order_data(self):
        self.down_order_dateEdit.setDate(QDate.currentDate())
        self.up_googs_dateEdit.setDate(QDate.currentDate())

        query = QSqlQuery("SELECT supplier_id, name FROM supplier")
        while query.next():
            ids = query.value(0)
            name = query.value(1)
            self.supplier_order_comboBox.addItem(name, ids)

        timestamp = QDateTime.currentDateTime().toString("yyyyMMddHHmmss")
        random_num = random.randint(1, 9999)
        self.lineEdit.setText(f"PO-{timestamp}-{random_num}")

    def create_order(self):
        order_date = self.down_order_dateEdit.dateTime().toString("yyyy-MM-dd")  # 下单日期
        estimated_delivery_date = self.up_googs_dateEdit.dateTime().toString("yyyy-MM-dd")  # 交货日期
        supplier = self.supplier_order_comboBox.itemData(self.supplier_order_comboBox.currentIndex())  # 供应商
        order_number = self.lineEdit.text() # 订单编号
        total_purchase_price = self.doubleSpinBox.value() # 采购总价
        remarks = self.plainTextEdit.toPlainText()  # 备注

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            query.prepare(
                "INSERT INTO purchase_order(supplier_id, order_number, order_date, expected_delivery_date, total_amount,  remarks)"
                "VALUES (?,?,?,?,?,?)")
            query.addBindValue(supplier)
            query.addBindValue(order_number)
            query.addBindValue(order_date)
            query.addBindValue(estimated_delivery_date)
            query.addBindValue(total_purchase_price)
            query.addBindValue(remarks)

            if not query.exec():
                raise Exception(f"添加失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")
            QMessageBox.information(self, "成功", "添加成功")
            self.accept()  # 关闭对话框

        except Exception as e:
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))

    def update_order(self):
        order_date = self.down_order_dateEdit.dateTime().toString("yyyy-MM-dd")  # 下单日期
        estimated_delivery_date = self.up_googs_dateEdit.dateTime().toString("yyyy-MM-dd")  # 交货日期
        supplier = self.supplier_order_comboBox.itemData(self.supplier_order_comboBox.currentIndex())  # 供应商
        order_number = self.lineEdit.text() # 订单编号
        total_purchase_price = self.doubleSpinBox.value() # 采购总价
        remarks = self.plainTextEdit.toPlainText()  # 备注

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            query.prepare(
                "UPDATE purchase_order SET order_number = ?, supplier_id=?, order_date=?, expected_delivery_date=?, total_amount=?, remarks=? "
                "WHERE order_id=?")
            query.addBindValue(order_number)
            query.addBindValue(supplier)
            query.addBindValue(order_date)
            query.addBindValue(estimated_delivery_date)
            query.addBindValue(total_purchase_price)
            query.addBindValue(remarks)
            query.addBindValue(self.order_id)
            if not query.exec():
                raise Exception(f"更新失败: {query.lastError().text()}")
            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")
            QMessageBox.information(self, "成功", "更新成功")
            self.accept()  # 关闭对话框
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
