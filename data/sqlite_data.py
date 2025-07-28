import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtWidgets import QMessageBox


class DatabaseInit(QSqlDatabase, QMessageBox):
    def __init__(self):
        super().__init__()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("pharmacy.db")
        if not self.db.open():
            QMessageBox.critical(
                None, "数据库错误",
                f"无法打开数据库: {self.db.lastError().text()}"
            )
            sys.exit(1)

        query = QSqlQuery()
        query.exec("""
        CREATE TABLE IF NOT EXISTS medicine (             -- 药品信息表
                medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                generic_name TEXT,
                specification_id INTEGER NOT NULL ,        -- 规格型号
                manufacturer TEXT NOT NULL,  -- 生产厂家必填
                batch_number TEXT NOT NULL,  -- 批号必填
                expiry_date DATE NOT NULL,    -- 有效期必填
                purchase_date DATE,          -- 采购日期可选
                quantity INTEGER NOT NULL CHECK (quantity >= 0),   -- 库存数量
                price REAL NOT NULL CHECK (price >= 0),
                barcode TEXT,                   -- 国药准字
                category_id INTEGER NOT NULL,  -- 分类必选
                supplier_id INTEGER NOT NULL,  -- 供应商必选
                FOREIGN KEY (category_id) REFERENCES MedicineCategories(category_id),
                FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id),
                FOREIGN KEY (specification_id) REFERENCES Specification(specification_id),
                UNIQUE (name, manufacturer, batch_number)  -- 防重复批号
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS drug_formulation(
                formulation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                formulation_name TEXT NOT NULL           -- 剂型名称
        )""")

        query.exec("""
        CREATE TABLE IF NOT EXISTS drug_unit(
                unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
                unit_name TEXT NOT NULL              -- 单位名称
        )""")

        query.exec("""
        CREATE TABLE IF NOT EXISTS Specification(
                specification_id INT PRIMARY KEY,
                formulation_id INT,
                unit_id INT,
                dosage VARCHAR(50),                -- 剂量
                packaging_unit VARCHAR(20),        -- 包装单位
                packaging_quantity INT,            -- 包装数量
                FOREIGN KEY (formulation_id) REFERENCES drug_formulation(formulation_id),
                FOREIGN KEY (unit_id) REFERENCES drug_unit(unit_id)
        )""")

        query.exec(""" 
        CREATE TABLE IF NOT EXISTS MedicineCategories(          -- 药品分类表
                category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_name TEXT NOT NULL UNIQUE
        )
        """)

        query.exec(""" 
        CREATE TABLE IF NOT EXISTS price_adjustment(          -- 调价单表
                adjustment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                medicine_id INTEGER NOT NULL,
                old_price REAL NOT NULL,                  -- 调整前价格
                new_price REAL NOT NULL,                  -- 调整后价格
                adjustment_date DATE NOT NULL,            -- 调价日期
                reason TEXT,                              -- 调价原因（备注）
                FOREIGN KEY (medicine_id) REFERENCES medicine (medicine_id)
        )
        """)

        query.exec(""" 
        CREATE TABLE IF NOT EXISTS inventory_check(         
            check_id INTEGER PRIMARY KEY AUTOINCREMENT,
            medicine_id INTEGER NOT NULL,
            recorded_quantity INTEGER NOT NULL,         -- 盘点数量
            actual_quantity INTEGER NOT NULL,           -- 实际数量
            check_date DATE NOT NULL,                   -- 盘点日期
            discrepancy_reason TEXT,                    -- 差异原因（备注）
            FOREIGN KEY (medicine_id) REFERENCES medicine (medicine_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS supplier (             -- 供应商信息表
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,      -- 供应商唯一标识ID
            name TEXT NOT NULL,                                 -- 供应商名字
            contact_person TEXT,                                -- 联系人
            phone TEXT,                                         -- 联系电话
            address TEXT,                                       -- 地址
            email TEXT,                                        -- 邮箱
            status BOOLEAN DEFAULT 1,                          -- 状态（1: 正常，0: 禁用）
            remarks TEXT,                                      -- 备注
            update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- 更新时间
            update_by TEXT,                                    -- 更新人
            create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
            created_by TEXT                                     -- 创建人
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS purchase_order (                   -- 采购订单表
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,      -- 订单ID
                supplier_id INTEGER NOT NULL,                   -- 供应商ID
                order_date DATE NOT NULL DEFAULT CURRENT_DATE,  -- 下单日期
                expected_delivery_date DATE,                   -- 预计交货日期
                total_amount REAL,                             -- 订单总金额
                status TEXT NOT NULL DEFAULT '待处理',          -- 订单状态(待处理/已发货/已完成/已取消)
                remarks TEXT,                                  -- 备注
                FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS purchase_detail (                   -- 采购明细表（从表）
            detail_id INTEGER PRIMARY KEY AUTOINCREMENT,    -- 明细ID
            order_id INTEGER NOT NULL,                     -- 订单ID（外键）
            medicine_id INTEGER NOT NULL,                  -- 药品ID（外键）
            quantity INTEGER NOT NULL CHECK (quantity > 0),-- 采购数量
            remaining_quantity INTEGER NOT NULL DEFAULT 0 CHECK (remaining_quantity >= 0), -- 剩余库存
            purchase_price REAL NOT NULL CHECK (purchase_price >= 0), -- 采购单价
            sale_price REAL NOT NULL CHECK (sale_price >= 0), -- 销售单价
            batch_number TEXT NOT NULL,                    -- 批号
            expiry_date DATE NOT NULL,                     -- 有效期
            FOREIGN KEY (order_id) REFERENCES purchase_order(order_id),
            FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS stock_in_main (                   -- 入库主表（记录入库单头信息）
                in_id INTEGER PRIMARY KEY AUTOINCREMENT,      -- 入库单ID
                order_id INTEGER,                             -- 关联采购订单ID（可为空，允许直接入库）
                supplier_id INTEGER NOT NULL,                 -- 供应商ID
                in_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- 入库日期时间
                operator_id INTEGER NOT NULL,                 -- 操作员ID（外键关联用户表）
                total_amount REAL,                            -- 入库总金额
                invoice_number TEXT,                          -- 发票号
                remarks TEXT,                                 -- 备注
                FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id),
                FOREIGN KEY (operator_id) REFERENCES users(users_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS stock_in_detail (                   -- 入库明细表（记录具体药品入库信息）
                detail_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 明细ID
                in_id INTEGER NOT NULL,                      -- 关联入库单ID
                medicine_id INTEGER NOT NULL,                -- 药品ID
                batch_number TEXT NOT NULL,                  -- 批号
                expiry_date DATE NOT NULL,                   -- 有效期
                purchase_price REAL NOT NULL CHECK (purchase_price >= 0), -- 采购单价
                sale_price REAL NOT NULL CHECK (sale_price >= 0),         -- 销售单价
                quantity INTEGER NOT NULL CHECK (quantity > 0),          -- 入库数量
                actual_quantity INTEGER NOT NULL CHECK (actual_quantity > 0), -- 实际入库数量（可能不同于采购数量）
                FOREIGN KEY (in_id) REFERENCES stock_in_main(in_id),
                FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS inventory_batch (                   -- 库存批次表（核心库存管理）
                batch_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 批次ID
                medicine_id INTEGER NOT NULL,               -- 药品ID
                in_detail_id INTEGER NOT NULL,              -- 关联入库明细ID
                batch_number TEXT NOT NULL,                 -- 批号
                expiry_date DATE NOT NULL,                  -- 有效期
                purchase_price REAL NOT NULL,               -- 采购单价
                sale_price REAL NOT NULL,                   -- 销售单价
                current_quantity INTEGER NOT NULL CHECK (current_quantity >= 0), -- 当前库存数量
                in_date DATE NOT NULL,                      -- 入库日期
                location TEXT,                              -- 货位/存放位置
                FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id),
                FOREIGN KEY (in_detail_id) REFERENCES stock_in_detail(detail_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS stock_out_main (                  -- 出库主表（记录出库单头信息）
                out_id INTEGER PRIMARY KEY AUTOINCREMENT,      -- 出库单ID
                out_type TEXT NOT NULL CHECK (out_type IN ('销售', '调拨', '报损', '退货', '科室领用')), -- 出库类型
                out_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- 出库日期时间
                operator_id INTEGER NOT NULL,                  -- 操作员ID（外键关联用户表）
                related_id INTEGER,                            -- 关联单据ID（如销售单ID、调拨申请ID等）
                customer_id INTEGER,                           -- 客户ID（仅销售出库使用）
                total_amount REAL,                             -- 出库总金额（销售出库有意义）
                remarks TEXT,                                  -- 备注
                FOREIGN KEY (operator_id) REFERENCES users(users_id),
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS stock_out_detail (                   -- 出库明细表（记录具体药品出库信息））
                detail_id INTEGER PRIMARY KEY AUTOINCREMENT,   -- 明细ID
                out_id INTEGER NOT NULL,                       -- 关联出库单ID
                medicine_id INTEGER NOT NULL,                  -- 药品ID
                batch_id INTEGER NOT NULL,                     -- 出库批次ID（关键字段）
                quantity INTEGER NOT NULL CHECK (quantity > 0),-- 出库数量
                sale_price REAL,                               -- 销售单价（仅销售出库有意义）
                cost_price REAL,                               -- 成本单价（用于计算利润）
                sub_total REAL,                                -- 小计金额（数量*单价）
                FOREIGN KEY (out_id) REFERENCES stock_out_main(out_id),
                FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id),
                FOREIGN KEY (batch_id) REFERENCES inventory_batch(batch_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS sales (                                -- 销售记录表
            sales_id INTEGER PRIMARY KEY AUTOINCREMENT,                   -- 主键ID
            medicine_id INTEGER NOT NULL,                                 -- 对应的药品 ID（外键）
            quantity INTEGER NOT NULL CHECK (quantity >= 0),              -- 销售数量
            price REAL NOT NULL CHECK (price >= 0),                       -- 销售单价
            sale_date DATE NOT NULL CHECK (sale_date <= CURRENT_DATE),    -- 销售日期
            FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id)   -- 定义medicine_id为外键，引用medicine表中的id字段
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS inventory (                             -- 库存记录表
            inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,                -- 主键ID
            medicine_id INTEGER,                                           -- 对应的药品 ID（外键）
            quantity INTEGER,                                              -- 库存数量变化
            change_date DATE,                                              -- 库存变化日期
            change_type TEXT,                                              -- 变化类型（进货、销售等）
            FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS users(                                   -- 用户信息表
            users_id INTEGER PRIMARY KEY AUTOINCREMENT,                           -- 主键ID
            username TEXT NOT NULL,                                         -- 用户名
            password TEXT NOT NULL,                                         -- 密码
            role TEXT                                                       -- 用户角色
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS customers(                                   -- 客户信息表
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            customer_phone TEXT,
            role TEXT
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS logs(
            logs_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,                               -- 操作用户 ID（外键）
            action TEXT,                                   -- 操作描述
            timestamp DATETIME,                            -- 操作时间
            FOREIGN KEY (user_id) REFERENCES users(users_id)
    )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS expiring_medicines(
            expiring_medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            medicine_id INTEGER,
            expiry_date DATE,                                 -- 药品的到期时间
            days INTEGER,                                     -- 临期天数
            inventory_remainder TEXT,                         -- 库存剩余数量
            days_before_expiry INTEGER,                       -- 临期提醒提前天数
            FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id)   -- 定义medicine_id为外键，引用medicine表中的id字段
    )
        """)


# 基表模型
class BaseTableModel(QSqlTableModel):
    def __init__(self, parent=None, db=None, table_name="", headers=None, hidden_columns=None):
        super().__init__(parent, db)
        self.setTable(table_name)
        self.select()

        # 设置查询（带行数限制）
        self.setQuery(f"SELECT * FROM {table_name} LIMIT 100")

        # 设置表头
        if headers:
            for col_index, header_text in headers.items():
                self.setHeaderData(col_index, Qt.Horizontal, header_text)

        # 记录隐藏列
        self.hidden_columns = hidden_columns or []


# 药物模型
class MedicineModel(BaseTableModel):
    HEADERS = {
        1: "药品名称",
        2: "通用名",
        3: "规格",
        4: "生产厂家",
        5: "批号",
        6: "有效期",
        7: "采购日期",
        8: "库存数量",
        9: "单价",
        10: "国药准字",
        11: "分类",
        12: "供应商",
    }
    HIDDEN_COLUMNS = [0, 13, 14, 15]  # 隐藏的列索引

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="medicine",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 临期模型
class ExpiringMedicineModel(BaseTableModel):
    HEADERS = {
        1: "药品名称",
        2: "药品到期时间",
        3: "剩余天数",
        4: "剩余库存数量",
        5: "临期提醒时间"
    }
    HIDDEN_COLUMNS = [0, 6]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="expiring_medicines",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 供应商模式
class SupplierModel(BaseTableModel):
    HEADERS = {
        1: "名称",
        2: "联系人",
        3: "电话",
        4: "地址",
        5: "邮箱",
        6: "状态",
        7: "备注",
        8: "更新时间",
        9: "更新人",
        10: "创建时间",
        11: "创建人"
    }
    HIDDEN_COLUMNS = [0, 12, 13]  # 隐藏的列索引

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="supplier",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 采购订单模式
class PurchaseOrderModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "供应商",
        2: "下单日期",
        3: "预计交货日期",
        4: "订单总金额",
        5: "状态",
        6: "备注"
    }
    HIDDEN_COLUMNS = [0, 7, 8]  # 隐藏的列索引

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="purchase_order",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 采购明细模式
class PurchaseDetailModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "订单ID",
        2: "药品ID",
        3: "采购数量",
        4: "剩余库存",
        5: "采购单价",
        6: "销售单价",
        7: "批号",
        8: "有效期"
    }
    HIDDEN_COLUMNS = [0, 9, 10]  # 隐藏的列索引

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="purchase_detail",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 销售模式
class SalesModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "药品名称",
        2: "销售数量",
        3: "销售单价",
        4: "销售日期",
    }
    HIDDEN_COLUMNS = [0, 5]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="sales",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 库存记录模型
class InventoryModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "药品名称",
        2: "库存数量变化",
        3: "库存变化日期",
        4: "变化类型",
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="inventory",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 入库主模型
class StockInMainModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "采购订单",
        2: "供应商",
        3: "入库日期",
        4: "操作员",
        5: "入库总金额",
        6: "发票号",
        7: "备注",
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="stock_in_main",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 入库明细模式
class StockInDetailModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "采购订单",
        2: "药品",
        3: "批号",
        4: "有效期",
        5: "采购单价",
        6: "销售单价",
        7: "入库数量",
        8: "实际入库数量",
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="stock_in_detail",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 库存批次模式
class InventoryDatchModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "药品",
        2: "入库明细ID",
        3: "批号",
        4: "有效期",
        5: "采购单价",
        6: "销售单价",
        7: "当前库存数量",
        8: "入库日期",
        9: "货位",
    }
    HIDDEN_COLUMNS = [0, 10]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="inventory_batch",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 出库主模型
class StockOutMainModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "出库类型",
        2: "出库日期",
        3: "操作员",
        4: "关联单据",
        5: "客户",
        6: "出库总金额",
        7: "备注",
    }
    HIDDEN_COLUMNS = [0, 8]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="stock_out_main",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 出库明细模式
class StockOutDetailModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "出库单",
        2: "药品",
        3: "出库批次",
        4: "出库数量",
        5: "销售单价",
        6: "成本单价",
        7: "小计",
    }
    HIDDEN_COLUMNS = [0, 8]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="stock_out_detail",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 库存盘点模式
class InventoryCheckModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "药品名称",
        2: "盘点数量",
        3: "盘点日期",
        4: "盘点人",
        5: "盘点结果",
        6: "备注",
    }
    HIDDEN_COLUMNS = [0, 7]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="inventory_check",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class MedicineCategoriesModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "类型"
    }
    HIDDEN_COLUMNS = []

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="MedicineCategories",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class DrugRormulationModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "剂型"
    }
    HIDDEN_COLUMNS = []

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="drug_formulation",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class DrugUnitModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "单位"
    }
    HIDDEN_COLUMNS = []

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="drug_unit",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class SpecificationModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "剂量",
        2: "包装单位",
        3: "包装数量"
    }
    HIDDEN_COLUMNS = [4, 5]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="Specification",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 药品
def get_medicines_model(self):
    self.medicine_model = MedicineModel(self, self.db)
    self.drug_selection_tableView.setModel(self.medicine_model)

    # 应用隐藏列
    for col in self.medicine_model.hidden_columns:
        self.drug_selection_tableView.hideColumn(col)

    return self.medicine_model


# 临期
def get_expiring_medicine_model(self):
    self.expiring_medicine_model = ExpiringMedicineModel(self, self.db)
    self.expiring_drugs_tableView.setModel(self.expiring_medicine_model)

    # 应用隐藏列
    for col in self.expiring_medicine_model.hidden_columns:
        self.expiring_drugs_tableView.hideColumn(col)

    return self.expiring_medicine_model


# 入库主模型
def get_stock_in_main_model(self):
    self.stock_in_main_model = StockInMainModel(self, self.db)
    # table = self.findChild(QTableView, "main_tableView")
    # table.setModel(self.stock_in_main_model)
    self.main_tableView.setModel(self.stock_in_main_model)
    for col in self.stock_in_main_model.hidden_columns:
        self.main_tableView.hideColumn(col)

    return self.stock_in_main_model


# 入库明细模型
def get_stock_in_detail_model(self):
    self.stock_in_detail_model = StockInDetailModel(self, self.db)
    # table = self.findChild(QTableView, "detail_tableView")
    # table.setModel(self.stock_in_detail_model)
    self.detail_tableView.setModel(self.stock_in_detail_model)
    for col in self.stock_in_detail_model.hidden_columns:
        self.detail_tableView.hideColumn(col)

    return self.stock_in_detail_model


# 库存批次模型
def get_inventory_datch_model(self):
    self.inventory_datch_model = InventoryDatchModel(self, self.db)
    self.batch_tableView.setModel(self.inventory_datch_model)
    for col in self.inventory_datch_model.hidden_columns:
        self.batch_tableView.hideColumn(col)

    return self.inventory_datch_model


# 出库主模型
def get_stock_out_main_model(self):
    self.stock_out_main_model = StockOutMainModel(self, self.db)
    self.stock_out_main_tableView.setModel(self.stock_out_main_model)
    for col in self.stock_out_main_model.hidden_columns:
        self.stock_out_main_tableView.hideColumn(col)

    return self.stock_out_main_model


# 出库明细模型
def get_stock_out_detail_model(self):
    self.stock_out_detail_model = StockOutDetailModel(self, self.db)
    self.stock_out_detail_tableView.setModel(self.stock_out_detail_model)
    for col in self.stock_out_detail_model.hidden_columns:
        self.stock_out_detail_tableView.hideColumn(col)

    return self.stock_out_detail_model


# 供应商
def get_supplier_model(self):
    self.supplier_model = SupplierModel(self, self.db)
    self.supplier_tableView.setModel(self.supplier_model)

    # 应用隐藏列
    for col in self.supplier_model.hidden_columns:
        self.supplier_tableView.hideColumn(col)

    return self.supplier_model


# 采购订单
def get_purchase_order_model(self):
    self.purchase_order_model = PurchaseOrderModel(self, self.db)
    self.purchase_order_tableView.setModel(self.purchase_order_model)
    for col in self.purchase_order_model.hidden_columns:
        self.purchase_order_tableView.hideColumn(col)

    return self.purchase_order_model


# 采购订单明细
def get_purchase_order_detail_model(self):
    self.purchase_order_detail_model = PurchaseDetailModel(self, self.db)
    self.purchase_detail_tableView.setModel(self.purchase_order_detail_model)
    for col in self.purchase_order_detail_model.hidden_columns:
        self.purchase_detail_tableView.hideColumn(col)
    return self.purchase_order_detail_model


# 销售
def get_sales_model(self):
    self.sales_model = SalesModel(self, self.db)
    self.sales_records_tableView.setModel(self.sales_model)
    for col in self.sales_model.hidden_columns:
        self.sales_records_tableView.hideColumn(col)

    return self.sales_model


# 库存记录
def get_inventory_model(self):
    self.inventory_model = InventoryModel(self, self.db)
    self.inventory_tableView.setModel(self.inventory_model)
    for col in self.inventory_model.hidden_columns:
        self.inventory_tableView.hideColumn(col)

    return self.inventory_model


# 库存盘点
def get_inventory_check(self):
    self.inventory_check_model = InventoryCheckModel(self, self.db)
    self.inventory_check_tableView.setModel(self.inventory_check_model)
    for col in self.inventory_check_model.hidden_columns:
        self.inventory_check_tableView.hideColumn(col)

    return self.inventory_check_model
