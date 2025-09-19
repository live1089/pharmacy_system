# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_all.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHeaderView,
    QSizePolicy, QTabWidget, QTableView, QWidget)

class Ui_StockInAllDialog(object):
    def setupUi(self, StockInAllDialog):
        if not StockInAllDialog.objectName():
            StockInAllDialog.setObjectName(u"StockInAllDialog")
        StockInAllDialog.resize(979, 544)
        self.gridLayout_2 = QGridLayout(StockInAllDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(StockInAllDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.shelves_stock_tableView = QTableView(self.tab)
        self.shelves_stock_tableView.setObjectName(u"shelves_stock_tableView")

        self.gridLayout_5.addWidget(self.shelves_stock_tableView, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stock_all_tableView = QTableView(self.tab_2)
        self.stock_all_tableView.setObjectName(u"stock_all_tableView")

        self.gridLayout_3.addWidget(self.stock_all_tableView, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.retranslateUi(StockInAllDialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StockInAllDialog)
    # setupUi

    def retranslateUi(self, StockInAllDialog):
        StockInAllDialog.setWindowTitle(QCoreApplication.translate("StockInAllDialog", u"\u836f\u54c1\u5e93\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("StockInAllDialog", u"\u4e0a\u67b6\u5e93\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("StockInAllDialog", u"\u4ed3\u5e93\u5e93\u5b58", None))
    # retranslateUi

