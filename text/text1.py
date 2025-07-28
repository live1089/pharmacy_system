import sys
import sqlite3
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableView, QTreeView, QSplitter, QLabel, QPushButton,
    QLineEdit, QComboBox, QDateEdit, QFormLayout, QMessageBox
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtCore import Qt, QDate


class PharmacySystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("药房管理系统")
        self.setGeometry(100, 100, 900, 600)

        # 初始化数据库
        self.init_database()

        # 创建主界面
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 创建分割器
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)

        # 左侧：数据管理面板
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        # 右侧：数据显示面板
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([300, 700])

        # === 左侧面板：数据管理 ===
        # 药品管理
        med_group = QWidget()
        med_layout = QFormLayout(med_group)
        self.med_name_input = QLineEdit()
        self.med_category_combo = QComboBox()
        self.med_category_combo.addItems(["处方药", "非处方药", "抗生素", "麻醉药"])
        self.med_price_input = QLineEdit()
        self.med_submit = QPushButton("添加药品")
        self.med_submit.clicked.connect(self.add_medicine)

        med_layout.addRow("药品名称:", self.med_name_input)
        med_layout.addRow("药品类别:", self.med_category_combo)
        med_layout.addRow("价格:", self.med_price_input)
        med_layout.addRow(self.med_submit)

        # 库存管理
        stock_group = QWidget()
        stock_layout = QFormLayout(stock_group)
        self.stock_med_combo = QComboBox()
        self.stock_quantity_input = QLineEdit()
        self.stock_batch_input = QLineEdit()
        self.stock_expiry_input = QDateEdit()
        self.stock_expiry_input.setDate(QDate.currentDate().addYears(1))
        self.stock_submit = QPushButton("入库")
        self.stock_submit.clicked.connect(self.add_stock)

        stock_layout.addRow("药品:", self.stock_med_combo)
        stock_layout.addRow("数量:", self.stock_quantity_input)
        stock_layout.addRow("批号:", self.stock_batch_input)
        stock_layout.addRow("有效期:", self.stock_expiry_input)
        stock_layout.addRow(self.stock_submit)

        # 销售管理
        sale_group = QWidget()
        sale_layout = QFormLayout(sale_group)
        self.sale_med_combo = QComboBox()
        self.sale_quantity_input = QLineEdit()
        self.sale_customer_input = QLineEdit()
        self.sale_date_input = QDateEdit()
        self.sale_date_input.setDate(QDate.currentDate())
        self.sale_submit = QPushButton("销售记录")
        self.sale_submit.clicked.connect(self.add_sale)

        sale_layout.addRow("药品:", self.sale_med_combo)
        sale_layout.addRow("数量:", self.sale_quantity_input)
        sale_layout.addRow("顾客:", self.sale_customer_input)
        sale_layout.addRow("日期:", self.sale_date_input)
        sale_layout.addRow(self.sale_submit)

        # 添加控件到左侧面板
        left_layout.addWidget(QLabel("<b>药品管理</b>"))
        left_layout.addWidget(med_group)
        left_layout.addWidget(QLabel("<b>库存管理</b>"))
        left_layout.addWidget(stock_group)
        left_layout.addWidget(QLabel("<b>销售管理</b>"))
        left_layout.addWidget(sale_group)

        # === 右侧面板：数据显示 ===
        # 标签页切换
        self.tab_buttons = QHBoxLayout()
        self.btn_medicines = QPushButton("药品信息")
        self.btn_inventory = QPushButton("库存状态")
        self.btn_sales = QPushButton("销售记录")
        self.btn_expiry = QPushButton("过期预警")

        self.btn_medicines.clicked.connect(lambda: self.show_data("medicines"))
        self.btn_inventory.clicked.connect(lambda: self.show_data("inventory"))
        self.btn_sales.clicked.connect(lambda: self.show_data("sales"))
        self.btn_expiry.clicked.connect(lambda: self.show_data("expiry"))

        self.tab_buttons.addWidget(self.btn_medicines)
        self.tab_buttons.addWidget(self.btn_inventory)
        self.tab_buttons.addWidget(self.btn_sales)
        self.tab_buttons.addWidget(self.btn_expiry)

        # 数据显示表格
        self.data_table = QTableView()

        # 添加到右侧面板
        right_layout.addLayout(self.tab_buttons)
        right_layout.addWidget(self.data_table)

        # 初始化数据
        self.load_medicine_combo()
        self.show_data("medicines")

    def init_database(self):
        """初始化数据库和表结构"""
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("pharmacy.db")

        if not self.db.open():
            QMessageBox.critical(self, "数据库错误", "无法打开数据库")
            return False

        # 创建表结构
        queries = [
            # 药品信息表
            """CREATE TABLE IF NOT EXISTS medicines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )""",

            # 库存表
            """CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                medicine_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                batch_number TEXT NOT NULL,
                expiry_date DATE NOT NULL,
                FOREIGN KEY(medicine_id) REFERENCES medicines(id)
            )""",

            # 销售记录表
            """CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                medicine_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                customer TEXT,
                sale_date DATE NOT NULL,
                FOREIGN KEY(medicine_id) REFERENCES medicines(id)
            )"""
        ]

        query = QSqlQuery()
        for q in queries:
            if not query.exec(q):
                QMessageBox.critical(self, "数据库错误", f"创建表失败: {query.lastError().text()}")

    def load_medicine_combo(self):
        """加载药品到下拉框"""
        self.stock_med_combo.clear()
        self.sale_med_combo.clear()

        query = QSqlQuery("SELECT id, name FROM medicines")
        while query.next():
            med_id = query.value(0)
            med_name = query.value(1)
            self.stock_med_combo.addItem(med_name, med_id)
            self.sale_med_combo.addItem(med_name, med_id)

    def add_medicine(self):
        """添加新药品"""
        name = self.med_name_input.text().strip()
        category = self.med_category_combo.currentText()
        price = self.med_price_input.text().strip()

        if not name or not price:
            QMessageBox.warning(self, "输入错误", "药品名称和价格不能为空")
            return

        try:
            price_val = float(price)
            if price_val <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的价格")
            return

        query = QSqlQuery()
        query.prepare("INSERT INTO medicines (name, category, price) VALUES (?, ?, ?)")
        query.addBindValue(name)
        query.addBindValue(category)
        query.addBindValue(price_val)

        if not query.exec():
            QMessageBox.critical(self, "数据库错误", f"添加药品失败: {query.lastError().text()}")
        else:
            QMessageBox.information(self, "成功", "药品添加成功")
            self.med_name_input.clear()
            self.med_price_input.clear()
            self.load_medicine_combo()
            self.show_data("medicines")

    def add_stock(self):
        """药品入库"""
        med_id = self.stock_med_combo.currentData()
        quantity = self.stock_quantity_input.text().strip()
        batch = self.stock_batch_input.text().strip()
        expiry = self.stock_expiry_input.date().toString("yyyy-MM-dd")

        if not quantity or not batch:
            QMessageBox.warning(self, "输入错误", "数量和批号不能为空")
            return

        try:
            quantity_val = int(quantity)
            if quantity_val <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的数量")
            return

        query = QSqlQuery()
        query.prepare("INSERT INTO inventory (medicine_id, quantity, batch_number, expiry_date) VALUES (?, ?, ?, ?)")
        query.addBindValue(med_id)
        query.addBindValue(quantity_val)
        query.addBindValue(batch)
        query.addBindValue(expiry)

        if not query.exec():
            QMessageBox.critical(self, "数据库错误", f"入库失败: {query.lastError().text()}")
        else:
            QMessageBox.information(self, "成功", "药品入库成功")
            self.stock_quantity_input.clear()
            self.stock_batch_input.clear()
            self.show_data("inventory")

    def add_sale(self):
        """添加销售记录"""
        med_id = self.sale_med_combo.currentData()
        quantity = self.sale_quantity_input.text().strip()
        customer = self.sale_customer_input.text().strip()
        sale_date = self.sale_date_input.date().toString("yyyy-MM-dd")

        if not quantity:
            QMessageBox.warning(self, "输入错误", "数量不能为空")
            return

        try:
            quantity_val = int(quantity)
            if quantity_val <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的数量")
            return

        # 检查库存是否足够
        query = QSqlQuery()
        query.prepare("SELECT SUM(quantity) FROM inventory WHERE medicine_id = ? AND expiry_date > DATE('now')")
        query.addBindValue(med_id)
        query.exec()

        if query.next():
            stock = query.value(0) or 0
            if stock < quantity_val:
                QMessageBox.warning(self, "库存不足", f"当前库存不足，可用数量: {stock}")
                return

        # 添加销售记录
        query.prepare("INSERT INTO sales (medicine_id, quantity, customer, sale_date) VALUES (?, ?, ?, ?)")
        query.addBindValue(med_id)
        query.addBindValue(quantity_val)
        query.addBindValue(customer)
        query.addBindValue(sale_date)

        if not query.exec():
            QMessageBox.critical(self, "数据库错误", f"销售记录失败: {query.lastError().text()}")
        else:
            QMessageBox.information(self, "成功", "销售记录添加成功")
            self.sale_quantity_input.clear()
            self.sale_customer_input.clear()
            self.show_data("sales")

    def show_data(self, data_type):
        """显示不同类型的数据"""
        model = QSqlQueryModel()

        if data_type == "medicines":
            model.setQuery("SELECT id, name, category, price FROM medicines")
            model.setHeaderData(0, Qt.Horizontal, "ID")
            model.setHeaderData(1, Qt.Horizontal, "药品名称")
            model.setHeaderData(2, Qt.Horizontal, "类别")
            model.setHeaderData(3, Qt.Horizontal, "价格")

        elif data_type == "inventory":
            # 使用SQL JOIN获取库存详情
            model.setQuery("""
                SELECT 
                    m.name AS '药品名称',
                    i.batch_number AS '批号',
                    i.quantity AS '数量',
                    i.expiry_date AS '有效期',
                    (julianday(i.expiry_date) - julianday('now')) AS '剩余天数'
                FROM inventory i
                JOIN medicines m ON i.medicine_id = m.id
                WHERE i.expiry_date > DATE('now')
                ORDER BY i.expiry_date
            """)

        elif data_type == "sales":
            # 使用SQL JOIN获取销售详情
            model.setQuery("""
                SELECT 
                    s.sale_date AS '销售日期',
                    m.name AS '药品名称',
                    s.quantity AS '数量',
                    s.customer AS '顾客'
                FROM sales s
                JOIN medicines m ON s.medicine_id = m.id
                ORDER BY s.sale_date DESC
            """)

        elif data_type == "expiry":
            # 过期预警查询
            model.setQuery("""
                SELECT 
                    m.name AS '药品名称',
                    i.batch_number AS '批号',
                    i.quantity AS '数量',
                    i.expiry_date AS '有效期',
                    (julianday(i.expiry_date) - julianday('now')) AS '剩余天数'
                FROM inventory i
                JOIN medicines m ON i.medicine_id = m.id
                WHERE i.expiry_date BETWEEN DATE('now') AND DATE('now', '+30 days')
                ORDER BY i.expiry_date
            """)

        self.data_table.setModel(model)
        self.data_table.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PharmacySystem()
    window.show()
    sys.exit(app.exec())