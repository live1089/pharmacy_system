from PySide6.QtSql import QSqlDatabase, QSqlQuery
class QueryData(object):
    def __init__(self, perent=None):
        super().__init__()


    def get_query(self):
        query = QSqlQuery()
        query.exec("")


# base_table_model.py
from PySide6.QtSql import QSqlTableModel, QSqlDatabase
from PySide6.QtCore import QObject

class BaseTableModel(QSqlTableModel):
    """
    任何表都可以直接继承/实例化此类。
    只需在创建时传入：
      table_name: 数据库里的真实表名
      display_cols: 界面要显示的列 ['id','name','stock',...]
    """
    def __init__(self, table_name: str,
                 display_cols: list = None,
                 parent: QObject = None):
        super().__init__(parent, QSqlDatabase.database())
        self.setTable(table_name)
        if display_cols:
            # 隐藏不需要的列
            all_cols = [self.headerData(i, 1)
                        for i in range(self.columnCount())]
            for col in all_cols:
                if col not in display_cols:
                    idx = self.fieldIndex(col)
                    self.setHeaderData(idx, 1, "")  # 或者 self.removeColumn(idx)
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.select()

    # 下面三个函数足够覆盖 90% 查询需求
    def set_filter_like(self, column: str, keyword: str):
        self.setFilter(f"{column} LIKE '%{keyword}%'")
        self.select()

    def set_filter_exact(self, column: str, value):
        self.setFilter(f"{column}='{value}'")
        self.select()

    def clear_filter(self):
        self.setFilter("")
        self.select()
