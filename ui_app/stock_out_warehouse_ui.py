# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_out_warehouse.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QGridLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_OutWarehouseMTDialog(object):
    def setupUi(self, OutWarehouseMTDialog):
        if not OutWarehouseMTDialog.objectName():
            OutWarehouseMTDialog.setObjectName(u"OutWarehouseMTDialog")
        OutWarehouseMTDialog.resize(582, 296)
        self.gridLayout_2 = QGridLayout(OutWarehouseMTDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(OutWarehouseMTDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_4 = QLabel(OutWarehouseMTDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.outbound_number_lineEdit = QLineEdit(OutWarehouseMTDialog)
        self.outbound_number_lineEdit.setObjectName(u"outbound_number_lineEdit")

        self.gridLayout.addWidget(self.outbound_number_lineEdit, 0, 1, 1, 1)

        self.label_8 = QLabel(OutWarehouseMTDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)

        self.label = QLabel(OutWarehouseMTDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(OutWarehouseMTDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_2 = QLabel(OutWarehouseMTDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.stock_out_total_amount_spinBox = QSpinBox(OutWarehouseMTDialog)
        self.stock_out_total_amount_spinBox.setObjectName(u"stock_out_total_amount_spinBox")
        self.stock_out_total_amount_spinBox.setMaximum(1000000000)

        self.gridLayout.addWidget(self.stock_out_total_amount_spinBox, 0, 3, 1, 1)

        self.stock_out_operator_combox = QComboBox(OutWarehouseMTDialog)
        self.stock_out_operator_combox.setObjectName(u"stock_out_operator_combox")

        self.gridLayout.addWidget(self.stock_out_operator_combox, 1, 3, 1, 1)

        self.stock_out_remark_plainTextEdit = QPlainTextEdit(OutWarehouseMTDialog)
        self.stock_out_remark_plainTextEdit.setObjectName(u"stock_out_remark_plainTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_out_remark_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.stock_out_remark_plainTextEdit.setSizePolicy(sizePolicy)
        self.stock_out_remark_plainTextEdit.setMaximumSize(QSize(16777215, 100))

        self.gridLayout.addWidget(self.stock_out_remark_plainTextEdit, 2, 3, 1, 1)

        self.stock_out_dateTime = QDateTimeEdit(OutWarehouseMTDialog)
        self.stock_out_dateTime.setObjectName(u"stock_out_dateTime")

        self.gridLayout.addWidget(self.stock_out_dateTime, 2, 1, 1, 1)

        self.stock_out_type_combox = QComboBox(OutWarehouseMTDialog)
        self.stock_out_type_combox.setObjectName(u"stock_out_type_combox")

        self.gridLayout.addWidget(self.stock_out_type_combox, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.out_warehouse_save_btn = QPushButton(OutWarehouseMTDialog)
        self.out_warehouse_save_btn.setObjectName(u"out_warehouse_save_btn")

        self.gridLayout_2.addWidget(self.out_warehouse_save_btn, 1, 0, 1, 1)


        self.retranslateUi(OutWarehouseMTDialog)

        QMetaObject.connectSlotsByName(OutWarehouseMTDialog)
    # setupUi

    def retranslateUi(self, OutWarehouseMTDialog):
        OutWarehouseMTDialog.setWindowTitle(QCoreApplication.translate("OutWarehouseMTDialog", u"\u51fa\u5e93\u5355", None))
        self.label_5.setText(QCoreApplication.translate("OutWarehouseMTDialog", u"\u51fa\u5e93\u603b\u989d", None))
        self.label_4.setText(QCoreApplication.translate("OutWarehouseMTDialog", u"\u51fa\u5e93\u65f6\u95f4", None))
        self.label_8.setText(QCoreApplication.translate("OutWarehouseMTDialog", u"\u5907\u6ce8", None))
        self.label.setText(QCoreApplication.translate("OutWarehouseMTDialog", u"\u51fa\u5e93\u7f16\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("OutWarehouseMTDialog", u"\u64cd\u4f5c\u5458", None))
        self.label_2.setText(QCoreApplication.translate("OutWarehouseMTDialog", u"\u51fa\u5e93\u7c7b\u578b", None))
        self.out_warehouse_save_btn.setText(QCoreApplication.translate("OutWarehouseMTDialog", u"\u4fdd\u5b58", None))
    # retranslateUi

