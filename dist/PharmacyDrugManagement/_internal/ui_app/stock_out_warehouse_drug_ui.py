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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_OutWarehouseDrugDialog(object):
    def setupUi(self, OutWarehouseDrugDialog):
        if not OutWarehouseDrugDialog.objectName():
            OutWarehouseDrugDialog.setObjectName(u"OutWarehouseDrugDialog")
        OutWarehouseDrugDialog.resize(412, 238)
        self.gridLayout_2 = QGridLayout(OutWarehouseDrugDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel(OutWarehouseDrugDialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)

        self.stock_out_dateTimeEdit = QDateTimeEdit(OutWarehouseDrugDialog)
        self.stock_out_dateTimeEdit.setObjectName(u"stock_out_dateTimeEdit")

        self.gridLayout.addWidget(self.stock_out_dateTimeEdit, 6, 1, 1, 1)

        self.stock_out_drug_combox = QComboBox(OutWarehouseDrugDialog)
        self.stock_out_drug_combox.setObjectName(u"stock_out_drug_combox")
        self.stock_out_drug_combox.setEditable(True)

        self.gridLayout.addWidget(self.stock_out_drug_combox, 3, 1, 1, 1)

        self.label_4 = QLabel(OutWarehouseDrugDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_3 = QLabel(OutWarehouseDrugDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.stock_out_number_spinBox = QSpinBox(OutWarehouseDrugDialog)
        self.stock_out_number_spinBox.setObjectName(u"stock_out_number_spinBox")
        self.stock_out_number_spinBox.setMinimum(1)
        self.stock_out_number_spinBox.setMaximum(999999999)
        self.stock_out_number_spinBox.setValue(1)

        self.gridLayout.addWidget(self.stock_out_number_spinBox, 4, 1, 1, 1)

        self.label = QLabel(OutWarehouseDrugDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.stock_batch_combox = QComboBox(OutWarehouseDrugDialog)
        self.stock_batch_combox.setObjectName(u"stock_batch_combox")
        self.stock_batch_combox.setEditable(True)

        self.gridLayout.addWidget(self.stock_batch_combox, 1, 1, 1, 1)

        self.label_5 = QLabel(OutWarehouseDrugDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.stock_out_list_combox = QComboBox(OutWarehouseDrugDialog)
        self.stock_out_list_combox.setObjectName(u"stock_out_list_combox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_out_list_combox.sizePolicy().hasHeightForWidth())
        self.stock_out_list_combox.setSizePolicy(sizePolicy)
        self.stock_out_list_combox.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.stock_out_list_combox, 0, 1, 1, 1)

        self.label_2 = QLabel(OutWarehouseDrugDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.outbatch_lineEdit = QLineEdit(OutWarehouseDrugDialog)
        self.outbatch_lineEdit.setObjectName(u"outbatch_lineEdit")
        self.outbatch_lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.outbatch_lineEdit, 2, 1, 1, 1)

        self.label_6 = QLabel(OutWarehouseDrugDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.current_inventory_label = QLabel(OutWarehouseDrugDialog)
        self.current_inventory_label.setObjectName(u"current_inventory_label")
        self.current_inventory_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.current_inventory_label, 5, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.stock_out_warehouse_drug_save_btn = QPushButton(OutWarehouseDrugDialog)
        self.stock_out_warehouse_drug_save_btn.setObjectName(u"stock_out_warehouse_drug_save_btn")

        self.gridLayout_2.addWidget(self.stock_out_warehouse_drug_save_btn, 1, 0, 1, 1)


        self.retranslateUi(OutWarehouseDrugDialog)

        QMetaObject.connectSlotsByName(OutWarehouseDrugDialog)
    # setupUi

    def retranslateUi(self, OutWarehouseDrugDialog):
        OutWarehouseDrugDialog.setWindowTitle(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u51fa\u5e93\u836f\u54c1", None))
        self.label_11.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u51fa\u5e93\u65f6\u95f4", None))
        self.label_4.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u5e93\u5b58\u6279\u6b21", None))
        self.label_3.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u51fa\u5e93\u5355", None))
        self.label.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u51fa\u5e93\u836f\u54c1", None))
        self.label_5.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u51fa\u5e93\u6279\u6b21", None))
        self.label_2.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u51fa\u5e93\u6570\u91cf", None))
        self.label_6.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u5f53\u524d\u5e93\u5b58", None))
        self.current_inventory_label.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u672a\u77e5", None))
        self.stock_out_warehouse_drug_save_btn.setText(QCoreApplication.translate("OutWarehouseDrugDialog", u"\u4fdd\u5b58", None))
    # retranslateUi

