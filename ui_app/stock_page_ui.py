# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_page.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_StockDialog(object):
    def setupUi(self, StockDialog):
        if not StockDialog.objectName():
            StockDialog.setObjectName(u"StockDialog")
        StockDialog.resize(659, 330)
        self.gridLayout_2 = QGridLayout(StockDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stock_save_btn = QPushButton(StockDialog)
        self.stock_save_btn.setObjectName(u"stock_save_btn")

        self.gridLayout_2.addWidget(self.stock_save_btn, 3, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(StockDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)

        self.inbound_date_time_edit = QDateTimeEdit(StockDialog)
        self.inbound_date_time_edit.setObjectName(u"inbound_date_time_edit")

        self.gridLayout.addWidget(self.inbound_date_time_edit, 0, 3, 1, 1)

        self.label_10 = QLabel(StockDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.purchase_order_combox = QComboBox(StockDialog)
        self.purchase_order_combox.setObjectName(u"purchase_order_combox")
        self.purchase_order_combox.setEditable(True)

        self.gridLayout.addWidget(self.purchase_order_combox, 0, 1, 1, 1)

        self.batch_spin_box = QSpinBox(StockDialog)
        self.batch_spin_box.setObjectName(u"batch_spin_box")
        self.batch_spin_box.setMinimum(1)
        self.batch_spin_box.setMaximum(9999)

        self.gridLayout.addWidget(self.batch_spin_box, 4, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 1)

        self.label_8 = QLabel(StockDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.label_20 = QLabel(StockDialog)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_20, 9, 2, 1, 1)

        self.operator_combox = QComboBox(StockDialog)
        self.operator_combox.setObjectName(u"operator_combox")

        self.gridLayout.addWidget(self.operator_combox, 6, 1, 1, 1)

        self.warehousing_remarks_plain_text_edit = QPlainTextEdit(StockDialog)
        self.warehousing_remarks_plain_text_edit.setObjectName(u"warehousing_remarks_plain_text_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warehousing_remarks_plain_text_edit.sizePolicy().hasHeightForWidth())
        self.warehousing_remarks_plain_text_edit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.warehousing_remarks_plain_text_edit, 9, 3, 1, 1)

        self.label_6 = QLabel(StockDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.supplier_stock_combox = QComboBox(StockDialog)
        self.supplier_stock_combox.setObjectName(u"supplier_stock_combox")
        self.supplier_stock_combox.setEditable(True)

        self.gridLayout.addWidget(self.supplier_stock_combox, 9, 1, 1, 1)

        self.label_4 = QLabel(StockDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 7, 1, 1, 1)

        self.label_7 = QLabel(StockDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 6, 2, 1, 1)

        self.Invoice_line_edit = QLineEdit(StockDialog)
        self.Invoice_line_edit.setObjectName(u"Invoice_line_edit")

        self.gridLayout.addWidget(self.Invoice_line_edit, 4, 1, 1, 1)

        self.label_5 = QLabel(StockDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.inbound_amount_spin_box = QSpinBox(StockDialog)
        self.inbound_amount_spin_box.setObjectName(u"inbound_amount_spin_box")
        self.inbound_amount_spin_box.setMaximum(999999)

        self.gridLayout.addWidget(self.inbound_amount_spin_box, 6, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 2, 0, 1, 1)


        self.retranslateUi(StockDialog)

        QMetaObject.connectSlotsByName(StockDialog)
    # setupUi

    def retranslateUi(self, StockDialog):
        StockDialog.setWindowTitle(QCoreApplication.translate("StockDialog", u"\u836f\u54c1\u5165\u5e93", None))
        self.stock_save_btn.setText(QCoreApplication.translate("StockDialog", u"\u4fdd\u5b58", None))
        self.label_2.setText(QCoreApplication.translate("StockDialog", u"\u6279\u6b21", None))
        self.label_10.setText(QCoreApplication.translate("StockDialog", u"\u4f9b\u5e94\u5546", None))
        self.label_8.setText(QCoreApplication.translate("StockDialog", u"\u5165\u5e93\u65e5\u671f", None))
        self.label_20.setText(QCoreApplication.translate("StockDialog", u"\u5907\u6ce8", None))
        self.label_6.setText(QCoreApplication.translate("StockDialog", u"\u91c7\u8d2d\u8ba2\u5355", None))
        self.label_4.setText(QCoreApplication.translate("StockDialog", u"\u64cd\u4f5c\u5458", None))
        self.label_7.setText(QCoreApplication.translate("StockDialog", u"\u5165\u5e93\u603b\u91d1\u989d", None))
        self.label_5.setText(QCoreApplication.translate("StockDialog", u"\u53d1\u7968\u53f7", None))
    # retranslateUi

