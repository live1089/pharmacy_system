# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drug_unit.ui'
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

class Ui_UnitDialog(object):
    def setupUi(self, UnitDialog):
        if not UnitDialog.objectName():
            UnitDialog.setObjectName(u"UnitDialog")
        UnitDialog.resize(485, 412)
        self.gridLayout_2 = QGridLayout(UnitDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.refresh_btn = QPushButton(UnitDialog)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.verticalLayout.addWidget(self.refresh_btn)

        self.add_btn = QPushButton(UnitDialog)
        self.add_btn.setObjectName(u"add_btn")

        self.verticalLayout.addWidget(self.add_btn)

        self.del_btn = QPushButton(UnitDialog)
        self.del_btn.setObjectName(u"del_btn")

        self.verticalLayout.addWidget(self.del_btn)

        self.modify_btn = QPushButton(UnitDialog)
        self.modify_btn.setObjectName(u"modify_btn")

        self.verticalLayout.addWidget(self.modify_btn)

        self.verticalSpacer = QSpacerItem(20, 270, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.unit_set_tableView = QTableView(UnitDialog)
        self.unit_set_tableView.setObjectName(u"unit_set_tableView")

        self.gridLayout_2.addWidget(self.unit_set_tableView, 0, 0, 1, 1)


        self.retranslateUi(UnitDialog)

        QMetaObject.connectSlotsByName(UnitDialog)
    # setupUi

    def retranslateUi(self, UnitDialog):
        UnitDialog.setWindowTitle(QCoreApplication.translate("UnitDialog", u"\u5355\u4f4d\u8bbe\u7f6e", None))
        self.refresh_btn.setText(QCoreApplication.translate("UnitDialog", u"\u5237\u65b0", None))
        self.add_btn.setText(QCoreApplication.translate("UnitDialog", u"\u6dfb\u52a0", None))
        self.del_btn.setText(QCoreApplication.translate("UnitDialog", u"\u5220\u9664", None))
        self.modify_btn.setText(QCoreApplication.translate("UnitDialog", u"\u4fee\u6539", None))
    # retranslateUi

