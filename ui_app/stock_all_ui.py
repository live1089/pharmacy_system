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
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_StockInAllDialog(object):
    def setupUi(self, StockInAllDialog):
        if not StockInAllDialog.objectName():
            StockInAllDialog.setObjectName(u"StockInAllDialog")
        StockInAllDialog.resize(979, 544)
        self.gridLayout_2 = QGridLayout(StockInAllDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.stock_all_tableView = QTableView(StockInAllDialog)
        self.stock_all_tableView.setObjectName(u"stock_all_tableView")

        self.gridLayout.addWidget(self.stock_all_tableView, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.del_row = QPushButton(StockInAllDialog)
        self.del_row.setObjectName(u"del_row")

        self.gridLayout_2.addWidget(self.del_row, 1, 1, 1, 1)


        self.retranslateUi(StockInAllDialog)

        QMetaObject.connectSlotsByName(StockInAllDialog)
    # setupUi

    def retranslateUi(self, StockInAllDialog):
        StockInAllDialog.setWindowTitle(QCoreApplication.translate("StockInAllDialog", u"Dialog", None))
        self.del_row.setText(QCoreApplication.translate("StockInAllDialog", u"\u5220\u9664", None))
    # retranslateUi

