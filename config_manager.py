import os
import sys
from pathlib import Path


class ConfigManager:
    def __init__(self):
        super().__init__()

    def get_db_path(self):
        documents_path = Path("E:/PharmacyDrugManagement")
        documents_path.mkdir(exist_ok=True)
        db_path = str(documents_path / "pharmacy.db")
        return db_path

    def get_backup_dir(self):
        documents_path = Path("E:/Pharmacy_Backups")
        documents_path.mkdir(exist_ok=True)
        return str(documents_path)
