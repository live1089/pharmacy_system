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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1096, 580)
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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.drug_selection = QPushButton(self.centralwidget)
        self.drug_selection.setObjectName(u"drug_selection")

        self.verticalLayout.addWidget(self.drug_selection)

        self.sales_records = QPushButton(self.centralwidget)
        self.sales_records.setObjectName(u"sales_records")

        self.verticalLayout.addWidget(self.sales_records)

        self.expiring_drugs = QPushButton(self.centralwidget)
        self.expiring_drugs.setObjectName(u"expiring_drugs")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expiring_drugs.sizePolicy().hasHeightForWidth())
        self.expiring_drugs.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.expiring_drugs)

        self.inventory_stock = QPushButton(self.centralwidget)
        self.inventory_stock.setObjectName(u"inventory_stock")

        self.verticalLayout.addWidget(self.inventory_stock)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.supplier_info = QPushButton(self.centralwidget)
        self.supplier_info.setObjectName(u"supplier_info")

        self.verticalLayout.addWidget(self.supplier_info)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.search_le = QLineEdit(self.centralwidget)
        self.search_le.setObjectName(u"search_le")

        self.gridLayout.addWidget(self.search_le, 0, 2, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)

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
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.sales_records_tableView = QTableView(self.page_2)
        self.sales_records_tableView.setObjectName(u"sales_records_tableView")

        self.gridLayout_5.addWidget(self.sales_records_tableView, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_8 = QGridLayout(self.page_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.expiring_drugs_tableView = QTableView(self.page_3)
        self.expiring_drugs_tableView.setObjectName(u"expiring_drugs_tableView")

        self.gridLayout_7.addWidget(self.expiring_drugs_tableView, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1096, 33))
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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u836f\u623f\u7ba1\u7406\u7cfb\u7edf", None))
        self.actionout.setText(QCoreApplication.translate("mainWindow", u"\u5bfc\u51fa\u62a5\u8868", None))
        self.drug_selection.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1\u9009\u62e9", None))
        self.sales_records.setText(QCoreApplication.translate("mainWindow", u"\u9500\u552e\u8bb0\u5f55", None))
        self.expiring_drugs.setText(QCoreApplication.translate("mainWindow", u"\u4e34\u671f\u836f\u54c1", None))
        self.inventory_stock.setText(QCoreApplication.translate("mainWindow", u"\u5269\u4f59\u836f\u54c1", None))
        self.supplier_info.setText(QCoreApplication.translate("mainWindow", u"\u4f9b\u5e94\u5546", None))
        self.drug_inbound.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1\u5165\u5e93", None))
        self.drug_outbound.setText(QCoreApplication.translate("mainWindow", u"\u836f\u54c1\u51fa\u5e93", None))
        self.recently_added.setText(QCoreApplication.translate("mainWindow", u"\u6700\u8fd1\u6dfb\u52a0", None))
        self.search_le.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u641c\u7d22", None))
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("mainWindow", u"\u5de5\u5177", None))
        self.menu_3.setTitle(QCoreApplication.translate("mainWindow", u"\u8d26\u53f7", None))
    # retranslateUi

