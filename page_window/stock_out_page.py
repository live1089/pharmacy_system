from PySide6 import QtCore
from PySide6.QtCore import QDate, QDateTime, Qt, QEvent
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit
import random

from page_window.tools import install_enter_key_filter
from ui_app.stock_out_warehouse_ui import Ui_OutWarehouseMTDialog
from ui_app.stock_out_warehouse_drug_ui import Ui_OutWarehouseDrugDialog


class StockOutPage(QDialog, Ui_OutWarehouseMTDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.out_id = None
        self.load_data()
        self.ignore_cargo_return()

    def ignore_cargo_return(self):
        install_enter_key_filter(self.outbound_number_lineEdit)
        install_enter_key_filter(self.stock_out_total_amount_spinBox)
        install_enter_key_filter(self.stock_out_type_combox)
        install_enter_key_filter(self.stock_out_dateTime)
        install_enter_key_filter(self.stock_out_remark_plainTextEdit)

    def bind_event(self):
        self.out_warehouse_save_btn.clicked.connect(self.save)

    def save(self):
        if self.out_id:
            self.update_stock_out()
        else:
            self.create_stock_out()

    def load_data(self):
        self.stock_out_dateTime.setDateTime(QtCore.QDateTime.currentDateTime())
        # 生成唯一的出库编号
        while True:
            outbound_number = f"ON-{QDate.currentDate().toString('yyyyMMdd')}-{random.randint(1000, 9999)}"
            # 检查该编号是否已存在
            query = QSqlQuery()
            query.prepare("SELECT COUNT(*) FROM stock_out_main WHERE outbound_number = ?")
            query.addBindValue(outbound_number)
            if query.exec():
                query.first()
                if query.value(0) == 0:  # 编号不存在
                    break

        self.outbound_number_lineEdit.setText(outbound_number)
        # 设置出库类型下拉框，同时设置 itemData
        types = ["上架", "调拨", "报损", "退货"]
        for type_name in types:
            self.stock_out_type_combox.addItem(type_name, type_name)  # 第二个参数是 itemData

        query = QSqlQuery("SELECT users_id, username FROM users")
        while query.next():
            operator_id = query.value(0)
            operator_name = query.value(1)
            self.stock_out_operator_combox.addItem(operator_name, operator_id)

    def load_stock_out_data(self, out_id):
        self.out_warehouse_save_btn.setText("更新出库")
        query = QSqlQuery()
        query.prepare("SELECT outbound_number, out_type, out_date, operator_id, total_amount, remarks "
                      "FROM stock_out_main "
                      "WHERE out_id = ?")
        query.addBindValue(out_id)
        if query.exec():
            query.first()
            outbound_number = query.value(0)
            stock_out_type = query.value(1)
            out_date = query.value(2)
            stock_out_operator = query.value(3)
            total_amount = query.value(4)
            stock_out_remark = query.value(5)

            self.outbound_number_lineEdit.setText(outbound_number)
            self.stock_out_type_combox.setCurrentIndex(self.stock_out_type_combox.findData(stock_out_type))
            self.stock_out_operator_combox.setCurrentIndex(self.stock_out_operator_combox.findData(stock_out_operator))
            datetime_value = QDateTime.currentDateTime()  # 默认值
            if out_date:
                if isinstance(out_date, str):
                    datetime_value = QDateTime.fromString(out_date, "yyyy-MM-dd hh:mm:ss")
                else:
                    datetime_value = out_date
            self.stock_out_dateTime.setDateTime(datetime_value)
            self.stock_out_total_amount_spinBox.setValue(total_amount)
            self.stock_out_remark_plainTextEdit.setPlainText(stock_out_remark)

    def update_stock_out(self):
        if not self.out_id:
            QMessageBox.critical(self, "错误", "无法找到要修改的出库单")
            return
        outbound_number = self.outbound_number_lineEdit.text()
        stock_out_type = self.stock_out_type_combox.itemData(self.stock_out_type_combox.currentIndex())
        stock_out_operator = self.stock_out_operator_combox.itemData(self.stock_out_operator_combox.currentIndex())
        stock_out_date = self.stock_out_dateTime.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        stock_out_total_amount = self.stock_out_total_amount_spinBox.value()
        stock_out_remark = self.stock_out_remark_plainTextEdit.toPlainText()

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        try:
            if not query.exec("BEGIN"):
                raise Exception(f"无法开始事务: {query.lastError().text()}")

            query.prepare(
                "UPDATE stock_out_main "
                "SET outbound_number = ?, out_type = ?, out_date = ?, operator_id = ?, total_amount = ?, remarks = ? "
                "WHERE out_id = ?")
            query.addBindValue(outbound_number)
            query.addBindValue(stock_out_type)
            query.addBindValue(stock_out_date)
            query.addBindValue(stock_out_operator)
            query.addBindValue(stock_out_total_amount)
            query.addBindValue(stock_out_remark)
            if not query.exec():
                raise Exception(f"更新出库单失败: {query.lastError().text()}")
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
        finally:
            # 显式清理资源
            query.finish()

    def create_stock_out(self):
        outbound_number = self.outbound_number_lineEdit.text()
        stock_out_type = self.stock_out_type_combox.currentText()
        stock_out_operator = self.stock_out_operator_combox.itemData(self.stock_out_operator_combox.currentIndex())
        stock_out_date = self.stock_out_dateTime.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        stock_out_total_amount = self.stock_out_total_amount_spinBox.value()
        stock_out_remark = self.stock_out_remark_plainTextEdit.toPlainText()

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            query.prepare(
                "Insert into stock_out_main(outbound_number, out_type, out_date, operator_id, total_amount, remarks) "
                "values (?,?,?,?,?,?)")
            query.addBindValue(outbound_number)
            query.addBindValue(stock_out_type)
            query.addBindValue(stock_out_date)
            query.addBindValue(stock_out_operator)
            query.addBindValue(stock_out_total_amount)
            query.addBindValue(stock_out_remark)
            if not query.exec():  # 执行INSERT语句
                raise Exception(f"插入数据失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "添加成功")
            self.accept()  # 关闭对话框
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
        finally:
            query.finish()


class StockOutAddDrugPage(QDialog, Ui_OutWarehouseDrugDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_event()
        self.detail_id = None
        self.load_data()
        self.ignore_cargo_return()

    def ignore_cargo_return(self):
        install_enter_key_filter(self.stock_out_list_combox)
        install_enter_key_filter(self.stock_batch_combox)
        install_enter_key_filter(self.outbatch_lineEdit)
        install_enter_key_filter(self.stock_out_drug_combox)
        install_enter_key_filter(self.stock_out_number_spinBox)
        install_enter_key_filter(self.stock_out_dateTimeEdit)

    def bind_event(self):
        self.stock_out_warehouse_drug_save_btn.clicked.connect(self.save)
        self.stock_batch_combox.currentIndexChanged.connect(self.load_stock_out_drug_data)

    def load_stock_out_drug_data(self, index):
        if index >= 0:
            stock_out_batch_id = self.stock_batch_combox.itemData(self.stock_batch_combox.currentIndex())
            self.load_stock_out_drug(stock_out_batch_id)

    def load_stock_out_drug(self, stock_out_batch_id):
        if stock_out_batch_id is not None:
            # 清空当前药品列表（除了默认选项）
            self.stock_out_drug_combox.clear()

            # 查询该批次对应的药品信息
            query = QSqlQuery()
            query.prepare("""
                SELECT md.dic_id, md.trade_name
                FROM stock_in_main sm
                JOIN medicine_dic md ON md.dic_id = (
                    SELECT pd.medicine_id 
                    FROM purchase_detail pd
                    JOIN stock_in_detail sd ON sd.purchase_detail_id = pd.detail_id
                    WHERE sd.in_id = ?
                    LIMIT 1
                )
                WHERE sm.in_id = ?
                LIMIT 1
            """)
            query.addBindValue(stock_out_batch_id)
            query.addBindValue(stock_out_batch_id)

            if query.exec() and query.next():
                medicine_id = query.value(0)
                medicine_name = query.value(1)
                self.stock_out_drug_combox.addItem(medicine_name, medicine_id)
                self.stock_out_drug_combox.setCurrentIndex(0)
            else:
                # 如果查询失败，添加一个空选项
                self.stock_out_drug_combox.addItem("请选择药品", None)
                if not query.exec():
                    print(f"数据库查询错误: {query.lastError().text()}")

    def save(self):
        if self.detail_id:
            self.update_stock_out_drug()
        else:
            self.create_stock_out_drug()

    def load_data(self):
        self.stock_out_dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        query = QSqlQuery("SELECT out_id, outbound_number FROM stock_out_main ORDER BY out_id DESC")
        while query.next():
            out_id = query.value(0)
            outbound_number = query.value(1)
            self.stock_out_list_combox.addItem(outbound_number, out_id)

        query = QSqlQuery("SELECT dic_id, trade_name FROM medicine_dic")
        while query.next():
            medicine_id = query.value(0)
            medicine_name = query.value(1)
            self.stock_out_drug_combox.addItem(medicine_name, medicine_id)
        query = QSqlQuery("SELECT in_id, batch FROM stock_in_main ORDER BY in_id DESC")
        while query.next():
            in_id = query.value(0)
            batch = query.value(1)
            self.stock_batch_combox.addItem(batch, in_id)
        out_batch = f"OUT-BN{QDate.currentDate().toString('yyyyMMdd')}-{random.randint(1000, 9999)}"
        self.outbatch_lineEdit.setText(out_batch)

    def create_stock_out_drug(self):
        stock_out_list = self.stock_out_list_combox.itemData(self.stock_out_list_combox.currentIndex())
        stock_out_drug = self.stock_out_drug_combox.itemData(self.stock_out_drug_combox.currentIndex())
        stock_batch = self.stock_batch_combox.itemData(self.stock_batch_combox.currentIndex())
        out_batch = self.outbatch_lineEdit.text()
        stock_out_number = self.stock_out_number_spinBox.value()
        stock_out_date = self.stock_out_dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")

        query = QSqlQuery()
        try:
            # 开始事务
            if not query.exec("BEGIN"):
                raise Exception(f"无法开始事务: {query.lastError().text()}")

            # 准备插入语句
            query.prepare("""
                INSERT INTO stock_out_detail(out_id, medicine_id,stock_batch, out_batch, quantity, time)
                VALUES (?, ?, ?, ?, ?, ?)
            """)
            # 绑定参数
            query.addBindValue(stock_out_list)
            query.addBindValue(stock_out_drug)
            query.addBindValue(stock_batch)

            query.addBindValue(out_batch)
            query.addBindValue(stock_out_number)
            query.addBindValue(stock_out_date)

            # 执行插入
            if not query.exec():  # 执行INSERT语句
                raise Exception(f"插入数据失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "添加成功")
            self.accept()

        except Exception as e:
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
            print(e)
        finally:
            query.finish()

    def update_stock_out_drug(self):
        if not self.detail_id:
            QMessageBox.critical(self, "错误", "无法找到要修改的出库单")
            return
        stock_out_list = self.stock_out_list_combox.itemData(self.stock_out_list_combox.currentIndex())
        stock_out_drug = self.stock_out_drug_combox.itemData(self.stock_out_drug_combox.currentIndex())
        stock_batch = self.stock_batch_combox.itemData(self.stock_batch_combox.currentIndex())
        out_batch = self.outbatch_lineEdit.text()
        stock_out_number = self.stock_out_number_spinBox.value()
        stock_out_date = self.stock_out_dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        try:
            if not query.exec("BEGIN"):
                raise Exception(f"无法开始事务: {query.lastError().text()}")

            query.prepare(
                "UPDATE stock_out_detail "
                "SET out_id=?, medicine_id=?,stock_batch=?, out_batch=?, quantity=?, time=?"
                "WHERE detail_id = ?")
            query.addBindValue(stock_out_list)
            query.addBindValue(stock_out_drug)
            query.addBindValue(stock_batch)
            query.addBindValue(out_batch)
            query.addBindValue(stock_out_number)
            query.addBindValue(stock_out_date)
            query.addBindValue(self.detail_id)
            if not query.exec():
                raise Exception(f"更新出库单失败: {query.lastError().text()}")
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
        finally:
            # 显式清理资源
            query.finish()

    def load_stock_out_update_data(self, detail_id):
        self.stock_out_warehouse_drug_save_btn.setText("更新出库")
        query = QSqlQuery()
        query.prepare("SELECT out_id, medicine_id, stock_batch, out_batch, quantity ,time "
                      "FROM stock_out_detail "
                      "WHERE detail_id = ?")
        query.addBindValue(detail_id)
        if query.exec():
            query.first()
            out_id = query.value(0)
            medicine_id = query.value(1)
            stock_batch = query.value(2)
            out_batch = query.value(3)
            quantity = query.value(4)
            self.stock_out_list_combox.setCurrentIndex(self.stock_out_list_combox.findData(out_id))
            self.stock_out_drug_combox.setCurrentIndex(self.stock_out_drug_combox.findData(medicine_id))
            self.stock_batch_combox.setCurrentIndex(self.stock_batch_combox.findData(stock_batch))
            self.outbatch_lineEdit.setText(out_batch)
            self.stock_out_number_spinBox.setValue(quantity)
            self.stock_out_dateTimeEdit.setDateTime(QDateTime.fromString(query.value(5), "yyyy-MM-dd hh:mm:ss"))
