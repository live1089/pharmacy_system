from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QDialog, QMessageBox

from page_window.tools import install_enter_key_filter
from ui_app.shelves_drug_ui import Ui_ShelvesDialog


class ShelvesDrugPage(QDialog, Ui_ShelvesDialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = parent
        self.bind_events()  # 修改为 bind_events
        self.shelves_id = None
        self.load_data()
        self.ignore_cargo_return()

    def ignore_cargo_return(self):
        install_enter_key_filter(self.stock_out_list_combox)
        install_enter_key_filter(self.stock_out_batch_combox)
        install_enter_key_filter(self.shelves_drug_combox)
        install_enter_key_filter(self.shelves_number_spinBox)
        install_enter_key_filter(self.shelves_location_combox)

    def check_if_drug_already_shelved(self, stock_out_batch, drug_id):
        """
        检查药品是否已经上架
        Args:
            stock_out_batch: 出库批次ID
            drug_id: 药品ID
        Returns:
            tuple: (是否已上架, 已上架数量)
        """
        query = QSqlQuery()
        query.prepare("""
            SELECT SUM(shelves_number) as total_shelved
            FROM shelves_drug 
            WHERE out_batch = ? AND drug = ?
        """)
        query.addBindValue(stock_out_batch)
        query.addBindValue(drug_id)

        if query.exec() and query.next():
            total_shelved = query.value(0)
            if total_shelved is not None and total_shelved != "":
                # 确保将结果转换为整数类型
                try:
                    shelved_count = int(total_shelved)
                    if shelved_count > 0:
                        return True, shelved_count
                except (ValueError, TypeError):
                    # 如果转换失败，返回默认值
                    return False, 0

        return False, 0

    def bind_events(self):  # 修改方法名
        self.shelves_add_save_btn.clicked.connect(self.save)
        # 添加上架药品出库单选择变化事件
        self.stock_out_list_combox.currentIndexChanged.connect(self.on_outbound_changed)
        # 添加出库批次选择变化事件
        self.stock_out_batch_combox.currentIndexChanged.connect(self.on_batch_changed)

    def on_outbound_changed(self, index):
        """当出库单选择变化时，更新批次列表"""
        if index >= 0:
            out_id = self.stock_out_list_combox.itemData(index)
            self.load_batches_by_outbound(out_id)

    def on_batch_changed(self, index):
        """当出库批次选择变化时，自动加载对应的药品信息和数量"""
        if index >= 0:
            detail_id = self.stock_out_batch_combox.itemData(index)
            self.load_drug_by_batch(detail_id)

    def load_batches_by_outbound(self, out_id):
        """根据出库单ID加载对应的出库批次"""
        # 清空当前批次列表
        self.stock_out_batch_combox.clear()
        # 清空药品和数量显示
        self.shelves_drug_combox.clear()
        self.shelves_number_spinBox.setValue(0)

        # 查询该出库单对应的批次
        query = QSqlQuery()
        query.prepare("""
               SELECT detail_id, out_batch 
               FROM stock_out_detail 
               WHERE out_id = ?
               ORDER BY out_batch
           """)
        query.addBindValue(out_id)

        if query.exec():
            while query.next():
                detail_id = query.value(0)
                out_batch = query.value(1)
                self.stock_out_batch_combox.addItem(out_batch, detail_id)
        else:
            print(f"查询批次失败: {query.lastError().text()}")

    def load_drug_by_batch(self, detail_id):
        self.shelves_drug_combox.clear()
        """根据出库批次ID加载对应的药品信息和数量"""
        if detail_id is not None:
            # 查询该批次对应的药品信息
            query = QSqlQuery()
            query.prepare("""
                   SELECT md.dic_id, md.trade_name, sod.quantity
                   FROM stock_out_detail sod
                   JOIN medicine_dic md ON sod.medicine_id = md.dic_id
                   WHERE sod.detail_id = ?
               """)
            query.addBindValue(detail_id)

            if query.exec() and query.next():
                medicine_id = query.value(0)
                medicine_name = query.value(1)
                quantity = query.value(2)

                # 设置药品下拉框
                # 先检查药品是否已存在
                index = self.shelves_drug_combox.findData(medicine_id)
                if index >= 0:
                    self.shelves_drug_combox.setCurrentIndex(index)
                else:
                    # 如果药品不在下拉框中，添加它
                    self.shelves_drug_combox.addItem(medicine_name, medicine_id)
                    self.shelves_drug_combox.setCurrentIndex(self.shelves_drug_combox.count() - 1)

                # 设置数量
                self.shelves_number_spinBox.setValue(quantity or 0)
            else:
                print(f"查询批次对应的药品信息失败: {query.lastError().text()}")
                # 清空数量显示
                self.shelves_number_spinBox.setValue(0)

    def load_data(self):
        """加载初始数据"""
        # 加载出库单列表（上架类型）
        query = QSqlQuery(
            "SELECT out_id, outbound_number FROM stock_out_main WHERE out_type = '上架' ORDER BY out_id DESC")
        while query.next():
            out_id = query.value(0)
            outbound_number = query.value(1)
            self.stock_out_list_combox.addItem(outbound_number, out_id)

        # 加载货位信息
        query = QSqlQuery("SELECT warehouse_shelf_id, location FROM warehouse_shelf_position")
        while query.next():
            shelf_id = query.value(0)
            shelf_name = query.value(1)
            self.shelves_location_combox.addItem(shelf_name, shelf_id)

    def save(self):
        if self.shelves_id:
            self.update_stock_shelves()
        else:
            self.create_stock_shelves()

    def create_stock_shelves(self):
        stock_out_list = self.stock_out_list_combox.itemData(self.stock_out_list_combox.currentIndex())
        stock_out_batch = self.stock_out_batch_combox.itemData(self.stock_out_batch_combox.currentIndex())
        shelves_drug = self.shelves_drug_combox.itemData(self.shelves_drug_combox.currentIndex())
        shelves_number = self.shelves_number_spinBox.value()
        shelves_location = self.shelves_location_combox.itemData(self.shelves_location_combox.currentIndex())

        # 检查药品是否已经上架
        if stock_out_batch is not None and shelves_drug is not None:
            already_shelved, shelved_quantity = self.check_if_drug_already_shelved(stock_out_batch, shelves_drug)
            if already_shelved:
                reply = QMessageBox.question(
                    self,
                    '提示',
                    f'该药品批次已经上架 {shelved_quantity} 件',
                    QMessageBox.StandardButton.Yes,
                    QMessageBox.StandardButton.Yes
                )
                if reply == QMessageBox.StandardButton.Yes:
                    return

        query = QSqlQuery()
        if not query.exec("BEGIN"):
            QMessageBox.critical(self, "数据库错误", f"无法开始事务: {query.lastError().text()}")
            return

        try:
            query.prepare(
                "Insert into shelves_drug(outbound_number, out_batch, drug, shelves_number, location_id) "
                "values (?,?,?,?,?)")
            query.addBindValue(stock_out_list)
            query.addBindValue(stock_out_batch)
            query.addBindValue(shelves_drug)
            query.addBindValue(shelves_number)
            query.addBindValue(shelves_location)
            if not query.exec():
                raise Exception(f"添加上架药品失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "添加成功")
            self.accept()  # 关闭对话框
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
        finally:
            query.finish()

    def update_load_data(self, shelves_id):
        self.shelves_id = shelves_id
        self.shelves_add_save_btn.setText("更新")
        query = QSqlQuery()
        query.prepare("SELECT outbound_number, out_batch, drug, shelves_number, location_id "
                      "FROM shelves_drug "
                      "WHERE shelves_id = ?")
        query.addBindValue(shelves_id)

        if query.exec() and query.next():
            outbound_number = query.value(0)
            out_batch = query.value(1)
            drug = query.value(2)
            shelves_number = query.value(3)
            location_id = query.value(4)

            self.stock_out_list_combox.setCurrentIndex(self.stock_out_list_combox.findData(outbound_number))
            self.stock_out_batch_combox.setCurrentIndex(self.stock_out_batch_combox.findData(out_batch))
            self.shelves_drug_combox.setCurrentIndex(self.shelves_drug_combox.findData(drug))
            self.shelves_number_spinBox.setValue(shelves_number)
            self.shelves_location_combox.setCurrentIndex(self.shelves_location_combox.findData(location_id))
        else:
            # 处理查询失败或无结果的情况
            print(f"查询失败或未找到数据: {query.lastError().text()}")

    def update_stock_shelves(self):
        stock_out_list = self.stock_out_list_combox.itemData(self.stock_out_list_combox.currentIndex())
        stock_out_batch = self.stock_out_batch_combox.itemData(self.stock_out_batch_combox.currentIndex())
        shelves_drug = self.shelves_drug_combox.itemData(self.shelves_drug_combox.currentIndex())
        shelves_number = self.shelves_number_spinBox.value()
        shelves_location = self.shelves_location_combox.itemData(self.shelves_location_combox.currentIndex())

        # 开始事务以确保数据一致性
        query = QSqlQuery()
        try:
            if not query.exec("BEGIN"):
                raise Exception(f"无法开始事务: {query.lastError().text()}")

            # 更新主表
            query.prepare("""
                UPDATE shelves_drug
                SET outbound_number=?, out_batch=?, drug=?, shelves_number=?, location_id=?
                WHERE shelves_id = ?
            """)
            query.addBindValue(stock_out_list)
            query.addBindValue(stock_out_batch)
            query.addBindValue(shelves_drug)
            query.addBindValue(shelves_number)
            query.addBindValue(shelves_location)
            query.addBindValue(self.shelves_id)

            if not query.exec():
                raise Exception(f"更新失败: {query.lastError().text()}")

            # 提交事务
            if not query.exec("COMMIT"):
                raise Exception(f"无法提交事务: {query.lastError().text()}")

            QMessageBox.information(self, "成功", "更新成功")
            self.accept()  # 关闭对话框
        except Exception as e:
            # 回滚事务
            query.exec("ROLLBACK")
            QMessageBox.critical(self, "数据库错误", str(e))
        finally:
            # 显式清理资源
            query.finish()
