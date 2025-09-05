# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_locaton.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_StockLocationDialog(object):
    def setupUi(self, StockLocationDialog):
        if not StockLocationDialog.objectName():
            StockLocationDialog.setObjectName(u"StockLocationDialog")
        StockLocationDialog.resize(400, 382)
        self.gridLayout_2 = QGridLayout(StockLocationDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.refresh_btn = QPushButton(StockLocationDialog)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.verticalLayout.addWidget(self.refresh_btn)

        self.add_btn = QPushButton(StockLocationDialog)
        self.add_btn.setObjectName(u"add_btn")

        self.verticalLayout.addWidget(self.add_btn)

        self.del_btn = QPushButton(StockLocationDialog)
        self.del_btn.setObjectName(u"del_btn")

        self.verticalLayout.addWidget(self.del_btn)

        self.verticalSpacer = QSpacerItem(20, 270, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 2, 1, 1)

        self.stock_set_tableView = QTableView(StockLocationDialog)
        self.stock_set_tableView.setObjectName(u"stock_set_tableView")

        self.gridLayout_2.addWidget(self.stock_set_tableView, 1, 1, 1, 1)


        self.retranslateUi(StockLocationDialog)

        QMetaObject.connectSlotsByName(StockLocationDialog)
    # setupUi

    def retranslateUi(self, StockLocationDialog):
        StockLocationDialog.setWindowTitle(QCoreApplication.translate("StockLocationDialog", u"Dialog", None))
        self.refresh_btn.setText(QCoreApplication.translate("StockLocationDialog", u"\u5237\u65b0", None))
        self.add_btn.setText(QCoreApplication.translate("StockLocationDialog", u"\u6dfb\u52a0", None))
        self.del_btn.setText(QCoreApplication.translate("StockLocationDialog", u"\u5220\u9664", None))
    # retranslateUi

