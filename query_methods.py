from PySide6.QtCore import QDateTime
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox

import data.sqlite_data
from data.sqlite_data import (SupplierModel, StockInMainModel, StockInDetailModel, ShelvesDrugsMessageModel,
                              PurchaseDetailModel, PurchaseOrderModel, StockOutMainModel, StockOutDetailModel,
                              ShelvesDrugModel
                              )

# 其他工具
start_times = QDateTime.currentDateTime().addDays(-30).date().toString("yyyy-MM-dd")
end_times = QDateTime.currentDateTime().addDays(+1).date().toString("yyyy-MM-dd")


# 药品上架查询
def shelves_select(self):
    text = self.shelves_select_lineEdit.text().strip()
    if not text:
        data.sqlite_data.get_shelves_drug_model(self)
        return

    self.shelves_model = ShelvesDrugModel(self, self.db)
    sql = """
        SELECT
            e.shelves_id,
            sm.outbound_number,
            sd.out_batch,
            md.trade_name,
            e.shelves_number,
            wsp.location,
            sma.batch as 库存批次,
            sma.validity as 有效期
        FROM shelves_drug e
        LEFT JOIN stock_out_detail sd ON e.out_batch = sd.detail_id
        LEFT JOIN stock_in_main sma ON sd.stock_batch = sma.in_id
        LEFT JOIN medicine_dic md ON e.drug = md.dic_id
        LEFT JOIN warehouse_shelf_position wsp ON e.location_id = wsp.warehouse_shelf_id
        LEFT JOIN stock_out_main sm ON e.outbound_number = sm.out_id
        WHERE sm.outbound_number LIKE ?
    """
    query = QSqlQuery(self.db)
    query.prepare(sql)
    query.addBindValue(f"%{text}%")
    if not query.exec():
        print(f"查询错误: {query.lastError().text()}")
        return
    self.shelves_model.setQuery(query)
    self.drugs_on_shelves_tableView.setModel(self.shelves_model)
    for col in self.shelves_model.HIDDEN_COLUMNS:
        self.drugs_on_shelves_tableView.hideColumn(col)


# 出库单查询
def stock_out_number_select(self):
    current_index = self.stock_out_tabWidget.currentIndex()
    text = self.stock_out_number_lineEdit.text().strip()
    if not text:
        data.sqlite_data.get_stock_out_main_model(self, start_times, end_times)
        data.sqlite_data.get_stock_out_detail_model(self, start_times, end_times)
        return

    if current_index == 0:
        self.stock_out_main_model = StockOutMainModel(self, self.db)
        sql = f"""
            SELECT
                s.out_id,
                s.outbound_number,
                s.out_type,
                s.out_date,
                s.total_amount,
                s.remarks
            FROM stock_out_main s
            WHERE s.outbound_number LIKE ?
            """
        query = QSqlQuery(self.db)
        query.prepare(sql)
        query.addBindValue(f"%{text}%")
        if not query.exec():
            print(f"查询错误: {query.lastError().text()}")
            return
        self.stock_out_main_model.setQuery(query)
        self.stock_out_main_tableView.setModel(self.stock_out_main_model)
        for col in self.stock_out_main_model.hidden_columns:
            self.stock_out_main_tableView.hideColumn(col)

    elif current_index == 1:
        self.stock_out_detail_model = StockOutDetailModel(self, self.db)
        sql = f"""
            SELECT
                s.detail_id,
                sm.outbound_number,
                dic.trade_name,
                st.batch,
                s.out_batch,
                s.quantity,
                s.time,
                st.in_date as 入库时间
            FROM stock_out_detail s
            LEFT JOIN stock_out_main sm ON s.out_id = sm.out_id
            LEFT JOIN medicine_dic dic ON s.medicine_id = dic.dic_id
            LEFT JOIN stock_in_main st ON s.stock_batch = st.in_id
            where sm.outbound_number LIKE ?
        """
        query = QSqlQuery(self.db)
        query.prepare(sql)
        query.addBindValue(f"%{text}%")
        if not query.exec():
            print(f"查询错误: {query.lastError().text()}")
            return
        self.stock_out_detail_model.setQuery(query)
        self.stock_out_detail_tableView.setModel(self.stock_out_detail_model)
        for col in self.stock_out_detail_model.hidden_columns:
            self.stock_out_detail_tableView.hideColumn(col)


# 采购单查询
def purchase_order_select(self):
    current_index = self.order_tabWidget.currentIndex()
    text = self.purchase_order_lineEdit.text().strip()

    if not text:
        data.sqlite_data.get_purchase_order_model(self, start_times, end_times)
        data.sqlite_data.get_purchase_order_detail_model(self, start_times, end_times)
        return

    if current_index == 0:
        self.purchase_order_model = PurchaseOrderModel(self, self.db)
        sql = f"""
            SELECT
                pur.order_id,
                pur.order_number,
                de.name,
                pur.order_date,
                pur.expected_delivery_date,
                pur.total_amount,
                pur.remarks
            FROM purchase_order pur
            LEFT JOIN supplier de ON pur.supplier_id = de.supplier_id
            LEFT JOIN purchase_order ord ON pur.order_id = ord.order_id
            WHERE pur.order_number LIKE ?
        """
        query = QSqlQuery(self.db)
        query.prepare(sql)
        query.addBindValue(f"%{text}%")
        if not query.exec():
            print(f"查询错误: {query.lastError().text()}")
            return
        self.purchase_order_model.setQuery(query)
        self.purchase_order_tableView.setModel(self.purchase_order_model)
        for col in self.purchase_order_model.hidden_columns:
            self.purchase_order_tableView.hideColumn(col)

    elif current_index == 1:
        self.purchase_order_detail_model = PurchaseDetailModel(self, self.db)
        sql = f"""
            SELECT
                pur.detail_id,
                ord.order_number,
                de.trade_name,
                pur.quantity,
                pur.purchase_total_price,
                pur.purchase_price,
                de.price as 售价,
                ord.order_date as 下单时间,
                pur.remarks as 备注  
            FROM purchase_detail pur
            LEFT JOIN medicine_dic de ON pur.medicine_id = de.dic_id
            LEFT JOIN purchase_order ord ON pur.order_id = ord.order_id
            WHERE ord.order_number LIKE ?
        """
        query = QSqlQuery(self.db)
        query.prepare(sql)
        query.addBindValue(f"%{text}%")
        if not query.exec():
            print(f"查询错误: {query.lastError().text()}")
            return
        self.purchase_order_detail_model.setQuery(query)
        self.purchase_detail_tableView.setModel(self.purchase_order_detail_model)
        for col in self.purchase_order_detail_model.hidden_columns:
            self.purchase_detail_tableView.hideColumn(col)


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
                s.total_amount,
                s.invoice_number,
                s.batch,
                s.production_lot_number,
                s.validity,
                s.remarks as 备注
            FROM stock_in_main s
            LEFT JOIN purchase_order p ON s.order_id = p.order_id
            LEFT JOIN supplier r ON p.supplier_id = r.supplier_id
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
        self.purchase_order_detail_model = PurchaseDetailModel(self, self.db)
        sql = f"""
            SELECT
                pur.detail_id,
                ord.order_number,
                de.trade_name,
                pur.quantity,
                pur.purchase_total_price,
                pur.purchase_price,
                de.price as 售价,
                ord.order_date as 下单时间,
                pur.remarks as 备注  
            FROM purchase_detail pur
            LEFT JOIN medicine_dic de ON pur.medicine_id = de.dic_id
            LEFT JOIN purchase_order ord ON pur.order_id = ord.order_id
            WHERE ord.order_number LIKE ?
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


def sales_record_query(self):
    text = self.sales_records_lineEdit.text().strip()
    if not text:
        data.sqlite_data.get_sales_lists_model(self)
        return

    self.purchase_order_detail_model = PurchaseDetailModel(self, self.db)
    sql = f"""
        SELECT
            pur.detail_id,
            ord.order_number,
            de.trade_name,
            pur.quantity,
            pur.purchase_total_price,
            pur.purchase_price,
            de.price as 售价,
            ord.order_date as 下单时间,
            pur.remarks as 备注  
        FROM purchase_detail pur
        LEFT JOIN medicine_dic de ON pur.medicine_id = de.dic_id
        LEFT JOIN purchase_order ord ON pur.order_id = ord.order_id
        WHERE ord.order_number LIKE '%{text}%'
    """
    self.purchase_order_detail_model.setQuery(sql, self.db)
    self.purchase_detail_tableView.setModel(self.purchase_order_detail_model)
    for col in self.purchase_order_detail_model.hidden_columns:
        self.purchase_detail_tableView.hideColumn(col)
