from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QMessageBox, QDialog

import data.sqlite_data
from data.sqlite_data import DrugDicModel, SupplierModel, PurchaseOrderModel, \
    StockInMainModel, StockInDetailModel, StockOutMainModel, InventoryCheckModel, \
    ShelvesDrugModel, InventoryModel, SalesListsModel, SalesModel
from page_window.inventory_count_page import InventoryCountPage
from page_window.medicines_page import MedicinesPage, delete_selected_rows, DrugRormulationPage, \
    DrugUnitPage, DrugAttributePage, DrugSpecificationPage
from page_window.purchase_page import PurAddPage, AnOrderPage
from page_window.sell_medicines_page import SellDrugUiDialog, SellListDialog
from page_window.shelves_drug_page import ShelvesDrugPage
from page_window.stock_medicines_page import StockMedicinesPage, StockLocationPage, StockInAllPage
from page_window.stock_out_page import StockOutPage, StockOutAddDrugPage
from page_window.supplier_medicines_page import SupplierDrugPage, get_selected_logical_rows

start_times = QDateTime.currentDateTime().addDays(-30).date().toString("yyyy-MM-dd")
end_times = QDateTime.currentDateTime().addDays(+1).date().toString("yyyy-MM-dd")


def stock_in_all(self):
    self.stock_all = StockInAllPage(self)
    self.stock_all.exec()


def add_stock_location(self):
    self.stock_location = StockLocationPage(self)
    self.stock_location.exec()


def del_dic(self):
    self.dic = DrugDicModel(self, self.db)
    success, msg = delete_selected_rows(
        self=self,
        tableView=self.drug_dic_tableView,
        model=self.dic,
        db=self.db,
    )
    if success:
        QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
        data.sqlite_data.get_medicine_dic_model(self)
        self.drug_dic_tableView.clearSelection()
    else:
        QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)


def del_sell(self):
    current_tab_index = self.tabWidget.currentIndex()
    if current_tab_index == 0:
        self.sell_li = SalesListsModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.sales_lists_tableView,
            model=self.sell_li,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_sales_lists_model(self, start_times, end_times)
            self.sales_lists_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)
    elif current_tab_index == 1:
        self.sell_sa = SalesModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.sales_records_tableView,
            model=self.sell_sa,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_sales_model(self, start_times, end_times)
            self.sales_records_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)


def supplier_mod(self):
    selected_rows = get_selected_logical_rows(self.supplier_tableView)
    if not selected_rows:
        QMessageBox.warning(self, "警告", "请先选择要修改的供应商记录")
        return

    # 获取选中行的supplier_id
    model = self.supplier_tableView.model()
    if model and len(selected_rows) > 0:
        # 假设supplier_id在第一列（索引为0）
        supplier_id = model.data(model.index(selected_rows[0], 0))

        self.sup = SupplierDrugPage(self)
        self.sup.show_mod_supplier_data(supplier_id)  # 先填充数据
        if self.sup.exec() == QDialog.DialogCode.Accepted:  # 如果成功保存
            data.sqlite_data.get_supplier_model(self)  # 刷新供应商列表


def drug_revise(self):
    selected_rows = get_selected_logical_rows(self.drug_dic_tableView)
    if not selected_rows:
        QMessageBox.warning(self, "警告", "请先选择要修改的药品记录")
        return
    model = self.drug_dic_tableView.model()
    if model and len(selected_rows) > 0:
        # 假设drug_id在第一列（索引为0）
        drug_id = model.data(model.index(selected_rows[0], 0))
        self.drug = MedicinesPage(self)
        self.drug.load_update_drug_data(drug_id)
        if self.drug.exec() == QDialog.DialogCode.Accepted:  # 如果成功保存
            data.sqlite_data.get_medicine_dic_model(self)


def supplier_del(self):
    self.supp = SupplierModel(self, self.db)
    success, msg = delete_selected_rows(
        self=self,
        tableView=self.supplier_tableView,
        model=self.supp,
        db=self.db,
    )
    if success:
        QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
        data.sqlite_data.get_supplier_model(self)
        self.supplier_tableView.clearSelection()
    else:
        QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)


def purchase_del(self):
    # 获取当前采购标签页的索引
    current_order_tab_index = self.order_tabWidget.currentIndex()
    if current_order_tab_index == 0:  # 采购订单表
        self.pur = PurchaseOrderModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.purchase_order_tableView,
            model=self.pur,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_purchase_order_model(self, start_times, end_times)
            self.purchase_order_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    elif current_order_tab_index == 1:  # 采购明细表
        from data.sqlite_data import PurchaseDetailModel
        self.pur_detail = PurchaseDetailModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.purchase_detail_tableView,
            model=self.pur_detail,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_purchase_order_detail_model(self, start_times, end_times)
            self.purchase_detail_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)


def stock_del(self):
    # 获取当前采购标签页的索引
    current_order_tab_index = self.stock_in_tabWidget.currentIndex()
    if current_order_tab_index == 0:
        self.stock = StockInMainModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.main_tableView,
            model=self.stock,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_stock_in_main_model(self, start_times, end_times)
            self.main_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    if current_order_tab_index == 1:
        self.stock = StockInDetailModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.detail_tableView,
            model=self.stock,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_stock_in_detail_model(self, start_times, end_times)
            self.detail_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)


def stock_out_del(self):
    # 获取当前出库标签页的索引
    current_tab_index = self.stock_out_tabWidget.currentIndex()

    if current_tab_index == 0:  # 出库主表
        self.stock = StockOutMainModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.stock_out_main_tableView,
            model=self.stock,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_stock_out_main_model(self, start_times, end_times)
            self.stock_out_main_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)

    elif current_tab_index == 1:  # 出库明细表
        from data.sqlite_data import StockOutDetailModel
        self.stock_detail = StockOutDetailModel(self, self.db)
        success, msg = delete_selected_rows(
            self=self,
            tableView=self.stock_out_detail_tableView,
            model=self.stock_detail,
            db=self.db,
        )
        if success:
            QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
            data.sqlite_data.get_stock_out_detail_model(self, start_times, end_times)
            self.stock_out_detail_tableView.clearSelection()
        else:
            QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)


def inventory_check_del(self):
    self.inventory_check_model = InventoryCheckModel(self, self.db)
    success, msg = delete_selected_rows(
        self=self,
        tableView=self.inventory_check_tableView,
        model=self.inventory_check_model,
        db=self.db,
    )
    if success:
        QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
        data.sqlite_data.get_inventory_check(self, start_times, end_times)
        self.inventory_check_tableView.clearSelection()
    else:
        QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)


def shelves_del(self):
    self.shelves = ShelvesDrugModel(self, self.db)
    success, msg = delete_selected_rows(
        self=self,
        tableView=self.drugs_on_shelves_tableView,
        model=self.shelves,
        db=self.db,
    )
    if success:
        QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
        data.sqlite_data.get_shelves_drug_model(self)
    else:
        QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)


def inventory_del(self):
    self.inventory = InventoryModel(self, self.db)
    success, msg = delete_selected_rows(
        self=self,
        tableView=self.inventory_tableView,
        model=self.inventory,
        db=self.db,
    )
    if success:
        QMessageBox.information(self, "成功", msg, QMessageBox.StandardButton.Ok)
        data.sqlite_data.get_inventory_model(self, start_times, end_times)
    else:
        QMessageBox.warning(self, "失败", msg, QMessageBox.StandardButton.Ok)


def stock_mod(self):
    selected_rows = get_selected_logical_rows(self.main_tableView)
    if not selected_rows:
        QMessageBox.warning(self, "警告", "请先选择要修改的记录")
        return

    model = self.main_tableView.model()
    if model and len(selected_rows) > 0:
        stock_in_id = model.data(model.index(selected_rows[0], 0))

        self.sup = StockMedicinesPage(self)
        self.sup.load_order_data(stock_in_id)  # 先填充数据
        if self.sup.exec() == QDialog.DialogCode.Accepted:  # 如果成功保存
            data.sqlite_data.get_stock_in_main_model(self, start_times, end_times)
            data.sqlite_data.get_stock_in_detail_model(self, start_times, end_times)


def shelves_mod(self):
    selected_rows = get_selected_logical_rows(self.drugs_on_shelves_tableView)
    if not selected_rows:
        QMessageBox.warning(self, "警告", "请先选择要修改的记录")
        return
    model = self.drugs_on_shelves_tableView.model()
    if model and len(selected_rows) > 0:
        shelves_id = model.data(model.index(selected_rows[0], 0))
        self.shelves = ShelvesDrugPage(self)
        self.shelves.update_load_data(shelves_id)
        self.shelves.exec()
        data.sqlite_data.get_shelves_drug_model(self)


def purchase_modify(self):
    """修改采购订单"""
    current_order_tab_index = self.order_tabWidget.currentIndex()

    if current_order_tab_index == 0:  # 采购订单表
        selected_rows = get_selected_logical_rows(self.purchase_order_tableView)
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请先选择要修改的采购订单记录")
            return

        # 获取选中行的order_id
        model = self.purchase_order_tableView.model()
        if model and len(selected_rows) > 0:
            order_id = model.data(model.index(selected_rows[0], 0))  # 假设ID在第一列

            self.pu = AnOrderPage(self)
            self.pu.load_order(order_id)  # 加载订单数据
            self.pu.exec()

            # 更新数据
            data.sqlite_data.get_purchase_order_model(self, start_times, end_times)
            data.sqlite_data.get_purchase_order_detail_model(self, start_times, end_times)

    if current_order_tab_index == 1:  # 采购订单明细表
        selected_rows = get_selected_logical_rows(self.purchase_detail_tableView)
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请先选择要修改的药品订单记录")
            return
        model = self.purchase_detail_tableView.model()
        if model and len(selected_rows) > 0:
            detail_id = model.data(model.index(selected_rows[0], 0))
            self.pu = PurAddPage(self)
            self.pu.load_order_data(detail_id)
            self.pu.exec()
            data.sqlite_data.get_purchase_order_model(self, start_times, end_times)
            data.sqlite_data.get_purchase_order_detail_model(self, start_times, end_times)


def stock_out_mod(self):
    current_tab_index = self.stock_out_tabWidget.currentIndex()
    if current_tab_index == 0:
        selected_rows = get_selected_logical_rows(self.stock_out_main_tableView)
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请先选择要修改的出库订单记录")
            return
        model = self.stock_out_main_tableView.model()
        if model and len(selected_rows) > 0:
            out_id = model.data(model.index(selected_rows[0], 0))
            self.so = StockOutPage(self)
            self.so.load_stock_out_data(out_id)
            self.so.exec()
            data.sqlite_data.get_stock_out_main_model(self, start_times, end_times)
            data.sqlite_data.get_stock_out_detail_model(self, start_times, end_times)
    if current_tab_index == 1:
        selected_rows = get_selected_logical_rows(self.stock_out_detail_tableView)
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请先选择要修改的记录")
            return
        model = self.stock_out_detail_tableView.model()
        if model and len(selected_rows) > 0:
            detail_id = model.data(model.index(selected_rows[0], 0))
            print(detail_id)
            self.so = StockOutAddDrugPage(self)
            self.so.load_stock_out_update_data(detail_id)
            self.so.exec()
            data.sqlite_data.get_stock_out_main_model(self, start_times, end_times)
            data.sqlite_data.get_stock_out_detail_model(self, start_times, end_times)


def inventory_check_mod(self):
    selected_rows = get_selected_logical_rows(self.inventory_check_tableView)
    if not selected_rows:
        QMessageBox.warning(self, "警告", "请先选择要修改的盘点记录")
        return
    model = self.inventory_check_tableView.model()
    if model and len(selected_rows) > 0:
        check_id = model.data(model.index(selected_rows[0], 0))
        self.ic = InventoryCountPage(self)
        self.ic.load_check_out_data(check_id)
        self.ic.exec()
        data.sqlite_data.get_inventory_check(self, start_times, end_times)


# -------------------------------------------------------------------------------------------------------------------------------
# 添加跳出子窗口事件
def sub_window_event(self):
    self.drug_add_btn.clicked.connect(lambda: drug_adds(self))
    self.drugs_set_btn.clicked.connect(lambda: drug_attribute(self))
    self.dosage_set_btn.clicked.connect(lambda: drug_rormulation(self))
    self.unit_set_btn.clicked.connect(lambda: drug_unit(self))
    self.specifications_set_btn.clicked.connect(lambda: drug_specification(self))
    self.sell_drug_btn.clicked.connect(lambda: sell_drug_func(self))
    self.add_sell_list_btn.clicked.connect(lambda: sell_list_func(self))
    self.supplier_add_btn.clicked.connect(lambda: supplier_add(self))
    self.stock_in_btn.clicked.connect(lambda: stock_in(self))
    self.purchase_add_btn.clicked.connect(lambda: purchase_add(self))
    self.add_an_order_btn.clicked.connect(lambda: add_an_order(self))
    self.stock_out_add_btn.clicked.connect(lambda: stock_out(self))
    self.stock_out_add_drug_btn.clicked.connect(lambda: stock_out_add_drug(self))
    self.inventory_check_add_btn.clicked.connect(lambda: inventory_check_add(self))
    self.shelves_add_btn.clicked.connect(lambda: shelves_add(self))



def shelves_add(self):
    self.shelves = ShelvesDrugPage(self)
    self.shelves.exec()
    data.sqlite_data.get_shelves_drug_model(self)


# 药品添加
def drug_adds(self):
    self.drug_add = MedicinesPage(self)
    self.drug_add.exec()


def drug_attribute(self):
    self.drug_att = DrugAttributePage(self)
    self.drug_att.exec()
    # self.drug_att.show()


def drug_rormulation(self):
    self.drug_ror = DrugRormulationPage(self)
    self.drug_ror.exec()


def drug_unit(self):
    self.drug_un = DrugUnitPage(self)
    self.drug_un.exec()


def drug_specification(self):
    self.drug_sp = DrugSpecificationPage(self)
    self.drug_sp.exec()


def sell_drug_func(self):
    self.sell_d = SellDrugUiDialog(self)
    self.sell_d.exec()
    data.sqlite_data.get_sales_model(self, start_times, end_times)


def sell_list_func(self):
    self.sell_list = SellListDialog(self)
    self.sell_list.exec()
    data.sqlite_data.get_sales_lists_model(self, start_times, end_times)


def supplier_add(self):
    self.sup = SupplierDrugPage(self)
    self.sup.load_supplier_time()
    self.sup.exec()
    data.sqlite_data.get_supplier_model(self)


def stock_in(self):
    self.stock_inbo = StockMedicinesPage(self)
    self.stock_inbo.exec()
    data.sqlite_data.get_stock_in_main_model(self, start_times, end_times)
    data.sqlite_data.get_stock_in_detail_model(self, start_times, end_times)


def purchase_add(self):
    self.pu = PurAddPage(self)
    self.pu.exec()
    data.sqlite_data.get_purchase_order_detail_model(self, start_times, end_times)


def add_an_order(self):
    self.puan = AnOrderPage(self)
    self.puan.exec()
    data.sqlite_data.get_purchase_order_model(self, start_times, end_times)


def stock_out(self):
    self.stock_out_page = StockOutPage(self)
    self.stock_out_page.exec()
    data.sqlite_data.get_stock_out_main_model(self, start_times, end_times)
    data.sqlite_data.get_stock_out_detail_model(self, start_times, end_times)


def stock_out_add_drug(self):
    self.stock_out_add_dr = StockOutAddDrugPage(self)
    self.stock_out_add_dr.exec()
    data.sqlite_data.get_stock_out_main_model(self, start_times, end_times)
    data.sqlite_data.get_stock_out_detail_model(self, start_times, end_times)


def inventory_check_add(self):
    self.inventory_check_add_page = InventoryCountPage(self)
    self.inventory_check_add_page.exec()
    data.sqlite_data.get_inventory_check(self, start_times, end_times)