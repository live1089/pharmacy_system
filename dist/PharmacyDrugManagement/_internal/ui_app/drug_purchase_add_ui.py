# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drug_purchase_add.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QGridLayout, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_PurchaseDialog(object):
    def setupUi(self, PurchaseDialog):
        if not PurchaseDialog.objectName():
            PurchaseDialog.setObjectName(u"PurchaseDialog")
        PurchaseDialog.resize(612, 220)
        self.gridLayout_2 = QGridLayout(PurchaseDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.purchase_save_btn = QPushButton(PurchaseDialog)
        self.purchase_save_btn.setObjectName(u"purchase_save_btn")

        self.gridLayout_2.addWidget(self.purchase_save_btn, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(PurchaseDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.total_amount_order_double = QDoubleSpinBox(PurchaseDialog)
        self.total_amount_order_double.setObjectName(u"total_amount_order_double")
        self.total_amount_order_double.setMaximum(9999999999.989999771118164)

        self.gridLayout.addWidget(self.total_amount_order_double, 4, 1, 1, 1)

        self.label_9 = QLabel(PurchaseDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)

        self.purchase_unit_price_double = QDoubleSpinBox(PurchaseDialog)
        self.purchase_unit_price_double.setObjectName(u"purchase_unit_price_double")
        self.purchase_unit_price_double.setMaximum(999999.989999999990687)

        self.gridLayout.addWidget(self.purchase_unit_price_double, 2, 4, 1, 1)

        self.label_7 = QLabel(PurchaseDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.purchase_notes_plain_text = QPlainTextEdit(PurchaseDialog)
        self.purchase_notes_plain_text.setObjectName(u"purchase_notes_plain_text")
        self.purchase_notes_plain_text.setMinimumSize(QSize(0, 0))
        self.purchase_notes_plain_text.setMaximumSize(QSize(99999, 50))

        self.gridLayout.addWidget(self.purchase_notes_plain_text, 4, 4, 1, 1)

        self.label_6 = QLabel(PurchaseDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.label_4 = QLabel(PurchaseDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.drug_purchase_combox = QComboBox(PurchaseDialog)
        self.drug_purchase_combox.setObjectName(u"drug_purchase_combox")
        self.drug_purchase_combox.setEditable(True)

        self.gridLayout.addWidget(self.drug_purchase_combox, 1, 1, 1, 1)

        self.label = QLabel(PurchaseDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.quantity_purchased_spin_box = QSpinBox(PurchaseDialog)
        self.quantity_purchased_spin_box.setObjectName(u"quantity_purchased_spin_box")
        self.quantity_purchased_spin_box.setMinimum(1)
        self.quantity_purchased_spin_box.setMaximum(9999999)

        self.gridLayout.addWidget(self.quantity_purchased_spin_box, 2, 1, 1, 1)

        self.order_number_combox = QComboBox(PurchaseDialog)
        self.order_number_combox.setObjectName(u"order_number_combox")
        self.order_number_combox.setEditable(True)

        self.gridLayout.addWidget(self.order_number_combox, 1, 4, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(PurchaseDialog)

        QMetaObject.connectSlotsByName(PurchaseDialog)
    # setupUi

    def retranslateUi(self, PurchaseDialog):
        PurchaseDialog.setWindowTitle(QCoreApplication.translate("PurchaseDialog", u"\u6dfb\u52a0\u91c7\u8d2d\u836f\u54c1", None))
        self.purchase_save_btn.setText(QCoreApplication.translate("PurchaseDialog", u"\u4fdd\u5b58", None))
        self.label_8.setText(QCoreApplication.translate("PurchaseDialog", u"\u91c7\u8d2d\u6570\u91cf", None))
        self.label_9.setText(QCoreApplication.translate("PurchaseDialog", u"\u5907\u6ce8", None))
        self.label_7.setText(QCoreApplication.translate("PurchaseDialog", u"\u836f\u54c1", None))
        self.label_6.setText(QCoreApplication.translate("PurchaseDialog", u"\u91c7\u8d2d\u5355\u4ef7", None))
        self.label_4.setText(QCoreApplication.translate("PurchaseDialog", u"\u91c7\u8d2d\u603b\u4ef7", None))
        self.label.setText(QCoreApplication.translate("PurchaseDialog", u"\u8ba2\u5355\u53f7", None))
    # retranslateUi

