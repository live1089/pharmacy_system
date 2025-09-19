# 在 data/clean_up_useless_data.py 文件中添加以下代码

from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox
import sqlite3


class DataCleaner:
    def __init__(self, db):
        self.db = db

    def clean_expired_data(self):
        """
        清理过期数据
        """
        query = QSqlQuery(self.db)
        cleaned_count = 0

        try:
            # 1. 清理过期很久的药品监控记录(过期超过30天)
            query.exec("""
                DELETE FROM expiring_medicines 
                WHERE days_until_expiry < -30
            """)
            expired_medicines_count = query.numRowsAffected()
            cleaned_count += expired_medicines_count

            # 2. 清理过期的库存记录(可选)
            query.exec("""
                DELETE FROM stock 
                WHERE quantity = 0
            """)
            zero_stock_count = query.numRowsAffected()
            cleaned_count += zero_stock_count

            # 3. 清理孤立的采购明细(没有对应主表的记录)
            query.exec("""
                DELETE FROM purchase_detail 
                WHERE order_id NOT IN (SELECT order_id FROM purchase_order)
            """)
            orphaned_purchase_detail_count = query.numRowsAffected()
            cleaned_count += orphaned_purchase_detail_count

            # 4. 清理孤立的入库明细
            query.exec("""
                DELETE FROM stock_in_detail 
                WHERE in_id NOT IN (SELECT in_id FROM stock_in_main)
            """)
            orphaned_stock_in_detail_count = query.numRowsAffected()
            cleaned_count += orphaned_stock_in_detail_count

            # 5. 清理孤立的出库明细
            query.exec("""
                DELETE FROM stock_out_detail 
                WHERE out_id NOT IN (SELECT out_id FROM stock_out_main)
            """)
            orphaned_stock_out_detail_count = query.numRowsAffected()
            cleaned_count += orphaned_stock_out_detail_count

            # 6. 清理孤立的销售明细
            query.exec("""
                DELETE FROM sale_details 
                WHERE sales_id NOT IN (SELECT sales_id FROM sales)
            """)
            orphaned_sale_details_count = query.numRowsAffected()
            cleaned_count += orphaned_sale_details_count

            return True, f"清理完成，共清理 {cleaned_count} 条无用数据记录:\n" \
                         f"- 过期药品监控记录: {expired_medicines_count} 条\n" \
                         f"- 零库存记录: {zero_stock_count} 条\n" \
                         f"- 孤立采购明细: {orphaned_purchase_detail_count} 条\n" \
                         f"- 孤立入库明细: {orphaned_stock_in_detail_count} 条\n" \
                         f"- 孤立出库明细: {orphaned_stock_out_detail_count} 条\n" \
                         f"- 孤立销售明细: {orphaned_sale_details_count} 条"

        except Exception as e:
            return False, f"清理过程中发生错误: {str(e)}"

    def optimize_database(self):
        """
        优化数据库(整理碎片，减小数据库文件大小)
        """
        try:
            query = QSqlQuery(self.db)
            query.exec("VACUUM")
            return True, "数据库优化完成"
        except Exception as e:
            return False, f"数据库优化失败: {str(e)}"

    def clean_logs(self, days=30):
        """
        清理日志记录(默认清理30天前的日志)
        """
        query = QSqlQuery(self.db)
        try:
            query.prepare("""
                DELETE FROM logs 
                WHERE timestamp < datetime('now', '-{} days')
            """.format(days))
            query.exec()
            deleted_count = query.numRowsAffected()
            return True, f"已清理 {deleted_count} 条 {days} 天前的日志记录"
        except Exception as e:
            return False, f"清理日志失败: {str(e)}"

    def get_database_size(self):
        """
        获取数据库大小信息
        """
        try:
            query = QSqlQuery(self.db)
            query.exec("PRAGMA page_count")
            page_count = 0
            if query.next():
                page_count = query.value(0)

            query.exec("PRAGMA page_size")
            page_size = 0
            if query.next():
                page_size = query.value(0)

            size_bytes = page_count * page_size
            size_mb = size_bytes / (1024 * 1024)

            return True, f"数据库大小: {size_mb:.2f} MB ({size_bytes} 字节)"
        except Exception as e:
            return False, f"获取数据库大小失败: {str(e)}"


def clean_up_useless_data(parent_window):
    """
    清理系统垃圾的主函数
    """
    from data.sqlite_data import DatabaseInit

    try:
        # 创建数据清理器实例
        cleaner = DataCleaner(parent_window.db)

        # 获取清理前的数据库大小
        size_success, size_info = cleaner.get_database_size()
        if size_success:
            print(f"清理前: {size_info}")

        # 执行清理操作
        clean_success, clean_msg = cleaner.clean_expired_data()
        if not clean_success:
            QMessageBox.warning(parent_window, "清理失败", clean_msg)
            return

        # 执行数据库优化
        optimize_success, optimize_msg = cleaner.optimize_database()
        if not optimize_success:
            QMessageBox.warning(parent_window, "优化失败", optimize_msg)
            return

        # 获取清理后的数据库大小
        size_success_after, size_info_after = cleaner.get_database_size()
        if size_success_after:
            print(f"清理后: {size_info_after}")

        # 显示清理结果
        result_msg = f"{clean_msg}\n\n{optimize_msg}"
        if size_success and size_success_after:
            result_msg += f"\n\n数据库大小变化:\n- 清理前: {size_info}\n- 清理后: {size_info_after}"

        QMessageBox.information(parent_window, "清理完成", result_msg)

    except Exception as e:
        QMessageBox.critical(parent_window, "错误", f"清理过程中发生未知错误: {str(e)}")
