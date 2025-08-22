# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_out_warehouse_drug.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QSizePolicy,
    QSpinBox, QWidget)

class Ui_OutWarehouseDrugDialog(object):
    def setupUi(self, OutWarehouseDrugDialog):
        if not OutWarehouseDrugDialog.objectName():
            OutWarehouseDrugDialog.setObjectName(u"OutWarehouseDrugDialog")
        OutWarehouseDrugDialog.resize(385, 159)
        self.gridLayout_2 = QGridLayout(OutWarehouseDrugDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(OutWarehouseDrugDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.stock_out_drug_combox = QComboBox(OutWarehouseDrugDialog)
        self.stock_out_drug_combox.setObjectName(u"stock_out_drug_combox")
        self.stock_out_drug_combox.setEditable(True)

        self.gridLayout.addWidget(self.stock_out_drug_combox, 1, 1, 1, 1)

        self.label = QLabel(OutWarehouseDrugDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(OutWarehouseDrugDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.stock_out_number_spinBox = QSpinBox(OutWarehouseDrugDialog)
        self.stock_out_number_spinBox.setObjectName(u"stock_out_number_spinBox")
        self.stock_out_number_spinBox.setMinimum(1)
        self.stock_out_number_spinBox.setMaximum(999999999)
        self.stock_out_number_spinBox.setValue(1)

        self.gridLayout.addWidget(self.stock_out_number_spinBox, 2, 1, 1, 1)

        self.stock_out_list_combox = QComboBox(OutWarehouseDrugDialog)
        self.stock_out_list_combox.setObjectName(u"stock_out_list_combox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_out_list_combox.sizePolicy().hasHeightForWidth())
        self.stock_out_list_combox.setSizePolicy(sizePolicy)
        self.stock_out_list_combox.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.stock_out_list_combox, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(OutWarehouseDrugDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMouseTracking(False)
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(OutWarehouseDrugDialog)

        QMetaObject.connectSlotsByName(OutWarehouseDrugDialog)
    # setupUi

    def retranslateUi(self, OutWarehouseDrugDialog):
        OutWarehouseDrugDialog.setWindowTitle(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u51fa\u5e93\u836f\u54c1", None))
        self.label_2.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u51fa\u5e93\u6570\u91cf", None))
        self.label.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u51fa\u5e93\u836f\u54c1", None))
        self.label_3.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u51fa\u5e93\u5355", None))
    # retranslateUi

