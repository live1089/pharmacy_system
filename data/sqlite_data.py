import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtWidgets import QMessageBox, QTableView


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
                manufacturer TEXT NOT NULL,  -- 生产厂家必填
                batch_number TEXT NOT NULL,  -- 批号必填
                expiry_date DATE NOT NULL,    -- 有效期必填
                purchase_date DATE,          -- 采购日期可选
                quantity INTEGER NOT NULL CHECK (quantity >= 0),
                unit TEXT NOT NULL,          -- 单位必填（如：盒/瓶/克）
                price REAL NOT NULL CHECK (price >= 0),
                barcode TEXT,                   -- 批次条码
                category_id INTEGER NOT NULL,  -- 分类必选
                supplier_id INTEGER NOT NULL,  -- 供应商必选
                FOREIGN KEY (category_id) REFERENCES MedicineCategories(category_id),
                FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id),
                UNIQUE (name, manufacturer, batch_number)  -- 防重复批号
        )
        """)

        query.exec(""" 
        CREATE TABLE IF NOT EXISTS MedicineCategories(          -- 药品分类表
                category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_name TEXT NOT NULL UNIQUE
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS supplier (             -- 供应商信息表
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,     -- 供应商唯一标识ID
            name TEXT NOT NULL,                                 -- 供应商名字
            contact_person TEXT,                                -- 联系人
            phone TEXT,                                         -- 联系电话
            address TEXT,                                       -- 地址
            email TEXT                                          -- 邮箱
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS purchases (                   -- 进货记录表
            purchases_id INTEGER PRIMARY KEY AUTOINCREMENT,                               -- ID
            medicine_id INTEGER,                                                          -- 药品ID （外键）
            supplier_id INTEGER NOT NULL,                                                 -- 供应商ID（外键）
            quantity INTEGER NOT NULL CHECK (quantity >= 0),                              -- 进货数量
            price REAL NOT NULL CHECK (price >= 0),                                       -- 进货单价
            purchase_date NOT NULL CHECK (purchase_date <= CURRENT_DATE),                 -- 进货日期
            batch_number TEXT,                                                            -- 批号
            expiry_date DATE,                                                             -- 有效期
            FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id),  -- 定义medicine_id为外键，引用medicines表中的id字段
            FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)   -- 定义supplier_id为外键，引用suppliers表中的id字段
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
            id INTEGER PRIMARY KEY AUTOINCREMENT,                           -- 主键ID
            username TEXT NOT NULL,                                         -- 用户名
            password TEXT NOT NULL,                                         -- 密码
            role TEXT                                                       -- 用户角色
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,                               -- 操作用户 ID（外键）
            action TEXT,                                   -- 操作描述
            timestamp DATETIME,                            -- 操作时间
            FOREIGN KEY (user_id) REFERENCES users(id)
    )
        """)


# def get_medicines_model(self):
#     # 创建模型并设置表名
#     self.model = QSqlTableModel(self, self.db)
#     self.model.setTable("medicine")
#     self.model.select()
#     self.model.setQuery("SELECT * FROM medicine LIMIT 100")  # 限制显示前10行数据
#     # 修改表头标题
#     headers = {
#         1: "药品名称",
#         2: "通用名",
#         3: "生产厂家",
#         4: "批号",
#         5: "有效期",
#         6: "采购日期",
#         7: "库存数量",
#         8: "单价",
#         9: "批次条码"
#     }
#     for column, header in headers.items():
#         self.model.setHeaderData(column, Qt.Horizontal, header)
#
#     # 将模型设置到表格视图
#     self.drug_selection_tableView.setModel(self.model)
#
#     # 隐藏第一列（id 列）
#     self.drug_selection_tableView.hideColumn(0)
#     self.drug_selection_tableView.hideColumn(10)
#     self.drug_selection_tableView.hideColumn(11)
#     self.drug_selection_tableView.hideColumn(12)
#     return self.model
#
#
# def get_supplier_model(self):
#     # 创建模型并设置表名
#     self.model = QSqlTableModel(self, self.db)
#     self.model.setTable("supplier")
#     self.model.select()
#     self.model.setQuery("SELECT * FROM medicine LIMIT 100")  # 限制显示前10行数据
#     headers = {
#         0: "id",
#         1: "名称",
#         2: "联系人",
#         3: "电话",
#         4: "地址",
#         5: "邮箱",
#         6: "状态",
#         7: "备注",
#         8: "创建时间",
#         9: "更新时间",
#         10: "创建人",
#         11: "更新人",
#     }
#     for column, header in headers.items():
#         self.model.setHeaderData(column, Qt.Horizontal, header)
#
#     # 将模型设置到表格视图
#     self.sales_records_tableView.setModel(self.model)
#
#     # 隐藏第一列（id 列）
#     self.sales_records_tableView.hideColumn(0)
#     self.sales_records_tableView.hideColumn(10)
#     self.sales_records_tableView.hideColumn(11)
#     self.sales_records_tableView.hideColumn(12)
#     return self.model

    # # 禁用编辑功能以防止用户修改数据
    # self.table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
    # # 设置行选择行为，使用户可以选择整行数据
    # self.table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

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
        3: "生产厂家",
        4: "批号",
        5: "有效期",
        6: "采购日期",
        7: "库存数量",
        8: "单价",
        9: "批次条码"
    }
    HIDDEN_COLUMNS = [0, 10, 11, 12]  # 隐藏的列索引

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="medicine",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class SupplierModel(BaseTableModel):
    HEADERS = {
        1: "名称",
        2: "联系人",
        3: "电话",
        4: "地址",
        5: "邮箱",
        6: "状态",
        7: "备注",
        8: "创建时间",
        9: "更新时间"
    }
    HIDDEN_COLUMNS = [0, 10, 11]  # 隐藏的列索引

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="supplier",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


def get_medicines_model(self):
    self.medicine_model = MedicineModel(self, self.db)
    self.drug_selection_tableView.setModel(self.medicine_model)

    # 应用隐藏列
    for col in self.medicine_model.hidden_columns:
        self.drug_selection_tableView.hideColumn(col)

    return self.medicine_model


def get_supplier_model(self):
    self.supplier_model = SupplierModel(self, self.db)
    self.sales_records_tableView.setModel(self.supplier_model)

    # 应用隐藏列
    for col in self.supplier_model.hidden_columns:
        self.sales_records_tableView.hideColumn(col)

    return self.supplier_model


