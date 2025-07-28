from PySide6.QtSql import QSqlQuery


def insert_sample_data(self):
    # 检查表是否为空
    query = QSqlQuery()
    query.exec_("SELECT * FROM medicine LIMIT 1")
    if not query.next():  # 如果表为空
        print("表为空，插入示例数据")

        # 插入示例数据
        query.exec_(
            "INSERT INTO medicine (name, generic_name, manufacturer, batch_number, expiry_date, purchase_date, quantity, price, barcode, category_id, supplier_id) VALUES ('阿莫西林', 'Amoxicillin', '某制药厂', '123456', '2026-12-31', '2025-07-06', 100, 5.5, '1234567890123', 1, 1)")
        query.exec_(
            "INSERT INTO medicine (name, generic_name, manufacturer, batch_number, expiry_date, purchase_date, quantity, price, barcode, category_id, supplier_id) VALUES ('感冒灵', 'Cold Remedy', '某制药厂', '789012', '2026-11-30', '2025-07-05', 200, 3.0, '9876543210987', 2, 2)")
        query.exec_(
            "INSERT INTO medicine (name, generic_name, manufacturer, batch_number, expiry_date, purchase_date, quantity, price, barcode, category_id, supplier_id) VALUES ('布洛芬', 'Ibuprofen', '某制药厂', '345678', '2026-10-31', '2025-07-04', 50, 2.5, '5678901234567', 1, 1)")
    else:
        print("表中已有数据，跳过插入示例数据")