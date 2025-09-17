from PySide6.QtCore import QDateTime
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox

import data.sqlite_data
from data.sqlite_data import SupplierModel, StockInMainModel, StockInDetailModel, ShelvesDrugsMessageModel

# 其他工具
start_times = QDateTime.currentDateTime().addDays(-30).date().toString("yyyy-MM-dd")
end_times = QDateTime.currentDateTime().addDays(+1).date().toString("yyyy-MM-dd")


def stock_in_query(self):
    current_index = self.stock_in_tabWidget.currentIndex()
    text = self.stock_in_lineEdit.text().strip()

    # 如果文本为空，显示所有数据
    if not text:
        data.sqlite_data.get_stock_in_detail_model(self, start_times, end_times)
        data.sqlite_data.get_stock_in_main_model(self, start_times, end_times)
        return

    # 使用参数化查询避免SQL注入
    if current_index == 0:
        self.stock_in_main_model = StockInMainModel(self, self.db)
        sql = """
            SELECT
                s.in_id,
                p.order_number,
                r.name,
                s.in_date,
                us.username,
                s.total_amount,
                s.invoice_number,
                s.batch,
                s.production_lot_number,
                s.validity,
                s.remarks as 备注
            FROM stock_in_main s
            LEFT JOIN purchase_order p ON s.order_id = p.order_id
            LEFT JOIN supplier r ON p.supplier_id = r.supplier_id
            LEFT JOIN users us ON s.operator_id = us.users_id
            WHERE p.order_number LIKE ?
        """
        query = QSqlQuery(self.db)
        query.prepare(sql)
        query.addBindValue(f"%{text}%")

        if not query.exec():
            print(f"查询错误: {query.lastError().text()}")
            return

        self.stock_in_main_model.setQuery(query)
        self.main_tableView.setModel(self.stock_in_main_model)
        for col in self.stock_in_main_model.hidden_columns:
            self.main_tableView.hideColumn(col)

    elif current_index == 1:
        self.stock_in_detail_model = StockInDetailModel(self, self.db)
        sql = """
            SELECT
                s.detail_id,
                o.order_number,
                dic.trade_name,
                m.validity,
                pu.purchase_price,
                dic.price,
                s.quantity as 入库数量,
                s.actual_quantity as 实际入库数量,
                i.location as 库存位置,
                st.quantity as 库存数量,
                m.batch as 库存批次,
                m.production_lot_number as 生产批号,
                m.in_date as 入库时间
            FROM stock_in_detail s
            LEFT JOIN stock_in_main m ON s.in_id = m.in_id
            LEFT JOIN purchase_detail pu ON s.purchase_detail_id = pu.detail_id
            LEFT JOIN purchase_order o ON m.order_id = o.order_id
            LEFT JOIN medicine_dic dic ON pu.medicine_id = dic.dic_id
            LEFT JOIN warehouse_shelf_position i ON s.warehouse_shelf_id = i.warehouse_shelf_id
            LEFT JOIN stock st ON st.batch = s.in_id AND st.location = s.warehouse_shelf_id
            WHERE o.order_number LIKE ?
        """
        query = QSqlQuery(self.db)
        query.prepare(sql)
        query.addBindValue(f"%{text}%")

        if not query.exec():
            print(f"查询错误: {query.lastError().text()}")
            return

        self.stock_in_detail_model.setQuery(query)
        self.detail_tableView.setModel(self.stock_in_detail_model)
        for col in self.stock_in_detail_model.hidden_columns:
            self.detail_tableView.hideColumn(col)


def drug_selection_query(self):
    text = self.search_le.text().strip()
    if not text:
        data.sqlite_data.get_shelves_drug_message_model(self)
        return
    self.searction = ShelvesDrugsMessageModel(self, self.db)
    sql = f"""
    SELECT
        d.drug_information_shelves_id,
        d.drug,
        d.expiration_date,
        d.purchase_date,
        d.shelves_sum,
        d.warehouse_inventory_sum,
        d.shelves_location,
        d.warehouse_inventory_location,
        d.approval_number,
        d.manufacturer,
        d.batch,
        d.supplier
        FROM drug_information_shelves d
        WHERE d.drug LIKE '%{text}%'
        """
    self.searction.setQuery(sql, self.db)
    self.shelves_drug_tableView.setModel(self.searction)
    for col in self.searction.hidden_columns:
        self.shelves_drug_tableView.hideColumn(col)


def supplier_query(self):
    """根据输入的文本查询供应商"""
    text = self.supplier_lineEdit.text().strip()

    # 如果输入为空，则显示所有供应商
    if not text:
        data.sqlite_data.get_supplier_model(self)
        return

    # 如果有输入文本，则进行模糊查询
    self.supplier_model = SupplierModel(self, self.db)
    sql = f"""
        SELECT
            s.supplier_id,
            s.name,
            s.contact_person,
            s.phone,
            s.address,
            s.email,
            s.remarks,
            s.update_at,
            s.update_by,
            s.create_at,
            s.created_by
        FROM supplier s
        WHERE s.name LIKE '%{text}%' 
           OR s.contact_person LIKE '%{text}%'
           OR s.phone LIKE '%{text}%'
           OR s.address LIKE '%{text}%'
           OR s.email LIKE '%{text}%'
    """
    self.supplier_model.setQuery(sql, self.db)
    self.supplier_tableView.setModel(self.supplier_model)

    # 隐藏ID列
    for col in self.supplier_model.HIDDEN_COLUMNS:
        self.supplier_tableView.hideColumn(col)


def storage_query(self):
    current_index = self.stock_in_tabWidget.currentIndex()
    storage_start_date = self.storage_dateEdit_start.date().toString("yyyy-MM-dd")
    storage_end_date = self.storage_dateEdit_deadline_end.date().toString("yyyy-MM-dd")
    if current_index == 0:
        data.sqlite_data.get_stock_in_main_model(self, storage_start_date, storage_end_date)
    elif current_index == 1:
        data.sqlite_data.get_stock_in_detail_model(self, storage_start_date, storage_end_date)


def sale_record(self):
    current_interface_index = self.tabWidget.currentIndex()
    sale_start_date = self.sales_records_dateEdit_start.date().toString("yyyy-MM-dd")
    sale_end_date = self.sales_records_dateEdit_deadline.date().toString("yyyy-MM-dd")
    if current_interface_index == 0:
        data.sqlite_data.get_sales_lists_model(self, sale_start_date, sale_end_date)
    elif current_interface_index == 1:
        data.sqlite_data.get_sales_model(self, sale_start_date, sale_end_date)


def pur_order(self):
    current_interface_index = self.order_tabWidget.currentIndex()
    pur_start_date = self.purchase_order_dateEdit_start.date().toString("yyyy-MM-dd")
    pur_end_date = self.purchase_order_dateEdit_deadline.date().toString("yyyy-MM-dd")
    if current_interface_index == 0:
        data.sqlite_data.get_purchase_order_model(self, pur_start_date, pur_end_date)
    elif current_interface_index == 1:
        data.sqlite_data.get_purchase_order_detail_model(self, pur_start_date, pur_end_date)


def stock_out_query(self):
    """出库记录查询"""
    current_interface_index = self.stock_out_tabWidget.currentIndex()
    start_date = self.stock_out_dateEdit_start.date().toString("yyyy-MM-dd")
    end_date = self.stock_out_dateEdit_deadline.date().toString("yyyy-MM-dd")
    if current_interface_index == 0:
        data.sqlite_data.get_stock_out_main_model(self, start_date, end_date)
    elif current_interface_index == 1:
        data.sqlite_data.get_stock_out_detail_model(self, start_date, end_date)


def inventory_check_query(self):
    """库存盘点查询"""
    try:
        start_date = self.inventory_check_dateEdit_start.date().toString("yyyy-MM-dd")
        end_date = self.inventory_check_dateEdit_deadline.date().toString("yyyy-MM-dd")

        data.sqlite_data.get_inventory_check(self, start_date, end_date)

    except Exception as e:
        QMessageBox.critical(self, "查询错误", f"查询库存盘点时出错: {str(e)}")


def inventory_record_query(self):
    """库存记录查询"""
    try:
        start_date = self.inventory_dateEdit_start.date().toString("yyyy-MM-dd")
        end_date = self.inventory_dateEdit_deadline.date().toString("yyyy-MM-dd")

        data.sqlite_data.get_inventory_model(self, start_date, end_date)

    except Exception as e:
        QMessageBox.critical(self, "查询错误", f"查询库存记录时出错: {str(e)}")
