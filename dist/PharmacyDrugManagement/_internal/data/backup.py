# data/backup.py
import os
import shutil
import sys
from datetime import datetime

from PySide6.QtWidgets import QMessageBox, QFileDialog
from config_manager import ConfigManager

class DatabaseBackup:
    def __init__(self, db, parent_window):
        self.db = db
        self.parent_window = parent_window
        self.config = ConfigManager()
        self.db_path = self.config.get_db_path()
        self.backup_dir = self.config.get_backup_dir()

    def backup_database(self):
        """
        手动备份数据库
        """
        try:
            # 检查数据库文件是否存在
            if not os.path.exists(self.db_path):
                QMessageBox.warning(self.parent_window, "备份失败", f"数据库文件不存在: {self.db_path}")
                return False

            # 生成备份文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"pharmacy_backup_{timestamp}.db"

            # 打开文件保存对话框
            backup_path, _ = QFileDialog.getSaveFileName(
                self.parent_window,
                "保存数据库备份",
                backup_filename,
                "SQLite Database Files (*.db);;All Files (*)"
            )

            if not backup_path:
                return False  # 用户取消了操作

            # 执行备份
            shutil.copy2(self.db_path, backup_path)

            QMessageBox.information(
                self.parent_window,
                "备份成功",
                f"数据库已成功备份到:\n{backup_path}"
            )
            return True

        except Exception as e:
            QMessageBox.critical(
                self.parent_window,
                "备份失败",
                f"备份数据库时发生错误:\n{str(e)}"
            )
            return False

    def restore_database(self):
        """
        从备份恢复数据库
        """
        try:
            # 打开文件选择对话框选择备份文件
            backup_path, _ = QFileDialog.getOpenFileName(
                self.parent_window,
                "选择数据库备份文件",
                "",
                "SQLite Database Files (*.db);;All Files (*)"
            )

            if not backup_path:
                return False  # 用户取消了操作

            # 检查备份文件是否存在
            if not os.path.exists(backup_path):
                QMessageBox.warning(self.parent_window, "恢复失败", "选择的备份文件不存在")
                return False

            # 确认恢复操作
            reply = QMessageBox.question(
                self.parent_window,
                "确认恢复",
                "恢复数据库将覆盖当前数据，所有未备份的更改将会丢失。\n\n确定要继续吗？",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.No:
                return False

            # 执行恢复
            shutil.copy2(backup_path, self.db_path)

            QMessageBox.information(
                self.parent_window,
                "恢复成功",
                "数据库已成功从备份恢复。\n程序需要重启以应用更改。"
            )
            return True

        except Exception as e:
            QMessageBox.critical(
                self.parent_window,
                "恢复失败",
                f"恢复数据库时发生错误:\n{str(e)}"
            )
            return False

    def auto_backup_database(self):
        """
        自动备份数据库到指定目录
        """
        try:
            # 检查数据库文件是否存在
            if not os.path.exists(self.db_path):
                QMessageBox.warning(self.parent_window, "备份失败", f"数据库文件不存在: {self.db_path}")
                return False

            # 创建备份目录（如果不存在）
            if not os.path.exists(self.backup_dir):
                os.makedirs(self.backup_dir)

            # 生成备份文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"pharmacy_backup_{timestamp}.db"
            backup_path = os.path.join(self.backup_dir, backup_filename)

            # 执行备份
            shutil.copy2(self.db_path, backup_path)

            # 清理旧备份（保留最近7天的备份）
            self.cleanup_old_backups(days=7)

            print(f"自动备份完成: {backup_path}")
            return True

        except Exception as e:
            QMessageBox.critical(
                self.parent_window,
                "自动备份失败",
                f"自动备份数据库时发生错误:\n{str(e)}"
            )
            return False

    def cleanup_old_backups(self, days=7):
        """
        清理指定天数之前的备份文件

        Args:
            days: 保留天数
        """
        try:
            # 检查备份目录是否存在
            if not os.path.exists(self.backup_dir):
                return

            # 计算删除阈值时间
            cutoff_time = datetime.now().timestamp() - (days * 24 * 60 * 60)

            # 遍历备份目录中的文件
            for filename in os.listdir(self.backup_dir):
                if filename.startswith("pharmacy_backup_") and filename.endswith(".db"):
                    file_path = os.path.join(self.backup_dir, filename)
                    # 检查文件修改时间
                    if os.path.getmtime(file_path) < cutoff_time:
                        os.remove(file_path)
                        print(f"已删除旧备份: {filename}")

        except Exception as e:
            print(f"清理旧备份时出错: {str(e)}")

    def get_backup_info(self):
        """
        获取备份信息
        """
        try:
            backup_count = 0
            total_size = 0
            latest_backup = None

            if os.path.exists(self.backup_dir):
                for filename in os.listdir(self.backup_dir):
                    if filename.startswith("pharmacy_backup_") and filename.endswith(".db"):
                        backup_count += 1
                        file_path = os.path.join(self.backup_dir, filename)
                        total_size += os.path.getsize(file_path)

                        if latest_backup is None or os.path.getmtime(file_path) > os.path.getmtime(
                                os.path.join(self.backup_dir, latest_backup)):
                            latest_backup = filename

            # 转换文件大小为可读格式
            size_str = self.format_file_size(total_size)

            return {
                'backup_count': backup_count,
                'total_size': size_str,
                'latest_backup': latest_backup
            }
        except Exception as e:
            print(f"获取备份信息时出错: {str(e)}")
            return {
                'backup_count': 0,
                'total_size': '0 B',
                'latest_backup': None
            }

    def format_file_size(self, size_bytes):
        """
        格式化文件大小为可读格式
        """
        if size_bytes == 0:
            return "0 B"

        size_names = ["B", "KB", "MB", "GB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1

        return f"{size_bytes:.1f} {size_names[i]}"


def backup_database(parent_window, db_path="_internal/data/pharmacy.db"):
    """
    备份数据库文件

    Args:
        parent_window: 父窗口对象
        db_path: 数据库文件路径
    """
    try:
        # 检查数据库文件是否存在
        if not os.path.exists(db_path):
            QMessageBox.warning(parent_window, "备份失败", f"数据库文件不存在: {db_path}")
            return False

        # 生成备份文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"pharmacy_backup_{timestamp}.db"

        # 打开文件保存对话框
        backup_path, _ = QFileDialog.getSaveFileName(
            parent_window,
            "保存数据库备份",
            backup_filename,
            "SQLite Database Files (*.db);;All Files (*)"
        )

        if not backup_path:
            return False  # 用户取消了操作

        # 执行备份
        shutil.copy2(db_path, backup_path)

        QMessageBox.information(
            parent_window,
            "备份成功",
            f"数据库已成功备份到:\n{backup_path}"
        )
        return True

    except Exception as e:
        QMessageBox.critical(
            parent_window,
            "备份失败",
            f"备份数据库时发生错误:\n{str(e)}"
        )
        return False


def restore_database(parent_window, db_path="_internal/data/pharmacy.db"):
    """
    从备份恢复数据库文件

    Args:
        parent_window: 父窗口对象
        db_path: 数据库文件路径
    """
    try:
        # 打开文件选择对话框选择备份文件
        backup_path, _ = QFileDialog.getOpenFileName(
            parent_window,
            "选择数据库备份文件",
            "",
            "SQLite Database Files (*.db);;All Files (*)"
        )

        if not backup_path:
            return False  # 用户取消了操作

        # 检查备份文件是否存在
        if not os.path.exists(backup_path):
            QMessageBox.warning(parent_window, "恢复失败", "选择的备份文件不存在")
            return False

        # 确认恢复操作
        reply = QMessageBox.question(
            parent_window,
            "确认恢复",
            "恢复数据库将覆盖当前数据，所有未备份的更改将会丢失。\n\n确定要继续吗？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.No:
            return False

        # 执行恢复
        shutil.copy2(backup_path, db_path)

        QMessageBox.information(
            parent_window,
            "恢复成功",
            "数据库已成功从备份恢复。\n程序需要重启以应用更改。"
        )
        return True

    except Exception as e:
        QMessageBox.critical(
            parent_window,
            "恢复失败",
            f"恢复数据库时发生错误:\n{str(e)}"
        )
        return False


def auto_backup_database(parent_window, db_path, backup_dir):
    """
    自动备份数据库到指定目录

    Args:
        parent_window: 父窗口对象
        db_path: 数据库文件路径
        backup_dir: 备份目录
    """
    try:
        # 检查数据库文件是否存在
        if not os.path.exists(db_path):
            QMessageBox.warning(parent_window, "备份失败", f"数据库文件不存在: {db_path}")
            return False

        # 创建备份目录（如果不存在）
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # 生成备份文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"pharmacy_backup_{timestamp}.db"
        backup_path = os.path.join(backup_dir, backup_filename)

        # 执行备份
        shutil.copy2(db_path, backup_path)

        # 清理旧备份（保留最近7天的备份）
        cleanup_old_backups(backup_dir, days=7)

        QMessageBox.warning(parent_window, "自动备份完成", f"备份地址: {backup_path}")
        return True

    except Exception as e:
        QMessageBox.critical(
            parent_window,
            "自动备份失败",
            f"自动备份数据库时发生错误:\n{str(e)}"
        )
        return False


def cleanup_old_backups(backup_dir, days=7):
    """
    清理指定天数之前的备份文件

    Args:
        backup_dir: 备份目录
        days: 保留天数
    """
    try:
        # 计算删除阈值时间
        cutoff_time = datetime.now().timestamp() - (days * 24 * 60 * 60)

        # 遍历备份目录中的文件
        for filename in os.listdir(backup_dir):
            if filename.startswith("pharmacy_backup_") and filename.endswith(".db"):
                file_path = os.path.join(backup_dir, filename)
                # 检查文件修改时间
                if os.path.getmtime(file_path) < cutoff_time:
                    os.remove(file_path)
                    print(f"已删除旧备份: {filename}")

    except Exception as e:
        print(f"清理旧备份时出错: {str(e)}")
