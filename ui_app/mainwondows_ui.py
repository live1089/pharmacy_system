# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwondows.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1116, 597)
        icon = QIcon()
        icon.addFile(u"../../python_code/Res.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        self.actionout = QAction(mainWindow)
        self.actionout.setObjectName(u"actionout")
        self.actionfg = QAction(mainWindow)
        self.actionfg.setObjectName(u"actionfg")
        self.actionh = QAction(mainWindow)
        self.actionh.setObjectName(u"actionh")
        self.actiond = QAction(mainWindow)
        self.actiond.setObjectName(u"actiond")
        self.actionlight = QAction(mainWindow)
        self.actionlight.setObjectName(u"actionlight")
        self.actions = QAction(mainWindow)
        self.actions.setObjectName(u"actions")
        self.actions_2 = QAction(mainWindow)
        self.actions_2.setObjectName(u"actions_2")
        self.actiong = QAction(mainWindow)
        self.actiong.setObjectName(u"actiong")
        self.actionm = QAction(mainWindow)
        self.actionm.setObjectName(u"actionm")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.medicine = QPushButton(self.centralwidget)
        self.medicine.setObjectName(u"medicine")

        self.verticalLayout.addWidget(self.medicine)

        self.sales_records = QPushButton(self.centralwidget)
        self.sales_records.setObjectName(u"sales_records")

        self.verticalLayout.addWidget(self.sales_records)

        self.expiring_medicine = QPushButton(self.centralwidget)
        self.expiring_medicine.setObjectName(u"expiring_medicine")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expiring_medicine.sizePolicy().hasHeightForWidth())
        self.expiring_medicine.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.expiring_medicine)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.supplier = QPushButton(self.centralwidget)
        self.supplier.setObjectName(u"supplier")

        self.verticalLayout.addWidget(self.supplier)

        self.medicine_purchase = QPushButton(self.centralwidget)
        self.medicine_purchase.setObjectName(u"medicine_purchase")

        self.verticalLayout.addWidget(self.medicine_purchase)

        self.drug_inbound = QPushButton(self.centralwidget)
        self.drug_inbound.setObjectName(u"drug_inbound")

        self.verticalLayout.addWidget(self.drug_inbound)

        self.drug_outbound = QPushButton(self.centralwidget)
        self.drug_outbound.setObjectName(u"drug_outbound")
        self.drug_outbound.setEnabled(True)
        sizePolicy.setHeightForWidth(self.drug_outbound.sizePolicy().hasHeightForWidth())
        self.drug_outbound.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.drug_outbound)

        self.drugs_on_shelves = QPushButton(self.centralwidget)
        self.drugs_on_shelves.setObjectName(u"drugs_on_shelves")

        self.verticalLayout.addWidget(self.drugs_on_shelves)

        self.stock_in_all_btn = QPushButton(self.centralwidget)
        self.stock_in_all_btn.setObjectName(u"stock_in_all_btn")

        self.verticalLayout.addWidget(self.stock_in_all_btn)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.inventory_record = QPushButton(self.centralwidget)
        self.inventory_record.setObjectName(u"inventory_record")

        self.verticalLayout.addWidget(self.inventory_record)

        self.pharmacy_operation_record = QPushButton(self.centralwidget)
        self.pharmacy_operation_record.setObjectName(u"pharmacy_operation_record")

        self.verticalLayout.addWidget(self.pharmacy_operation_record)

        self.clear_btn = QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(u"clear_btn")

        self.verticalLayout.addWidget(self.clear_btn)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.line_30 = QFrame(self.page)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.Shape.VLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_30)

        self.search_le = QLineEdit(self.page)
        self.search_le.setObjectName(u"search_le")

        self.horizontalLayout_6.addWidget(self.search_le)

        self.drug_selection_query_btn = QPushButton(self.page)
        self.drug_selection_query_btn.setObjectName(u"drug_selection_query_btn")

        self.horizontalLayout_6.addWidget(self.drug_selection_query_btn)

        self.drug_ref_btn = QPushButton(self.page)
        self.drug_ref_btn.setObjectName(u"drug_ref_btn")
        sizePolicy.setHeightForWidth(self.drug_ref_btn.sizePolicy().hasHeightForWidth())
        self.drug_ref_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.drug_ref_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.shelves_drug_tableView = QTableView(self.page)
        self.shelves_drug_tableView.setObjectName(u"shelves_drug_tableView")

        self.verticalLayout_2.addWidget(self.shelves_drug_tableView)

        self.stackedWidget.addWidget(self.page)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_10 = QGridLayout(self.page_1)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.supplier_tableView = QTableView(self.page_1)
        self.supplier_tableView.setObjectName(u"supplier_tableView")

        self.gridLayout_9.addWidget(self.supplier_tableView, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.supplier_add_btn = QPushButton(self.page_1)
        self.supplier_add_btn.setObjectName(u"supplier_add_btn")

        self.horizontalLayout.addWidget(self.supplier_add_btn)

        self.supplier_mod_btn = QPushButton(self.page_1)
        self.supplier_mod_btn.setObjectName(u"supplier_mod_btn")

        self.horizontalLayout.addWidget(self.supplier_mod_btn)

        self.supplier_del_btn = QPushButton(self.page_1)
        self.supplier_del_btn.setObjectName(u"supplier_del_btn")

        self.horizontalLayout.addWidget(self.supplier_del_btn)


        self.gridLayout_9.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.line_29 = QFrame(self.page_1)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.Shape.VLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_29)

        self.supplier_lineEdit = QLineEdit(self.page_1)
        self.supplier_lineEdit.setObjectName(u"supplier_lineEdit")

        self.horizontalLayout_10.addWidget(self.supplier_lineEdit)

        self.supplier_query_btn = QPushButton(self.page_1)
        self.supplier_query_btn.setObjectName(u"supplier_query_btn")

        self.horizontalLayout_10.addWidget(self.supplier_query_btn)


        self.gridLayout_10.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_12 = QGridLayout(self.page_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.stock_in_tabWidget = QTabWidget(self.page_2)
        self.stock_in_tabWidget.setObjectName(u"stock_in_tabWidget")
        self.stock_in_tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.stock_in_tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.stock_in_tabWidget.setTabsClosable(False)
        self.stock_in_main = QWidget()
        self.stock_in_main.setObjectName(u"stock_in_main")
        self.gridLayout_16 = QGridLayout(self.stock_in_main)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.main_tableView = QTableView(self.stock_in_main)
        self.main_tableView.setObjectName(u"main_tableView")

        self.gridLayout_15.addWidget(self.main_tableView, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 2, 0, 1, 1)

        self.stock_in_tabWidget.addTab(self.stock_in_main, "")
        self.stock_in_detail = QWidget()
        self.stock_in_detail.setObjectName(u"stock_in_detail")
        self.gridLayout_18 = QGridLayout(self.stock_in_detail)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.detail_tableView = QTableView(self.stock_in_detail)
        self.detail_tableView.setObjectName(u"detail_tableView")

        self.gridLayout_17.addWidget(self.detail_tableView, 0, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_17, 0, 0, 1, 1)

        self.stock_in_tabWidget.addTab(self.stock_in_detail, "")

        self.gridLayout_11.addWidget(self.stock_in_tabWidget, 0, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_11, 1, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.line_24 = QFrame(self.page_2)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.VLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_24)

        self.label_18 = QLabel(self.page_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)

        self.storage_dateEdit_start = QDateEdit(self.page_2)
        self.storage_dateEdit_start.setObjectName(u"storage_dateEdit_start")

        self.horizontalLayout_11.addWidget(self.storage_dateEdit_start)

        self.line_25 = QFrame(self.page_2)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_25)

        self.label_19 = QLabel(self.page_2)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_11.addWidget(self.label_19)

        self.storage_dateEdit_deadline_end = QDateEdit(self.page_2)
        self.storage_dateEdit_deadline_end.setObjectName(u"storage_dateEdit_deadline_end")

        self.horizontalLayout_11.addWidget(self.storage_dateEdit_deadline_end)

        self.storage_btn = QPushButton(self.page_2)
        self.storage_btn.setObjectName(u"storage_btn")

        self.horizontalLayout_11.addWidget(self.storage_btn)

        self.line_26 = QFrame(self.page_2)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.Shape.VLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_26)

        self.stock_in_lineEdit = QLineEdit(self.page_2)
        self.stock_in_lineEdit.setObjectName(u"stock_in_lineEdit")

        self.horizontalLayout_11.addWidget(self.stock_in_lineEdit)

        self.stock_in_query_btn = QPushButton(self.page_2)
        self.stock_in_query_btn.setObjectName(u"stock_in_query_btn")

        self.horizontalLayout_11.addWidget(self.stock_in_query_btn)

        self.line_27 = QFrame(self.page_2)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.Shape.VLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_27)

        self.add_stock_location_btn = QPushButton(self.page_2)
        self.add_stock_location_btn.setObjectName(u"add_stock_location_btn")

        self.horizontalLayout_11.addWidget(self.add_stock_location_btn)

        self.stock_in_btn = QPushButton(self.page_2)
        self.stock_in_btn.setObjectName(u"stock_in_btn")

        self.horizontalLayout_11.addWidget(self.stock_in_btn)

        self.line_28 = QFrame(self.page_2)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.Shape.VLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_28)

        self.stock_del_btn = QPushButton(self.page_2)
        self.stock_del_btn.setObjectName(u"stock_del_btn")

        self.horizontalLayout_11.addWidget(self.stock_del_btn)

        self.stock_mod_btn = QPushButton(self.page_2)
        self.stock_mod_btn.setObjectName(u"stock_mod_btn")

        self.horizontalLayout_11.addWidget(self.stock_mod_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)


        self.gridLayout_12.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_14 = QGridLayout(self.page_3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.inventory_tableView = QTableView(self.page_3)
        self.inventory_tableView.setObjectName(u"inventory_tableView")

        self.gridLayout_13.addWidget(self.inventory_tableView, 0, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_13, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.line_22 = QFrame(self.page_3)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_22)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.inventory_dateEdit_start = QDateEdit(self.page_3)
        self.inventory_dateEdit_start.setObjectName(u"inventory_dateEdit_start")

        self.horizontalLayout_9.addWidget(self.inventory_dateEdit_start)

        self.line_4 = QFrame(self.page_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_4)

        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.inventory_dateEdit_deadline = QDateEdit(self.page_3)
        self.inventory_dateEdit_deadline.setObjectName(u"inventory_dateEdit_deadline")

        self.horizontalLayout_9.addWidget(self.inventory_dateEdit_deadline)

        self.inventory_btn = QPushButton(self.page_3)
        self.inventory_btn.setObjectName(u"inventory_btn")

        self.horizontalLayout_9.addWidget(self.inventory_btn)

        self.line_23 = QFrame(self.page_3)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.Shape.VLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_23)

        self.inventory_del_btn = QPushButton(self.page_3)
        self.inventory_del_btn.setObjectName(u"inventory_del_btn")

        self.horizontalLayout_9.addWidget(self.inventory_del_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.gridLayout_14.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_6 = QGridLayout(self.page_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget = QTabWidget(self.page_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_38 = QGridLayout(self.tab_2)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.sales_lists_tableView = QTableView(self.tab_2)
        self.sales_lists_tableView.setObjectName(u"sales_lists_tableView")

        self.gridLayout_37.addWidget(self.sales_lists_tableView, 0, 0, 1, 1)


        self.gridLayout_38.addLayout(self.gridLayout_37, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_20 = QGridLayout(self.tab_3)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.sales_records_tableView = QTableView(self.tab_3)
        self.sales_records_tableView.setObjectName(u"sales_records_tableView")

        self.gridLayout_19.addWidget(self.sales_records_tableView, 0, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_19, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.line_19 = QFrame(self.page_4)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_19)

        self.label = QLabel(self.page_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.sales_records_dateEdit_start = QDateEdit(self.page_4)
        self.sales_records_dateEdit_start.setObjectName(u"sales_records_dateEdit_start")

        self.horizontalLayout_7.addWidget(self.sales_records_dateEdit_start)

        self.line = QFrame(self.page_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line)

        self.label_2 = QLabel(self.page_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.sales_records_dateEdit_deadline = QDateEdit(self.page_4)
        self.sales_records_dateEdit_deadline.setObjectName(u"sales_records_dateEdit_deadline")

        self.horizontalLayout_7.addWidget(self.sales_records_dateEdit_deadline)

        self.sales_records_btn = QPushButton(self.page_4)
        self.sales_records_btn.setObjectName(u"sales_records_btn")

        self.horizontalLayout_7.addWidget(self.sales_records_btn)

        self.line_21 = QFrame(self.page_4)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.VLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_21)

        self.sales_records_lineEdit = QLineEdit(self.page_4)
        self.sales_records_lineEdit.setObjectName(u"sales_records_lineEdit")

        self.horizontalLayout_7.addWidget(self.sales_records_lineEdit)

        self.sales_rec_btn = QPushButton(self.page_4)
        self.sales_rec_btn.setObjectName(u"sales_rec_btn")

        self.horizontalLayout_7.addWidget(self.sales_rec_btn)

        self.line_38 = QFrame(self.page_4)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.Shape.VLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_38)

        self.add_sell_list_btn = QPushButton(self.page_4)
        self.add_sell_list_btn.setObjectName(u"add_sell_list_btn")

        self.horizontalLayout_7.addWidget(self.add_sell_list_btn)

        self.sell_drug_btn = QPushButton(self.page_4)
        self.sell_drug_btn.setObjectName(u"sell_drug_btn")

        self.horizontalLayout_7.addWidget(self.sell_drug_btn)

        self.line_20 = QFrame(self.page_4)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_20)

        self.sell_del_btn = QPushButton(self.page_4)
        self.sell_del_btn.setObjectName(u"sell_del_btn")

        self.horizontalLayout_7.addWidget(self.sell_del_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.gridLayout_6.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_8 = QGridLayout(self.page_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.expiring_drugs_tableView = QTableView(self.page_5)
        self.expiring_drugs_tableView.setObjectName(u"expiring_drugs_tableView")

        self.gridLayout_7.addWidget(self.expiring_drugs_tableView, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.line_18 = QFrame(self.page_5)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_18)

        self.label_3 = QLabel(self.page_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.expiring_drugs_lineEdit_day = QLineEdit(self.page_5)
        self.expiring_drugs_lineEdit_day.setObjectName(u"expiring_drugs_lineEdit_day")
        sizePolicy.setHeightForWidth(self.expiring_drugs_lineEdit_day.sizePolicy().hasHeightForWidth())
        self.expiring_drugs_lineEdit_day.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.expiring_drugs_lineEdit_day)

        self.expiring_drugs_save_btn = QPushButton(self.page_5)
        self.expiring_drugs_save_btn.setObjectName(u"expiring_drugs_save_btn")

        self.horizontalLayout_8.addWidget(self.expiring_drugs_save_btn)

        self.line_17 = QFrame(self.page_5)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_17)

        self.ex_ref_btn = QPushButton(self.page_5)
        self.ex_ref_btn.setObjectName(u"ex_ref_btn")

        self.horizontalLayout_8.addWidget(self.ex_ref_btn)


        self.gridLayout_8.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_24 = QGridLayout(self.page_6)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.stock_out_tabWidget = QTabWidget(self.page_6)
        self.stock_out_tabWidget.setObjectName(u"stock_out_tabWidget")
        self.stock_out_main = QWidget()
        self.stock_out_main.setObjectName(u"stock_out_main")
        self.gridLayout_26 = QGridLayout(self.stock_out_main)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.stock_out_main_tableView = QTableView(self.stock_out_main)
        self.stock_out_main_tableView.setObjectName(u"stock_out_main_tableView")

        self.gridLayout_25.addWidget(self.stock_out_main_tableView, 0, 0, 1, 1)


        self.gridLayout_26.addLayout(self.gridLayout_25, 0, 0, 1, 1)

        self.stock_out_tabWidget.addTab(self.stock_out_main, "")
        self.stock_out_detail = QWidget()
        self.stock_out_detail.setObjectName(u"stock_out_detail")
        self.gridLayout_28 = QGridLayout(self.stock_out_detail)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.stock_out_detail_tableView = QTableView(self.stock_out_detail)
        self.stock_out_detail_tableView.setObjectName(u"stock_out_detail_tableView")

        self.gridLayout_27.addWidget(self.stock_out_detail_tableView, 0, 0, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_27, 0, 0, 1, 1)

        self.stock_out_tabWidget.addTab(self.stock_out_detail, "")

        self.gridLayout_22.addWidget(self.stock_out_tabWidget, 0, 0, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_22, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_8 = QFrame(self.page_6)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_8)

        self.label_6 = QLabel(self.page_6)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.stock_out_dateEdit_start = QDateEdit(self.page_6)
        self.stock_out_dateEdit_start.setObjectName(u"stock_out_dateEdit_start")

        self.horizontalLayout_2.addWidget(self.stock_out_dateEdit_start)

        self.line_5 = QFrame(self.page_6)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_5)

        self.label_7 = QLabel(self.page_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.stock_out_dateEdit_deadline = QDateEdit(self.page_6)
        self.stock_out_dateEdit_deadline.setObjectName(u"stock_out_dateEdit_deadline")

        self.horizontalLayout_2.addWidget(self.stock_out_dateEdit_deadline)

        self.line_6 = QFrame(self.page_6)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_6)

        self.stock_out_query_btn = QPushButton(self.page_6)
        self.stock_out_query_btn.setObjectName(u"stock_out_query_btn")

        self.horizontalLayout_2.addWidget(self.stock_out_query_btn)

        self.line_10 = QFrame(self.page_6)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_10)

        self.stock_out_number_lineEdit = QLineEdit(self.page_6)
        self.stock_out_number_lineEdit.setObjectName(u"stock_out_number_lineEdit")

        self.horizontalLayout_2.addWidget(self.stock_out_number_lineEdit)

        self.stock_out_list_select_btn = QPushButton(self.page_6)
        self.stock_out_list_select_btn.setObjectName(u"stock_out_list_select_btn")

        self.horizontalLayout_2.addWidget(self.stock_out_list_select_btn)

        self.line_36 = QFrame(self.page_6)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.Shape.VLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_36)

        self.stock_out_add_btn = QPushButton(self.page_6)
        self.stock_out_add_btn.setObjectName(u"stock_out_add_btn")

        self.horizontalLayout_2.addWidget(self.stock_out_add_btn)

        self.stock_out_add_drug_btn = QPushButton(self.page_6)
        self.stock_out_add_drug_btn.setObjectName(u"stock_out_add_drug_btn")

        self.horizontalLayout_2.addWidget(self.stock_out_add_drug_btn)

        self.line_9 = QFrame(self.page_6)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_9)

        self.stock_out_del_btn = QPushButton(self.page_6)
        self.stock_out_del_btn.setObjectName(u"stock_out_del_btn")

        self.horizontalLayout_2.addWidget(self.stock_out_del_btn)

        self.stock_out_mod_btn = QPushButton(self.page_6)
        self.stock_out_mod_btn.setObjectName(u"stock_out_mod_btn")

        self.horizontalLayout_2.addWidget(self.stock_out_mod_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.gridLayout_24.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_30 = QGridLayout(self.page_7)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.order_tabWidget = QTabWidget(self.page_7)
        self.order_tabWidget.setObjectName(u"order_tabWidget")
        self.purchase_order = QWidget()
        self.purchase_order.setObjectName(u"purchase_order")
        self.gridLayout_32 = QGridLayout(self.purchase_order)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.purchase_order_tableView = QTableView(self.purchase_order)
        self.purchase_order_tableView.setObjectName(u"purchase_order_tableView")

        self.gridLayout_31.addWidget(self.purchase_order_tableView, 0, 0, 1, 1)


        self.gridLayout_32.addLayout(self.gridLayout_31, 0, 0, 1, 1)

        self.order_tabWidget.addTab(self.purchase_order, "")
        self.purchase_detail = QWidget()
        self.purchase_detail.setObjectName(u"purchase_detail")
        self.gridLayout_34 = QGridLayout(self.purchase_detail)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.purchase_detail_tableView = QTableView(self.purchase_detail)
        self.purchase_detail_tableView.setObjectName(u"purchase_detail_tableView")

        self.gridLayout_33.addWidget(self.purchase_detail_tableView, 0, 0, 1, 1)


        self.gridLayout_34.addLayout(self.gridLayout_33, 0, 0, 1, 1)

        self.order_tabWidget.addTab(self.purchase_detail, "")

        self.gridLayout_29.addWidget(self.order_tabWidget, 0, 0, 1, 1)


        self.gridLayout_30.addLayout(self.gridLayout_29, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.line_7 = QFrame(self.page_7)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_7)

        self.label_12 = QLabel(self.page_7)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.purchase_order_dateEdit_start = QDateEdit(self.page_7)
        self.purchase_order_dateEdit_start.setObjectName(u"purchase_order_dateEdit_start")

        self.horizontalLayout_5.addWidget(self.purchase_order_dateEdit_start)

        self.line_11 = QFrame(self.page_7)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_11)

        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.purchase_order_dateEdit_deadline = QDateEdit(self.page_7)
        self.purchase_order_dateEdit_deadline.setObjectName(u"purchase_order_dateEdit_deadline")

        self.horizontalLayout_5.addWidget(self.purchase_order_dateEdit_deadline)

        self.line_12 = QFrame(self.page_7)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_12)

        self.purchase_order_btn = QPushButton(self.page_7)
        self.purchase_order_btn.setObjectName(u"purchase_order_btn")

        self.horizontalLayout_5.addWidget(self.purchase_order_btn)

        self.line_34 = QFrame(self.page_7)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.Shape.VLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_34)

        self.purchase_order_lineEdit = QLineEdit(self.page_7)
        self.purchase_order_lineEdit.setObjectName(u"purchase_order_lineEdit")

        self.horizontalLayout_5.addWidget(self.purchase_order_lineEdit)

        self.purchase_order_select_btn = QPushButton(self.page_7)
        self.purchase_order_select_btn.setObjectName(u"purchase_order_select_btn")

        self.horizontalLayout_5.addWidget(self.purchase_order_select_btn)

        self.line_37 = QFrame(self.page_7)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_37)

        self.add_an_order_btn = QPushButton(self.page_7)
        self.add_an_order_btn.setObjectName(u"add_an_order_btn")

        self.horizontalLayout_5.addWidget(self.add_an_order_btn)

        self.purchase_add_btn = QPushButton(self.page_7)
        self.purchase_add_btn.setObjectName(u"purchase_add_btn")

        self.horizontalLayout_5.addWidget(self.purchase_add_btn)

        self.line_35 = QFrame(self.page_7)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.Shape.VLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_35)

        self.purchase_del_btn = QPushButton(self.page_7)
        self.purchase_del_btn.setObjectName(u"purchase_del_btn")

        self.horizontalLayout_5.addWidget(self.purchase_del_btn)

        self.purchase_mod_btn = QPushButton(self.page_7)
        self.purchase_mod_btn.setObjectName(u"purchase_mod_btn")

        self.horizontalLayout_5.addWidget(self.purchase_mod_btn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.gridLayout_30.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_23 = QGridLayout(self.page_8)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.drugs_on_shelves_tableView = QTableView(self.page_8)
        self.drugs_on_shelves_tableView.setObjectName(u"drugs_on_shelves_tableView")

        self.gridLayout_21.addWidget(self.drugs_on_shelves_tableView, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.line_15 = QFrame(self.page_8)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_13.addWidget(self.line_15)

        self.shelves_select_lineEdit = QLineEdit(self.page_8)
        self.shelves_select_lineEdit.setObjectName(u"shelves_select_lineEdit")

        self.horizontalLayout_13.addWidget(self.shelves_select_lineEdit)

        self.line_16 = QFrame(self.page_8)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_13.addWidget(self.line_16)

        self.shelves_select_btn = QPushButton(self.page_8)
        self.shelves_select_btn.setObjectName(u"shelves_select_btn")

        self.horizontalLayout_13.addWidget(self.shelves_select_btn)

        self.line_33 = QFrame(self.page_8)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.Shape.VLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_13.addWidget(self.line_33)

        self.shelves_add_btn = QPushButton(self.page_8)
        self.shelves_add_btn.setObjectName(u"shelves_add_btn")

        self.horizontalLayout_13.addWidget(self.shelves_add_btn)

        self.shelves_del_btn = QPushButton(self.page_8)
        self.shelves_del_btn.setObjectName(u"shelves_del_btn")

        self.horizontalLayout_13.addWidget(self.shelves_del_btn)

        self.shelves_mod_btn = QPushButton(self.page_8)
        self.shelves_mod_btn.setObjectName(u"shelves_mod_btn")

        self.horizontalLayout_13.addWidget(self.shelves_mod_btn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)


        self.gridLayout_21.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_21, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_36 = QGridLayout(self.page_9)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.inventory_check_tableView = QTableView(self.page_9)
        self.inventory_check_tableView.setObjectName(u"inventory_check_tableView")

        self.gridLayout_35.addWidget(self.inventory_check_tableView, 0, 0, 1, 1)


        self.gridLayout_36.addLayout(self.gridLayout_35, 1, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.line_31 = QFrame(self.page_9)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.Shape.VLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_31)

        self.label_14 = QLabel(self.page_9)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.inventory_check_dateEdit_start = QDateEdit(self.page_9)
        self.inventory_check_dateEdit_start.setObjectName(u"inventory_check_dateEdit_start")

        self.horizontalLayout_12.addWidget(self.inventory_check_dateEdit_start)

        self.line_13 = QFrame(self.page_9)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_13)

        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)

        self.inventory_check_dateEdit_deadline = QDateEdit(self.page_9)
        self.inventory_check_dateEdit_deadline.setObjectName(u"inventory_check_dateEdit_deadline")

        self.horizontalLayout_12.addWidget(self.inventory_check_dateEdit_deadline)

        self.line_14 = QFrame(self.page_9)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_14)

        self.inventory_check_query_btn = QPushButton(self.page_9)
        self.inventory_check_query_btn.setObjectName(u"inventory_check_query_btn")

        self.horizontalLayout_12.addWidget(self.inventory_check_query_btn)

        self.line_32 = QFrame(self.page_9)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.Shape.VLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_32)

        self.inventory_check_add_btn = QPushButton(self.page_9)
        self.inventory_check_add_btn.setObjectName(u"inventory_check_add_btn")

        self.horizontalLayout_12.addWidget(self.inventory_check_add_btn)

        self.inventory_check_del_btn = QPushButton(self.page_9)
        self.inventory_check_del_btn.setObjectName(u"inventory_check_del_btn")

        self.horizontalLayout_12.addWidget(self.inventory_check_del_btn)

        self.inventory_check_mod_btn = QPushButton(self.page_9)
        self.inventory_check_mod_btn.setObjectName(u"inventory_check_mod_btn")

        self.horizontalLayout_12.addWidget(self.inventory_check_mod_btn)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)


        self.gridLayout_36.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_9)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.gridLayout_40 = QGridLayout(self.page_11)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")

        self.gridLayout_40.addLayout(self.gridLayout_39, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.gridLayout_44 = QGridLayout(self.page_12)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.drug_tabWidget = QTabWidget(self.page_12)
        self.drug_tabWidget.setObjectName(u"drug_tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.drug_dic_tableView = QTableView(self.tab)
        self.drug_dic_tableView.setObjectName(u"drug_dic_tableView")

        self.gridLayout_4.addWidget(self.drug_dic_tableView, 0, 0, 1, 1)

        self.drug_tabWidget.addTab(self.tab, "")
        self.drug_class_pate = QWidget()
        self.drug_class_pate.setObjectName(u"drug_class_pate")
        self.gridLayout_42 = QGridLayout(self.drug_class_pate)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_41 = QGridLayout()
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.label_10 = QLabel(self.drug_class_pate)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_41.addWidget(self.label_10, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_41.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.label_8 = QLabel(self.drug_class_pate)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_41.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QLabel(self.drug_class_pate)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_41.addWidget(self.label_9, 2, 3, 1, 1)

        self.label_11 = QLabel(self.drug_class_pate)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_41.addWidget(self.label_11, 2, 1, 1, 1)

        self.drugs_set_btn = QPushButton(self.drug_class_pate)
        self.drugs_set_btn.setObjectName(u"drugs_set_btn")

        self.gridLayout_41.addWidget(self.drugs_set_btn, 0, 0, 1, 1)

        self.specifications_set_btn = QPushButton(self.drug_class_pate)
        self.specifications_set_btn.setObjectName(u"specifications_set_btn")

        self.gridLayout_41.addWidget(self.specifications_set_btn, 0, 1, 1, 1)

        self.dosage_set_btn = QPushButton(self.drug_class_pate)
        self.dosage_set_btn.setObjectName(u"dosage_set_btn")

        self.gridLayout_41.addWidget(self.dosage_set_btn, 0, 2, 1, 1)

        self.unit_set_btn = QPushButton(self.drug_class_pate)
        self.unit_set_btn.setObjectName(u"unit_set_btn")

        self.gridLayout_41.addWidget(self.unit_set_btn, 0, 3, 1, 1)

        self.drug_attr_table_view = QTableView(self.drug_class_pate)
        self.drug_attr_table_view.setObjectName(u"drug_attr_table_view")

        self.gridLayout_41.addWidget(self.drug_attr_table_view, 3, 0, 1, 1)

        self.spec_table_view = QTableView(self.drug_class_pate)
        self.spec_table_view.setObjectName(u"spec_table_view")

        self.gridLayout_41.addWidget(self.spec_table_view, 3, 1, 1, 1)

        self.dosage_table_view = QTableView(self.drug_class_pate)
        self.dosage_table_view.setObjectName(u"dosage_table_view")

        self.gridLayout_41.addWidget(self.dosage_table_view, 3, 2, 1, 1)

        self.unit_table_view = QTableView(self.drug_class_pate)
        self.unit_table_view.setObjectName(u"unit_table_view")

        self.gridLayout_41.addWidget(self.unit_table_view, 3, 3, 1, 1)


        self.gridLayout_42.addLayout(self.gridLayout_41, 0, 0, 1, 1)

        self.drug_tabWidget.addTab(self.drug_class_pate, "")

        self.gridLayout_43.addWidget(self.drug_tabWidget, 1, 0, 1, 1)


        self.gridLayout_44.addLayout(self.gridLayout_43, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.drug_dic_del_btn = QPushButton(self.page_12)
        self.drug_dic_del_btn.setObjectName(u"drug_dic_del_btn")

        self.horizontalLayout_3.addWidget(self.drug_dic_del_btn)

        self.drug_revise_btn = QPushButton(self.page_12)
        self.drug_revise_btn.setObjectName(u"drug_revise_btn")

        self.horizontalLayout_3.addWidget(self.drug_revise_btn)

        self.drug_add_btn = QPushButton(self.page_12)
        self.drug_add_btn.setObjectName(u"drug_add_btn")

        self.horizontalLayout_3.addWidget(self.drug_add_btn)


        self.gridLayout_44.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_12)

        self.gridLayout.addWidget(self.stackedWidget, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.drug_dic_btn = QPushButton(self.centralwidget)
        self.drug_dic_btn.setObjectName(u"drug_dic_btn")

        self.gridLayout_2.addWidget(self.drug_dic_btn, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1116, 33))
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.user_set_menu = QMenu(self.menubar)
        self.user_set_menu.setObjectName(u"user_set_menu")
        self.user_set_menu.setTearOffEnabled(False)
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.user_set_menu.menuAction())
        self.menu_4.addAction(self.actiond)
        self.menu_4.addAction(self.actionlight)
        self.menu_4.addAction(self.actionm)
        self.user_set_menu.addAction(self.actions)
        self.user_set_menu.addAction(self.actions_2)
        self.user_set_menu.addAction(self.actiong)

        self.retranslateUi(mainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stock_in_tabWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stock_out_tabWidget.setCurrentIndex(0)
        self.order_tabWidget.setCurrentIndex(0)
        self.drug_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u836f\u623f\u7ba1\u7406\u7cfb\u7edf", None))
        self.actionout.setText(QCoreApplication.translate("mainWindow", u"\u5bfc\u51fa\u62a5\u8868", None))
        self.actionfg.setText(QCoreApplication.translate("mainWindow", u"\u5207\u6362\u8d26\u53f7", None))
        self.actionh.setText(QCoreApplication.translate("mainWindow", u"\u5bfc\u5165\u62a5\u8868", None))
        self.actiond.setText(QCoreApplication.translate("mainWindow", u"\u6697\u8272", None))
        self.actionlight.setText(QCoreApplication.translate("mainWindow", u"\u6d45\u8272", None))
        self.actions.setText(QCoreApplication.translate("mainWindow", u"\u5f53\u524d\u8d26\u53f7", None))
        self.actions_2.setText(QCoreApplication.translate("mainWindow", u"\u4fee\u6539\u8d26\u53f7", None))
        self.actiong.setText(QCoreApplication.translate("mainWindow", u"\u7cfb\u7edf", None))
        self.actionm.setText(QCoreApplication.translate("mainWindow", u"\u9ed8\u8ba4", None))
        self.medicine.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1", None))
        self.sales_records.setText(QCoreApplication.translate("mainWindow", u"\u9500\u552e\u8bb0\u5f55", None))
        self.expiring_medicine.setText(QCoreApplication.translate("mainWindow", u"\u4e34\u671f\u836f\u54c1", None))
        self.supplier.setText(QCoreApplication.translate("mainWindow", u"\u4f9b\u5e94\u5546", None))
        self.medicine_purchase.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1\u91c7\u8d2d", None))
        self.drug_inbound.setText(QCoreApplication.translate("mainWindow", u"\u5165\u5e93\u8bb0\u5f55", None))
        self.drug_outbound.setText(QCoreApplication.translate("mainWindow", u"\u51fa\u5e93\u8bb0\u5f55", None))
        self.drugs_on_shelves.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1\u4e0a\u67b6", None))
        self.stock_in_all_btn.setText(QCoreApplication.translate("mainWindow", u"\u6240\u6709\u5e93\u5b58", None))
        self.inventory_record.setText(QCoreApplication.translate("mainWindow", u"\u76d8\u70b9\u8bb0\u5f55", None))
        self.pharmacy_operation_record.setText(QCoreApplication.translate("mainWindow", u"\u836f\u5e93\u64cd\u4f5c\u8bb0\u5f55", None))
        self.clear_btn.setText(QCoreApplication.translate("mainWindow", u"\u6e05\u7406\u5783\u573e", None))
        self.search_le.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u641c\u7d22\u836f\u54c1", None))
        self.drug_selection_query_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.drug_ref_btn.setText(QCoreApplication.translate("mainWindow", u"\u5237\u65b0\u754c\u9762", None))
        self.supplier_add_btn.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0", None))
        self.supplier_mod_btn.setText(QCoreApplication.translate("mainWindow", u"\u4fee\u6539", None))
        self.supplier_del_btn.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664", None))
        self.supplier_lineEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u8f93\u5165\u4f9b\u5e94\u5546\u67e5\u8be2", None))
        self.supplier_query_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.stock_in_tabWidget.setTabText(self.stock_in_tabWidget.indexOf(self.stock_in_main), QCoreApplication.translate("mainWindow", u"\u5165\u5e93\u4e3b\u8868", None))
        self.stock_in_tabWidget.setTabText(self.stock_in_tabWidget.indexOf(self.stock_in_detail), QCoreApplication.translate("mainWindow", u"\u5165\u5e93\u660e\u7ec6\u8868", None))
        self.label_18.setText(QCoreApplication.translate("mainWindow", u"\u8d77\u59cb\u65e5\u671f", None))
        self.label_19.setText(QCoreApplication.translate("mainWindow", u"\u622a\u6b62\u65e5\u671f", None))
        self.storage_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.stock_in_lineEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u8f93\u5165\u5546\u54c1\u8ba2\u5355\u53f7", None))
        self.stock_in_query_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2\u8ba2\u5355", None))
        self.add_stock_location_btn.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u5b58\u50a8\u4f4d\u7f6e", None))
        self.stock_in_btn.setText(QCoreApplication.translate("mainWindow", u"\u5165\u5e93\u5904\u7406", None))
        self.stock_del_btn.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664", None))
        self.stock_mod_btn.setText(QCoreApplication.translate("mainWindow", u"\u4fee\u6539\u5165\u5e93\u4e3b\u8868", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\u8d77\u59cb\u65e5\u671f", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"\u622a\u6b62\u65e5\u671f", None))
        self.inventory_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.inventory_del_btn.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u" \u9500\u552e\u5355", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("mainWindow", u"\u9500\u552e\u8be6\u60c5", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u8d77\u59cb\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\u622a\u6b62\u65e5\u671f", None))
        self.sales_records_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.sales_records_lineEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u8f93\u5165\u9500\u552e\u5355\u53f7", None))
        self.sales_rec_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2\u9500\u552e\u5355", None))
        self.add_sell_list_btn.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u9500\u552e\u5355", None))
        self.sell_drug_btn.setText(QCoreApplication.translate("mainWindow", u"\u52a0\u5165\u9500\u552e\u836f\u54c1", None))
        self.sell_del_btn.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\u4e34\u671f\u63d0\u9192\u5929\u6570", None))
        self.expiring_drugs_lineEdit_day.setText(QCoreApplication.translate("mainWindow", u"60", None))
        self.expiring_drugs_save_btn.setText(QCoreApplication.translate("mainWindow", u"\u4fdd\u5b58\u5929\u6570", None))
        self.ex_ref_btn.setText(QCoreApplication.translate("mainWindow", u"\u5237\u65b0\u6570\u636e", None))
        self.stock_out_tabWidget.setTabText(self.stock_out_tabWidget.indexOf(self.stock_out_main), QCoreApplication.translate("mainWindow", u"\u51fa\u5e93\u4e3b\u8868", None))
        self.stock_out_tabWidget.setTabText(self.stock_out_tabWidget.indexOf(self.stock_out_detail), QCoreApplication.translate("mainWindow", u"\u51fa\u5e93\u660e\u7ec6", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"\u8d77\u59cb\u65f6\u95f4", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"\u622a\u6b62\u65f6\u95f4", None))
        self.stock_out_query_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.stock_out_number_lineEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u8f93\u5165\u51fa\u5e93\u5355", None))
        self.stock_out_list_select_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2\u8ba2\u5355", None))
        self.stock_out_add_btn.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u51fa\u5e93\u5355", None))
        self.stock_out_add_drug_btn.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u51fa\u5e93\u836f\u54c1", None))
        self.stock_out_del_btn.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664", None))
        self.stock_out_mod_btn.setText(QCoreApplication.translate("mainWindow", u"\u4fee\u6539", None))
        self.order_tabWidget.setTabText(self.order_tabWidget.indexOf(self.purchase_order), QCoreApplication.translate("mainWindow", u"\u91c7\u8d2d\u8ba2\u5355\u8868", None))
        self.order_tabWidget.setTabText(self.order_tabWidget.indexOf(self.purchase_detail), QCoreApplication.translate("mainWindow", u"\u91c7\u8d2d\u660e\u7ec6\u8868", None))
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"\u8d77\u59cb\u65f6\u95f4", None))
        self.label_13.setText(QCoreApplication.translate("mainWindow", u"\u622a\u6b62\u65f6\u95f4", None))
        self.purchase_order_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.purchase_order_lineEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u8f93\u5165\u8ba2\u5355\u53f7", None))
        self.purchase_order_select_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2\u8ba2\u5355", None))
        self.add_an_order_btn.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u8ba2\u5355", None))
        self.purchase_add_btn.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u91c7\u8d2d\u836f\u54c1", None))
        self.purchase_del_btn.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664\u8ba2\u5355", None))
        self.purchase_mod_btn.setText(QCoreApplication.translate("mainWindow", u"\u4fee\u6539\u8ba2\u5355", None))
        self.shelves_select_lineEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u8f93\u5165\u5355\u53f7", None))
        self.shelves_select_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.shelves_add_btn.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u836f\u54c1", None))
        self.shelves_del_btn.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664\u836f\u54c1", None))
        self.shelves_mod_btn.setText(QCoreApplication.translate("mainWindow", u"\u4fee\u6539\u836f\u54c1", None))
        self.label_14.setText(QCoreApplication.translate("mainWindow", u"\u8d77\u59cb\u65f6\u95f4", None))
        self.label_15.setText(QCoreApplication.translate("mainWindow", u"\u622a\u6b62\u65f6\u95f4", None))
        self.inventory_check_query_btn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.inventory_check_add_btn.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0", None))
        self.inventory_check_del_btn.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664", None))
        self.inventory_check_mod_btn.setText(QCoreApplication.translate("mainWindow", u"\u4fee\u6539", None))
        self.drug_tabWidget.setTabText(self.drug_tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"\u57fa\u672c\u4fe1\u606f", None))
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"\u5242\u578b", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1\u5c5e\u6027", None))
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"\u6700\u5c0f\u5355\u4f4d", None))
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"\u89c4\u683c", None))
        self.drugs_set_btn.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1\u8bbe\u7f6e", None))
        self.specifications_set_btn.setText(QCoreApplication.translate("mainWindow", u"\u89c4\u683c\u8bbe\u7f6e", None))
        self.dosage_set_btn.setText(QCoreApplication.translate("mainWindow", u"\u5242\u578b\u8bbe\u7f6e", None))
        self.unit_set_btn.setText(QCoreApplication.translate("mainWindow", u"\u5355\u4f4d\u8bbe\u7f6e", None))
        self.drug_tabWidget.setTabText(self.drug_tabWidget.indexOf(self.drug_class_pate), QCoreApplication.translate("mainWindow", u"\u5206\u7c7b\u8bbe\u7f6e", None))
        self.drug_dic_del_btn.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664", None))
        self.drug_revise_btn.setText(QCoreApplication.translate("mainWindow", u"\u4fee\u6539\u836f\u54c1", None))
        self.drug_add_btn.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u836f\u54c1", None))
        self.drug_dic_btn.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1\u8bcd\u5178", None))
        self.menu_4.setTitle(QCoreApplication.translate("mainWindow", u"\u4e3b\u9898", None))
        self.user_set_menu.setTitle(QCoreApplication.translate("mainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

