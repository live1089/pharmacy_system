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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1086, 580)
        icon = QIcon()
        icon.addFile(u"../../python_code/Res.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        self.actionout = QAction(mainWindow)
        self.actionout.setObjectName(u"actionout")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.search_le = QLineEdit(self.centralwidget)
        self.search_le.setObjectName(u"search_le")

        self.gridLayout.addWidget(self.search_le, 0, 2, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)

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

        self.pharmacy_operation_record = QPushButton(self.centralwidget)
        self.pharmacy_operation_record.setObjectName(u"pharmacy_operation_record")

        self.verticalLayout.addWidget(self.pharmacy_operation_record)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.supplier = QPushButton(self.centralwidget)
        self.supplier.setObjectName(u"supplier")

        self.verticalLayout.addWidget(self.supplier)

        self.drug_inbound = QPushButton(self.centralwidget)
        self.drug_inbound.setObjectName(u"drug_inbound")

        self.verticalLayout.addWidget(self.drug_inbound)

        self.drug_outbound = QPushButton(self.centralwidget)
        self.drug_outbound.setObjectName(u"drug_outbound")
        self.drug_outbound.setEnabled(True)
        sizePolicy.setHeightForWidth(self.drug_outbound.sizePolicy().hasHeightForWidth())
        self.drug_outbound.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.drug_outbound)

        self.recently_added = QPushButton(self.centralwidget)
        self.recently_added.setObjectName(u"recently_added")

        self.verticalLayout.addWidget(self.recently_added)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.medicine_purchase = QPushButton(self.centralwidget)
        self.medicine_purchase.setObjectName(u"medicine_purchase")

        self.verticalLayout.addWidget(self.medicine_purchase)

        self.inventory_record = QPushButton(self.centralwidget)
        self.inventory_record.setObjectName(u"inventory_record")

        self.verticalLayout.addWidget(self.inventory_record)

        self.member_customer = QPushButton(self.centralwidget)
        self.member_customer.setObjectName(u"member_customer")

        self.verticalLayout.addWidget(self.member_customer)

        self.user_information = QPushButton(self.centralwidget)
        self.user_information.setObjectName(u"user_information")

        self.verticalLayout.addWidget(self.user_information)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

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
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.drug_selection_tableView = QTableView(self.page)
        self.drug_selection_tableView.setObjectName(u"drug_selection_tableView")

        self.gridLayout_3.addWidget(self.drug_selection_tableView, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_10 = QGridLayout(self.page_1)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.supplier_tableView = QTableView(self.page_1)
        self.supplier_tableView.setObjectName(u"supplier_tableView")

        self.gridLayout_9.addWidget(self.supplier_tableView, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_12 = QGridLayout(self.page_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.stock_in_tabWidget = QTabWidget(self.page_2)
        self.stock_in_tabWidget.setObjectName(u"stock_in_tabWidget")
        self.stock_in_main = QWidget()
        self.stock_in_main.setObjectName(u"stock_in_main")
        self.gridLayout_16 = QGridLayout(self.stock_in_main)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.main_tableView = QTableView(self.stock_in_main)
        self.main_tableView.setObjectName(u"main_tableView")

        self.gridLayout_15.addWidget(self.main_tableView, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)

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
        self.inventory_batch = QWidget()
        self.inventory_batch.setObjectName(u"inventory_batch")
        self.gridLayout_20 = QGridLayout(self.inventory_batch)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.batch_tableView = QTableView(self.inventory_batch)
        self.batch_tableView.setObjectName(u"batch_tableView")

        self.gridLayout_19.addWidget(self.batch_tableView, 0, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_19, 0, 0, 1, 1)

        self.stock_in_tabWidget.addTab(self.inventory_batch, "")

        self.gridLayout_11.addWidget(self.stock_in_tabWidget, 0, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.gridLayout_12.addLayout(self.horizontalLayout, 1, 0, 1, 1)

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


        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_6 = QGridLayout(self.page_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.sales_records_tableView = QTableView(self.page_4)
        self.sales_records_tableView.setObjectName(u"sales_records_tableView")

        self.gridLayout_5.addWidget(self.sales_records_tableView, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 1, 1)

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


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

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


        self.gridLayout_24.addLayout(self.gridLayout_22, 0, 0, 1, 1)

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


        self.gridLayout_30.addLayout(self.gridLayout_29, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_23 = QGridLayout(self.page_8)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.recently_added_tableView = QTableView(self.page_8)
        self.recently_added_tableView.setObjectName(u"recently_added_tableView")

        self.gridLayout_21.addWidget(self.recently_added_tableView, 0, 0, 1, 1)


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


        self.gridLayout_36.addLayout(self.gridLayout_35, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.gridLayout_38 = QGridLayout(self.page_10)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.customers_tableView = QTableView(self.page_10)
        self.customers_tableView.setObjectName(u"customers_tableView")

        self.gridLayout_37.addWidget(self.customers_tableView, 0, 0, 1, 1)


        self.gridLayout_38.addLayout(self.gridLayout_37, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.gridLayout_40 = QGridLayout(self.page_11)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.user_tableWidget = QTableWidget(self.page_11)
        if (self.user_tableWidget.columnCount() < 3):
            self.user_tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.user_tableWidget.rowCount() < 2):
            self.user_tableWidget.setRowCount(2)
        self.user_tableWidget.setObjectName(u"user_tableWidget")

        self.gridLayout_39.addWidget(self.user_tableWidget, 0, 0, 1, 1)


        self.gridLayout_40.addLayout(self.gridLayout_39, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_11)

        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1086, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.actionout)
        self.menu.addSeparator()

        self.retranslateUi(mainWindow)

        self.stackedWidget.setCurrentIndex(11)
        self.stock_in_tabWidget.setCurrentIndex(0)
        self.stock_out_tabWidget.setCurrentIndex(0)
        self.order_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u836f\u623f\u7ba1\u7406\u7cfb\u7edf", None))
        self.actionout.setText(QCoreApplication.translate("mainWindow", u"\u5bfc\u51fa\u62a5\u8868", None))
        self.search_le.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u641c\u7d22", None))
        self.medicine.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1", None))
        self.sales_records.setText(QCoreApplication.translate("mainWindow", u"\u9500\u552e\u8bb0\u5f55", None))
        self.expiring_medicine.setText(QCoreApplication.translate("mainWindow", u"\u4e34\u671f\u836f\u54c1", None))
        self.pharmacy_operation_record.setText(QCoreApplication.translate("mainWindow", u"\u836f\u5e93\u64cd\u4f5c\u8bb0\u5f55", None))
        self.supplier.setText(QCoreApplication.translate("mainWindow", u"\u4f9b\u5e94\u5546", None))
        self.drug_inbound.setText(QCoreApplication.translate("mainWindow", u"\u5165\u5e93\u8bb0\u5f55", None))
        self.drug_outbound.setText(QCoreApplication.translate("mainWindow", u"\u51fa\u5e93\u8bb0\u5f55", None))
        self.recently_added.setText(QCoreApplication.translate("mainWindow", u"\u6700\u8fd1\u6dfb\u52a0", None))
        self.medicine_purchase.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1\u91c7\u8d2d", None))
        self.inventory_record.setText(QCoreApplication.translate("mainWindow", u"\u76d8\u70b9\u8bb0\u5f55", None))
        self.member_customer.setText(QCoreApplication.translate("mainWindow", u"\u4f1a\u5458\u5ba2\u6237", None))
        self.user_information.setText(QCoreApplication.translate("mainWindow", u"\u7528\u6237\u4fe1\u606f", None))
        self.stock_in_tabWidget.setTabText(self.stock_in_tabWidget.indexOf(self.stock_in_main), QCoreApplication.translate("mainWindow", u"\u5165\u5e93\u4e3b\u8868", None))
        self.stock_in_tabWidget.setTabText(self.stock_in_tabWidget.indexOf(self.stock_in_detail), QCoreApplication.translate("mainWindow", u"\u5165\u5e93\u660e\u7ec6\u8868", None))
        self.stock_in_tabWidget.setTabText(self.stock_in_tabWidget.indexOf(self.inventory_batch), QCoreApplication.translate("mainWindow", u"\u5165\u5e93\u6279\u6b21\u8868", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u836f\u54c1", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664\u836f\u54c1", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainWindow", u"\u4fee\u6539\u836f\u54c1", None))
        self.stock_out_tabWidget.setTabText(self.stock_out_tabWidget.indexOf(self.stock_out_main), QCoreApplication.translate("mainWindow", u"\u51fa\u5e93\u4e3b\u8868", None))
        self.stock_out_tabWidget.setTabText(self.stock_out_tabWidget.indexOf(self.stock_out_detail), QCoreApplication.translate("mainWindow", u"\u51fa\u5e93\u660e\u7ec6", None))
        self.order_tabWidget.setTabText(self.order_tabWidget.indexOf(self.purchase_order), QCoreApplication.translate("mainWindow", u"\u91c7\u8d2d\u8ba2\u5355\u8868", None))
        self.order_tabWidget.setTabText(self.order_tabWidget.indexOf(self.purchase_detail), QCoreApplication.translate("mainWindow", u"\u91c7\u8d2d\u660e\u7ec6\u8868", None))
        ___qtablewidgetitem = self.user_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem1 = self.user_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"\u7535\u8bdd", None));
        ___qtablewidgetitem2 = self.user_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"\u90ae\u7bb1", None));
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("mainWindow", u"\u5de5\u5177", None))
        self.menu_3.setTitle(QCoreApplication.translate("mainWindow", u"\u8d26\u53f7", None))
    # retranslateUi

