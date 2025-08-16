import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QTableView, QWidget, QVBoxLayout,
    QPushButton, QDialog, QFormLayout, QLineEdit, QComboBox, QSpinBox,
    QDateEdit, QDialogButtonBox, QMessageBox, QSplitter, QLabel, QHeaderView, QHBoxLayout
)
from PySide6.QtSql import (
    QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel,
    QSqlRelation, QSqlQuery, QSqlRelationalDelegate, QSqlQueryModel
)
from PySide6.QtCore import Qt, QDate


class DatabaseManager:
    """管理数据库连接和多表模型"""

    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("business.db")

        if not self.db.open():
            QMessageBox.critical(
                None, "数据库错误",
                f"无法打开数据库: {self.db.lastError().text()}"
            )
            sys.exit(1)

        # 创建数据库表结构
        self.create_tables()

    def create_tables(self):
        """创建所需的数据库表"""
        queries = [
            """CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                address TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                stock INTEGER DEFAULT 0,
                description TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                order_date DATE NOT NULL,
                status TEXT DEFAULT 'Pending',
                FOREIGN KEY(customer_id) REFERENCES customers(id),
                FOREIGN KEY(product_id) REFERENCES products(id)
            )"""
        ]

        for query_str in queries:
            query = QSqlQuery()
            if not query.exec(query_str):
                QMessageBox.critical(
                    None, "数据库错误",
                    f"创建表失败: {query.lastError().text()}"
                )

    def get_customers_model(self):
        """客户表模型"""
        model = QSqlTableModel()
        model.setTable("customers")
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(1, Qt.Horizontal, "姓名")
        model.setHeaderData(2, Qt.Horizontal, "邮箱")
        model.setHeaderData(3, Qt.Horizontal, "电话")
        model.setHeaderData(4, Qt.Horizontal, "地址")
        return model

    def get_products_model(self):
        """产品表模型"""
        model = QSqlTableModel()
        model.setTable("products")
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(1, Qt.Horizontal, "产品名称")
        model.setHeaderData(2, Qt.Horizontal, "价格")
        model.setHeaderData(3, Qt.Horizontal, "库存")
        model.setHeaderData(4, Qt.Horizontal, "描述")
        return model

    def get_orders_model(self):
        """订单表关系模型"""
        model = QSqlRelationalTableModel()
        model.setTable("orders")
        model.setRelation(1, QSqlRelation("customers", "id", "name"))  # 客户ID -> 客户姓名
        model.setRelation(2, QSqlRelation("products", "id", "name"))  # 产品ID -> 产品名称
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.select()

        # 设置表头
        model.setHeaderData(0, Qt.Horizontal, "订单ID")
        model.setHeaderData(1, Qt.Horizontal, "客户")
        model.setHeaderData(2, Qt.Horizontal, "产品")
        model.setHeaderData(3, Qt.Horizontal, "数量")
        model.setHeaderData(4, Qt.Horizontal, "日期")
        model.setHeaderData(5, Qt.Horizontal, "状态")

        return model

    def get_orders_summary_model(self):
        """订单汇总查询模型"""
        query = QSqlQuery()
        query.exec("""
            SELECT 
                orders.id AS order_id,
                customers.name AS customer,
                products.name AS product,
                orders.quantity,
                orders.order_date,
                orders.status,
                (products.price * orders.quantity) AS total
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            JOIN products ON orders.product_id = products.id
        """)

        model = QSqlQueryModel()
        model.setQuery(query)

        # 设置表头
        model.setHeaderData(0, Qt.Horizontal, "订单ID")
        model.setHeaderData(1, Qt.Horizontal, "客户")
        model.setHeaderData(2, Qt.Horizontal, "产品")
        model.setHeaderData(3, Qt.Horizontal, "数量")
        model.setHeaderData(4, Qt.Horizontal, "日期")
        model.setHeaderData(5, Qt.Horizontal, "状态")
        model.setHeaderData(6, Qt.Horizontal, "总价")

        return model


class OrderDialog(QDialog):
    """添加/编辑订单的对话框"""

    def __init__(self, db_manager, parent=None, order_id=None):
        super().__init__(parent)
        self.db_manager = db_manager
        self.order_id = order_id

        self.setWindowTitle("添加订单" if not order_id else "编辑订单")
        self.setMinimumSize(400, 300)

        layout = QFormLayout(self)

        # 客户选择
        self.customer_combo = QComboBox()
        self.populate_customers()
        layout.addRow("客户:", self.customer_combo)

        # 产品选择
        self.product_combo = QComboBox()
        self.populate_products()
        layout.addRow("产品:", self.product_combo)

        # 数量
        self.quantity_spin = QSpinBox()
        self.quantity_spin.setRange(1, 100)
        layout.addRow("数量:", self.quantity_spin)

        # 日期
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        layout.addRow("日期:", self.date_edit)

        # 状态
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Pending", "Processing", "Shipped", "Delivered", "Cancelled"])
        layout.addRow("状态:", self.status_combo)

        # 按钮
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

        # 如果是编辑模式，加载现有数据
        if order_id:
            self.load_order_data()

    def populate_customers(self):
        """填充客户下拉框"""
        query = QSqlQuery("SELECT id, name FROM customers")
        while query.next():
            self.customer_combo.addItem(query.value("name"), query.value("id"))

    def populate_products(self):
        """填充产品下拉框"""
        query = QSqlQuery("SELECT id, name FROM products")
        while query.next():
            self.product_combo.addItem(query.value("name"), query.value("id"))

    def load_order_data(self):
        """加载订单数据"""
        query = QSqlQuery()
        query.prepare("""
            SELECT customer_id, product_id, quantity, order_date, status 
            FROM orders WHERE id = ?
        """)
        query.addBindValue(self.order_id)
        query.exec()

        if query.next():
            # 设置客户
            customer_id = query.value("customer_id")
            customer_index = self.customer_combo.findData(customer_id)
            if customer_index >= 0:
                self.customer_combo.setCurrentIndex(customer_index)

            # 设置产品
            product_id = query.value("product_id")
            product_index = self.product_combo.findData(product_id)
            if product_index >= 0:
                self.product_combo.setCurrentIndex(product_index)

            # 设置其他字段
            self.quantity_spin.setValue(query.value("quantity"))
            self.date_edit.setDate(query.value("order_date"))
            self.status_combo.setCurrentText(query.value("status"))

    def get_order_data(self):
        """返回订单数据"""
        return {
            "customer_id": self.customer_combo.currentData(),
            "product_id": self.product_combo.currentData(),
            "quantity": self.quantity_spin.value(),
            "order_date": self.date_edit.date().toString("yyyy-MM-dd"),
            "status": self.status_combo.currentText()
        }


class MainWindow(QMainWindow):
    """主应用程序窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("多表数据库管理系统")
        self.resize(1200, 800)

        # 初始化数据库
        self.db_manager = DatabaseManager()

        # 创建UI
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        # 创建标签页
        self.tab_widget = QTabWidget()

        # 客户标签页
        self.customers_tab = self.create_table_tab(
            self.db_manager.get_customers_model(), "客户"
        )
        self.tab_widget.addTab(self.customers_tab, "客户管理")

        # 产品标签页
        self.products_tab = self.create_table_tab(
            self.db_manager.get_products_model(), "产品"
        )
        self.tab_widget.addTab(self.products_tab, "产品管理")

        # 订单标签页
        self.orders_tab = self.create_table_tab(
            self.db_manager.get_orders_model(), "订单"
        )
        self.tab_widget.addTab(self.orders_tab, "订单管理")

        # 订单汇总标签页
        self.summary_tab = self.create_table_tab(
            self.db_manager.get_orders_summary_model(), "订单汇总"
        )
        self.tab_widget.addTab(self.summary_tab, "订单汇总")

        main_layout.addWidget(self.tab_widget)
        self.setCentralWidget(central_widget)

        # 添加订单按钮
        add_order_btn = QPushButton("添加新订单")
        add_order_btn.clicked.connect(self.add_order)
        main_layout.addWidget(add_order_btn)

    def create_table_tab(self, model, title):
        """创建包含表格视图的标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # 创建表格视图
        table_view = QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_view.setSelectionBehavior(QTableView.SelectRows)

        # 对于订单表，设置关系委托
        if title == "订单":
            delegate = QSqlRelationalDelegate(table_view)
            table_view.setItemDelegate(delegate)
            # 添加编辑和删除按钮
            btn_layout = QHBoxLayout()

            edit_btn = QPushButton("编辑订单")
            edit_btn.clicked.connect(lambda: self.edit_order(table_view))
            btn_layout.addWidget(edit_btn)

            delete_btn = QPushButton("删除订单")
            delete_btn.clicked.connect(lambda: self.delete_order(table_view))
            btn_layout.addWidget(delete_btn)

            layout.addLayout(btn_layout)

        layout.addWidget(table_view)
        return tab

    def get_selected_id(self, table_view):
        """获取选中行的ID"""
        selection = table_view.selectionModel().selectedRows(0)
        if selection:
            return selection[0].data()
        return None

    def add_order(self):
        """添加新订单"""
        dialog = OrderDialog(self.db_manager, self)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_order_data()

            query = QSqlQuery()
            query.prepare("""
                INSERT INTO orders (customer_id, product_id, quantity, order_date, status)
                VALUES (?, ?, ?, ?, ?)
            """)
            query.addBindValue(data["customer_id"])
            query.addBindValue(data["product_id"])
            query.addBindValue(data["quantity"])
            query.addBindValue(data["order_date"])
            query.addBindValue(data["status"])

            if not query.exec():
                QMessageBox.critical(
                    self, "数据库错误",
                    f"添加订单失败: {query.lastError().text()}"
                )
            else:
                # 刷新订单模型
                self.refresh_models()

    def edit_order(self, table_view):
        """编辑现有订单"""
        order_id = self.get_selected_id(table_view)
        if not order_id:
            QMessageBox.warning(self, "选择错误", "请先选择一个订单")
            return

        dialog = OrderDialog(self.db_manager, self, order_id)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_order_data()

            query = QSqlQuery()
            query.prepare("""
                UPDATE orders 
                SET customer_id = ?, product_id = ?, quantity = ?, order_date = ?, status = ?
                WHERE id = ?
            """)
            query.addBindValue(data["customer_id"])
            query.addBindValue(data["product_id"])
            query.addBindValue(data["quantity"])
            query.addBindValue(data["order_date"])
            query.addBindValue(data["status"])
            query.addBindValue(order_id)

            if not query.exec():
                QMessageBox.critical(
                    self, "数据库错误",
                    f"更新订单失败: {query.lastError().text()}"
                )
            else:
                # 刷新订单模型
                self.refresh_models()

    def delete_order(self, table_view):
        """删除订单"""
        order_id = self.get_selected_id(table_view)
        if not order_id:
            QMessageBox.warning(self, "选择错误", "请先选择一个订单")
            return

        reply = QMessageBox.question(
            self, "确认删除",
            "确定要删除此订单吗?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            query = QSqlQuery()
            query.prepare("DELETE FROM orders WHERE id = ?")
            query.addBindValue(order_id)

            if not query.exec():
                QMessageBox.critical(
                    self, "数据库错误",
                    f"删除订单失败: {query.lastError().text()}"
                )
            else:
                # 刷新订单模型
                self.refresh_models()

    def refresh_models(self):
        """刷新所有模型"""
        self.db_manager.get_customers_model().select()
        self.db_manager.get_products_model().select()
        self.db_manager.get_orders_model().select()
        self.db_manager.get_orders_summary_model().setQuery(
            self.db_manager.get_orders_summary_model().query()
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 检查SQLite驱动
    if "QSQLITE" not in QSqlDatabase.drivers():
        QMessageBox.critical(
            None, "驱动错误",
            "SQLite驱动(QSQLITE)不可用，无法运行此应用"
        )
        sys.exit(1)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())