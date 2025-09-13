import random

from PySide6.QtCore import QDateTime, QDate, Qt
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox, QVBoxLayout, QLineEdit, QDialogButtonBox

from data.sqlite_data import StockLocationModel, StockAllModel, shelves_stock_model
from page_window.medicines_page import delete_selected_rows
from page_window.tools import install_enter_key_filter
from ui_app.stock_in_page_ui import Ui_StockDialog
from ui_app.stock_locaton_ui import Ui_StockLocationDialog
from ui_app.stock_all_ui import Ui_StockInAllDialog


class StockMedicinesPage(QDialog, Ui_StockDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.stock_in_id = None
        self.bind_event()
        self.load_stock_data()
        self.ignore_cargo_return()

    def ignore_cargo_return(self):
        install_enter_key_filter(self.purchase_order_combox)
        install_enter_key_filter(self.Invoice_line_edit)
        install_enter_key_filter(self.Production_lot_number_line_edit)
        install_enter_key_filter(self.stock_drug_combox)
        install_enter_key_filter(self.incoming_quantity_spin_box)
        install_enter_key_filter(self.inbound_amount_double)
        install_enter_key_filter(self.valid_date_edit)
        install_enter_key_filter(self.actual_incoming_quantity_spin_box)
        install_enter_key_filter(self.inbound_date_time_edit)
        install_enter_key_filter(self.location_combox)
        install_enter_key_filter(self.warehousing_remarks_plain_text_edit)
        install_enter_key_filter(self.batch_lineEdit)

    def bind_event(self):
        self.stock_save_btn.clicked.connect(self.save)
        self.purchase_order_combox.currentIndexChanged.connect(self.purchase_of_stock_in_drug)
        self.stock_drug_combox.currentIndexChanged.connect(self.load_drugs_by_order)

    def purchase_of_stock_in_drug(self, index):
        if index >= 0:
            purchase_order_id = self.purchase_order_combox.itemData(index)
            self.load_stock_in_drug(purchase_order_id)

    def load_stock_in_drug(self, purchase_order_id):
        self.stock_drug_combox.clear()

        # 如果采购订单ID有效，则查询对应的药品信息
        if purchase_order_id is not None:
            query = QSqlQuery()
            query.prepare("""
                SELECT pd.detail_id, md.trade_name
                FROM purchase_detail pd
                JOIN medicine_dic md ON md.dic_id = pd.medicine_id
                WHERE pd.order_id = ?
            """)
            query.addBindValue(purchase_order_id)

            if query.exec():
                while query.next():
                    detail_id = query.value(0)
                    drug_name = query.value(1)
                    self.stock_drug_combox.addItem(drug_name, detail_id)
            else:
                print(f"数据库查询错误: {query.lastError().text()}")

    def load_drugs_by_order(self, index):
        if index >= 0:
            detail_id = self.stock_drug_combox.itemData(index)
            self.incoming_quantity(detail_id)

    def incoming_quantity(self, detail_id):
        """
        根据采购明细ID获取采购数量和总价，并更新界面控件
        """
        if detail_id is not None:
            query = QSqlQuery()
            query.prepare("""
                SELECT pd.quantity, pd.purchase_total_price
                FROM purchase_detail pd
                WHERE pd.detail_id = ?
            """)
            query.addBindValue(detail_id)

            if query.exec() and query.next():
                quantity = query.value(0) or 0
                total_price = query.value(1) or 0.0

                # 更新入库数量为采购数量
                self.incoming_quantity_spin_box.setValue(quantity)

                # 更新入库金额为采购总价
                self.inbound_amount_double.setValue(total_price)
            else:
                # 如果查询失败或无结果，重置为默认值
                self.incoming_quantity_spin_box.setValue(0)
                self.inbound_amount_double.setValue(0.0)
                if not query.exec():
                    print(f"数据库查询错误: {query.lastError().text()}")

    def save(self):
        if self.stock_in_id:  # 编辑模式
            self.update_stock_in()
        else:  # 新增模式
            self.create_stock_in()

    def create_stock_in(self):
        purchase_order = self.purchase_order_combox.itemData(self.purchase_order_combox.currentIndex())  # 采购订单ID
        invoice_number = self.Invoice_line_edit.text()  # 发票号
        manufacturer_batch = self.Production_lot_number_line_edit.text()  # 生产批号
        purchase_detail_id = self.stock_drug_combox.itemData(self.stock_drug_combox.currentIndex())  # 采购明细ID
        stock_num = self.incoming_quantity_spin_box.value()  # 获取入库数量
        actual_warehousing_quantity = self.actual_incoming_quantity_spin_box.value()  # 获取实际入库数量
        inbound_date = self.inbound_date_time_edit.dateTime().toString("yyyy-MM-dd hh:mm:ss")  # 获取入库时间
        operator = self.operator_combox.itemData(self.operator_combox.currentIndex())  # 获取操作员
        inbound_amount = self.inbound_amount_double.value()  # 获取入库金额
        validity = self.valid_date_edit.date().toString("yyyy-MM-dd")
        remarks = self.warehousing_remarks_plain_text_edit.toPlainText()  # 入库备注
        location = self.location_combox.itemData(self.location_combox.currentIndex())
        batch_number = self.batch_lineEdit.text()  # 批次

        # 输入校验
        if not all([purchase_order, invoice_number, purchase_detail_id]):
            QMessageBox.warning(self, "输入错误", "请填写所有必填项。")
            return

        if stock_num <= 0 or actual_warehousing_quantity < 0 or inbound_amount <= 0:
            QMessageBox.warning(self, "输入错误", "数量和金额必须大于0。")
            return

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            query.prepare(
                "Insert into stock_in_main(order_id, in_date, operator_id, total_amount, invoice_number, batch, production_lot_number, validity, remarks) "
                "values (?,?,?,?,?,?,?,?,?)")
            query.addBindValue(purchase_order)
            query.addBindValue(inbound_date)
            query.addBindValue(operator)
            query.addBindValue(inbound_amount)
            query.addBindValue(invoice_number)
            query.addBindValue(batch_number)
            query.addBindValue(manufacturer_batch)
            query.addBindValue(validity)
            query.addBindValue(remarks)
            if not query.exec():
                raise Exception(f"添加入库主表失败: {query.lastError().text()}")

            # 获取刚插入的入库单ID
            in_id = query.lastInsertId()

            query.prepare(
                "Insert into stock_in_detail(in_id, purchase_detail_id, quantity, actual_quantity,warehouse_shelf_id) "
                "values (?,?,?,?,?)")
            query.addBindValue(in_id)
            query.addBindValue(purchase_detail_id)
            query.addBindValue(stock_num)
            query.addBindValue(actual_warehousing_quantity)
            query.addBindValue(location)

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

    def load_stock_data(self):
        batch_number = f"IN-BN{QDate.currentDate().toString('yyyyMMdd')}-{random.Random().randint(1000, 9999)}"
        self.batch_lineEdit.setText(batch_number)
        self.inbound_date_time_edit.setDateTime(QDateTime.currentDateTime())
        self.valid_date_edit.setDate(QDate.currentDate())
        query = QSqlQuery("SELECT order_id, order_number FROM purchase_order ORDER BY order_id DESC")
        while query.next():
            order_id = query.value(0)
            order_number = query.value(1)
            self.purchase_order_combox.addItem(order_number, order_id)

        query = QSqlQuery("SELECT users_id, username FROM users")
        while query.next():
            operator_id = query.value(0)
            operator_name = query.value(1)
            self.operator_combox.addItem(operator_name, operator_id)

        query = QSqlQuery("SELECT warehouse_shelf_id, location FROM warehouse_shelf_position")
        while query.next():
            location_id = query.value(0)
            location_name = query.value(1)
            self.location_combox.addItem(location_name, location_id)

    def load_order_data(self, stock_in_id):
        self.stock_in_id = stock_in_id
        self.stock_save_btn.setText("更新入库")

        # 查询主表信息
        stock_in_query = QSqlQuery()
        stock_in_query.prepare("""
            SELECT order_id, in_date, operator_id, total_amount, invoice_number, batch, production_lot_number, validity, remarks
            FROM stock_in_main
            WHERE stock_in_main.in_id = ?
        """)
        stock_in_query.addBindValue(stock_in_id)

        order = None
        in_data = None
        operator = None
        total_amount = 0.0
        invoice_number = ""
        batch = ""
        production_lot_number = ""
        validity = None
        remarks = ""

        if stock_in_query.exec() and stock_in_query.next():
            order = stock_in_query.value(0)
            in_data = stock_in_query.value(1)
            operator = stock_in_query.value(2)
            total_amount = stock_in_query.value(3) or 0.0
            invoice_number = stock_in_query.value(4) or ""
            batch = stock_in_query.value(5) or ""
            production_lot_number = stock_in_query.value(6) or ""
            validity = stock_in_query.value(7)
            remarks = stock_in_query.value(8) or ""

        # 设置采购订单下拉框
        if order is not None:
            index = self.purchase_order_combox.findData(order)
            if index >= 0:
                self.purchase_order_combox.setCurrentIndex(index)
            else:
                self.purchase_order_combox.setCurrentIndex(-1)
        else:
            self.purchase_order_combox.setCurrentIndex(-1)

        # 设置其他控件值
        # self.inbound_date_time_edit.setDateTime(in_data if in_data else QDateTime.currentDateTime())
        # 确保传入的是QDateTime类型
        datetime_value = QDateTime.currentDateTime()  # 默认值
        if in_data:
            if isinstance(in_data, str):
                datetime_value = QDateTime.fromString(in_data, "yyyy-MM-dd hh:mm:ss")
            else:
                datetime_value = in_data
        self.inbound_date_time_edit.setDateTime(datetime_value)
        self.operator_combox.setCurrentText(str(operator) or "")
        self.inbound_amount_double.setValue(total_amount)
        self.Invoice_line_edit.setText(invoice_number)
        self.batch_lineEdit.setText(batch)
        self.Production_lot_number_line_edit.setText(str(production_lot_number))
        validity_value = QDate.currentDate()
        if validity:
            if isinstance(validity, str):
                validity_value = QDate.fromString(validity, "yyyy-MM-dd")
            else:
                validity_value = validity
        self.valid_date_edit.setDate(validity_value)
        self.warehousing_remarks_plain_text_edit.setPlainText(remarks)

        # 查询明细表信息
        detail_query = QSqlQuery()
        detail_query.prepare("""
            SELECT quantity, actual_quantity, warehouse_shelf_id
            FROM stock_in_detail
            WHERE stock_in_detail.detail_id = ?
        """)
        detail_query.addBindValue(stock_in_id)

        quantity = 0
        actual_quant = 0
        location = ""

        if detail_query.exec() and detail_query.next():
            quantity = detail_query.value(0) or 0
            actual_quant = detail_query.value(1) or 0
            location = detail_query.value(2) or ""

        self.incoming_quantity_spin_box.setValue(quantity)
        self.actual_incoming_quantity_spin_box.setValue(actual_quant)
        self.location_combox.itemData(self.location_combox.currentIndex())

    def update_stock_in(self):
        # 获取界面输入数据
        purchase_order = self.purchase_order_combox.itemData(self.purchase_order_combox.currentIndex())
        invoice_number = self.Invoice_line_edit.text()  # 获取发票号
        batch = self.batch_lineEdit.text()  # 获取批号
        manufacturer_batch = self.Production_lot_number_line_edit.text()
        purchase_detail_id = self.stock_drug_combox.itemData(self.stock_drug_combox.currentIndex())
        stock_num = self.incoming_quantity_spin_box.value()
        actual_warehousing_quantity = self.actual_incoming_quantity_spin_box.value()
        inbound_date = self.inbound_date_time_edit.dateTime().toString("yyyy-MM-dd hh:mm:ss")  # 获取入库时间
        operator = self.operator_combox.itemData(self.operator_combox.currentIndex())  # 获取操作员
        inbound_amount = self.inbound_amount_double.value()  # 获取入库金额
        validity = self.valid_date_edit.date().toString("yyyy-MM-dd")
        remarks = self.warehousing_remarks_plain_text_edit.toPlainText()  # 入库备注
        location = self.location_combox.itemData(self.location_combox.currentIndex())

        # 输入校验
        if not all([purchase_order, invoice_number, batch, purchase_detail_id, operator]):
            QMessageBox.warning(self, "输入错误", "请填写所有必填项。")
            return

        if stock_num < 0 or actual_warehousing_quantity < 0 or inbound_amount < 0:
            QMessageBox.warning(self, "输入错误", "数量和金额必须大于等于0。")
            return

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        try:
            if not query.exec("BEGIN"):
                raise Exception(f"无法开始事务: {query.lastError().text()}")

            # 更新主表
            query.prepare("""
                UPDATE stock_in_main 
                SET order_id=?, in_date=?, operator_id=?, total_amount=?, invoice_number=?, batch=?, production_lot_number=?, validity=?, remarks=?
                WHERE order_id = ?
            """)
            query.addBindValue(purchase_order)
            query.addBindValue(inbound_date)
            query.addBindValue(operator)
            query.addBindValue(inbound_amount)
            query.addBindValue(invoice_number)
            query.addBindValue(batch)
            query.addBindValue(manufacturer_batch)
            query.addBindValue(validity)
            query.addBindValue(remarks)
            query.addBindValue(purchase_order)  # WHERE 条件中的 order_id

            if not query.exec():
                raise Exception(f"更新主表失败: {query.lastError().text()}")

            if query.numRowsAffected() == 0:
                raise Exception("未找到对应的入库单进行更新")

            # 更新明细表 - 使用正确的detail_id
            # 首先获取当前的detail_id
            detail_query = QSqlQuery()
            detail_query.prepare("SELECT detail_id FROM stock_in_detail WHERE in_id = ?")
            detail_query.addBindValue(self.stock_in_id)

            detail_id = None
            if detail_query.exec() and detail_query.next():
                detail_id = detail_query.value(0)

            if detail_id is None:
                raise Exception("未找到对应的入库明细记录")

            query.prepare("""
                UPDATE stock_in_detail 
                SET purchase_detail_id=?, quantity=?, actual_quantity=?, warehouse_shelf_id=? 
                WHERE detail_id = ?
            """)
            query.addBindValue(purchase_detail_id)
            query.addBindValue(stock_num)
            query.addBindValue(actual_warehousing_quantity)
            query.addBindValue(location)
            query.addBindValue(detail_id)

            if not query.exec():
                raise Exception(f"更新明细表失败: {query.lastError().text()}")

            if query.numRowsAffected() == 0:
                raise Exception("未找到对应的入库明细进行更新")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "更新成功")
            self.accept()  # 关闭对话框

        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
        finally:
            # 显式清理资源
            query.finish()


class StockLocationPage(QDialog, Ui_StockLocationDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.db = parent.db
        self.bind_event()
        self.get_stock_location_model()

    def get_stock_location_model(self):
        self.stock_location = StockLocationModel(self, self.db)
        self.stock_set_tableView.setModel(self.stock_location)
        for col in self.stock_location.hidden_columns:
            self.stock_set_tableView.hideColumn(col)
        return self.stock_location

    def bind_event(self):
        self.add_btn.clicked.connect(self.add_location)
        self.refresh_btn.clicked.connect(self.get_stock_location_model)
        self.del_btn.clicked.connect(self.delete_selected_row)

    def add_location(self):
        dialog = PopupDialog(self, "输入存储位置")
        if dialog.exec() == QDialog.DialogCode.Accepted:
            input_text = dialog.input_lineEdit.text()
            query = QSqlQuery()
            query.prepare("INSERT INTO warehouse_shelf_position (location) VALUES (?)")
            query.addBindValue(input_text)

            if not query.exec():
                QMessageBox.critical(self, "数据库错误", f"添加失败: {query.lastError().text()}")
            else:
                QMessageBox.information(self, "成功", "添加成功")
                self.get_stock_location_model()

    def delete_selected_row(self):
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.stock_set_tableView,
            model=self.stock_location,  # 您的BaseTableModel实例
            db=self.db,  # QSqlDatabase实例
            parent=self  # 父窗口
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            self.get_stock_location_model()
            # 可选：清除选择
            self.stock_set_tableView.clearSelection()
        else:
            QMessageBox.critical(self, "错误", msg, QMessageBox.StandardButton.Ok)


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


class StockInAllPage(QDialog, Ui_StockInAllDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.db = parent.db
        self.bind_event()
        self.get_stock_in_all_model()
        self.get_shelves_stock_model()

    def bind_event(self):
        pass

    def get_shelves_stock_model(self):
        """获取上架药品库存模型并设置到表格视图"""
        model = shelves_stock_model(self.ui)  # 使用主窗口的数据库连接
        self.shelves_stock_tableView.setModel(model)

        # 设置表头
        model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "出库单号")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "出库批次")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "药品名称")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "上架数量")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "上架位置")
        model.setHeaderData(6, Qt.Orientation.Horizontal, "库存批次")
        model.setHeaderData(7, Qt.Orientation.Horizontal, "有效期")

        # 隐藏ID列
        self.shelves_stock_tableView.hideColumn(0)

        return model

    def get_stock_in_all_model(self):
        self.stock_all = StockAllModel(self, self.db)
        sql = f"""
            SELECT
                s.stock_id,
                dic.trade_name,
                us.batch,
                ud.location,
                s.quantity,
                s.last_update,
                us.validity as 有效期,
                us.production_lot_number as 生产批号
            FROM stock s
            LEFT JOIN stock_in_main us ON us.in_id = s.batch
            LEFT JOIN warehouse_shelf_position ud ON ud.warehouse_shelf_id = s.location
            LEFT JOIN medicine_dic dic ON dic.dic_id = s.drug_id
        """
        self.stock_all.setQuery(sql, self.db)
        self.stock_all_tableView.setModel(self.stock_all)
        for col in self.stock_all.hidden_columns:
            self.stock_all_tableView.hideColumn(col)
        return self.stock_all
