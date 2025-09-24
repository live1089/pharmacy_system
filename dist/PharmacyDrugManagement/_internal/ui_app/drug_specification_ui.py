# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drug_specification.ui'
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

class Ui_SpecificationDialog(object):
    def setupUi(self, SpecificationDialog):
        if not SpecificationDialog.objectName():
            SpecificationDialog.setObjectName(u"SpecificationDialog")
        SpecificationDialog.resize(482, 412)
        self.gridLayout_2 = QGridLayout(SpecificationDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.refresh_btn = QPushButton(SpecificationDialog)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.verticalLayout.addWidget(self.refresh_btn)

        self.add_btn = QPushButton(SpecificationDialog)
        self.add_btn.setObjectName(u"add_btn")

        self.verticalLayout.addWidget(self.add_btn)

        self.del_btn = QPushButton(SpecificationDialog)
        self.del_btn.setObjectName(u"del_btn")

        self.verticalLayout.addWidget(self.del_btn)

        self.verticalSpacer = QSpacerItem(20, 270, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.specification_tableView = QTableView(SpecificationDialog)
        self.specification_tableView.setObjectName(u"specification_tableView")

        self.gridLayout.addWidget(self.specification_tableView, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(SpecificationDialog)

        QMetaObject.connectSlotsByName(SpecificationDialog)
    # setupUi

    def retranslateUi(self, SpecificationDialog):
        SpecificationDialog.setWindowTitle(QCoreApplication.translate("SpecificationDialog", u"\u89c4\u683c\u8bbe\u7f6e", None))
        self.refresh_btn.setText(QCoreApplication.translate("SpecificationDialog", u"\u5237\u65b0", None))
        self.add_btn.setText(QCoreApplication.translate("SpecificationDialog", u"\u6dfb\u52a0", None))
        self.del_btn.setText(QCoreApplication.translate("SpecificationDialog", u"\u5220\u9664", None))
    # retranslateUi

