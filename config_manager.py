import os
import sys
from pathlib import Path


class ConfigManager:
    def __init__(self):
        super().__init__()

    def get_db_path(self):
        """获取数据库路径"""
        # db_path = self.config.get('Database', 'db_path')
        db_path = "data/pharmacy.db"
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
            # 对于 PyInstaller，数据文件通常在 _MEIPASS 目录下
            db_path = os.path.join(base_path, db_path)
        else:
            # 开发环境：使用当前文件所在目录
            base_path = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(base_path, 'data', 'pharmacy.db')
        return db_path

    def get_backup_dir(self):
        return os.path.join(str(Path.home()), "PharmacyDrugManagement_backups")
