from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox


def factory_reset_database(db):
    """
    恢复出厂设置 - 删除所有表和触发器

    Args:
        db: 数据库连接对象
    """
    try:
        query = QSqlQuery(db)

        # 首先禁用外键约束以避免删除时出现问题
        query.exec("PRAGMA foreign_keys = OFF")

        # 获取所有表名
        query.exec("SELECT name FROM sqlite_master WHERE type='table'")
        tables = []
        while query.next():
            tables.append(query.value(0))

        # 删除所有表
        for table in tables:
            if table != "sqlite_sequence":  # 保留sqlite_sequence表
                query.exec(f"DROP TABLE IF EXISTS {table}")

        # 获取所有触发器名并删除
        query.exec("SELECT name FROM sqlite_master WHERE type='trigger'")
        triggers = []
        while query.next():
            triggers.append(query.value(0))

        for trigger in triggers:
            query.exec(f"DROP TRIGGER IF EXISTS {trigger}")

        # 获取所有索引名并删除（除了系统索引）
        query.exec("SELECT name FROM sqlite_master WHERE type='index'")
        indexes = []
        while query.next():
            indexes.append(query.value(0))

        for index in indexes:
            # 跳过系统自动生成的索引
            if not index.startswith("sqlite_"):
                query.exec(f"DROP INDEX IF EXISTS {index}")

        # 重新启用外键约束
        query.exec("PRAGMA foreign_keys = ON")

        # 重新创建sqlite_sequence表（如果需要）
        query.exec("CREATE TABLE IF NOT EXISTS sqlite_sequence(name,seq)")

        return True, "系统已成功恢复出厂设置"

    except Exception as e:
        return False, f"恢复出厂设置失败: {str(e)}"


def confirm_factory_reset(parent_window, db):
    """
    确认并执行出厂重置

    Args:
        parent_window: 父窗口对象
        db: 数据库连接对象
    """
    # 弹出确认对话框
    reply = QMessageBox.question(
        parent_window,
        '确认恢复出厂设置',
        '警告：此操作将删除所有数据、表和触发器，系统将恢复到初始状态。\n\n'
        '请确认您已备份重要数据！\n\n'
        '是否继续执行恢复出厂设置？',
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
    )

    if reply == QMessageBox.StandardButton.Yes:
        try:
            # 执行出厂重置
            success, message = factory_reset_database(db)

            if success:
                # 显示成功消息
                QMessageBox.information(
                    parent_window,
                    '恢复出厂设置成功',
                    f'{message}\n\n系统将重新初始化数据库结构。'
                )

                # 重新初始化数据库结构
                from data.sqlite_data import DatabaseInit
                DatabaseInit()

                return True
            else:
                # 显示错误消息
                QMessageBox.critical(
                    parent_window,
                    '恢复出厂设置失败',
                    message
                )
                return False

        except Exception as e:
            QMessageBox.critical(
                parent_window,
                '错误',
                f'执行恢复出厂设置时发生错误: {str(e)}'
            )
            return False

    return False


# 更完整的出厂重置函数，包含重新初始化数据库结构
def complete_factory_reset(parent_window, db):
    """
    完整的出厂重置流程，包括删除所有数据并重新初始化

    Args:
        parent_window: 父窗口对象
        db: 数据库连接对象
    """
    # 确认操作
    if not confirm_factory_reset(parent_window, db):
        return False

    try:
        # 重新初始化数据库结构
        from data.sqlite_data import DatabaseInit
        DatabaseInit()

        # 显示完成消息
        QMessageBox.information(
            parent_window,
            '完成',
            '系统已恢复出厂设置并重新初始化。\n'
            '所有数据已被清除，数据库结构已重新创建。'
        )

        return True

    except Exception as e:
        QMessageBox.critical(
            parent_window,
            '错误',
            f'重新初始化数据库结构时发生错误: {str(e)}'
        )
        return False
