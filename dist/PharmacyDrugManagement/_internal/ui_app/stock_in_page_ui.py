# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_in_page.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QDialog, QDoubleSpinBox, QGridLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_StockDialog(object):
    def setupUi(self, StockDialog):
        if not StockDialog.objectName():
            StockDialog.setObjectName(u"StockDialog")
        StockDialog.resize(770, 343)
        self.gridLayout_2 = QGridLayout(StockDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stock_save_btn = QPushButton(StockDialog)
        self.stock_save_btn.setObjectName(u"stock_save_btn")

        self.gridLayout_2.addWidget(self.stock_save_btn, 3, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_12 = QLabel(StockDialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 7, 2, 1, 1)

        self.label_8 = QLabel(StockDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 4, 1, 1)

        self.label_11 = QLabel(StockDialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 4, 2, 1, 1)

        self.label_5 = QLabel(StockDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.Production_lot_number_line_edit = QLineEdit(StockDialog)
        self.Production_lot_number_line_edit.setObjectName(u"Production_lot_number_line_edit")

        self.gridLayout.addWidget(self.Production_lot_number_line_edit, 7, 1, 1, 1)

        self.Invoice_line_edit = QLineEdit(StockDialog)
        self.Invoice_line_edit.setObjectName(u"Invoice_line_edit")

        self.gridLayout.addWidget(self.Invoice_line_edit, 3, 1, 1, 1)

        self.label_6 = QLabel(StockDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.inbound_date_time_edit = QDateTimeEdit(StockDialog)
        self.inbound_date_time_edit.setObjectName(u"inbound_date_time_edit")

        self.gridLayout.addWidget(self.inbound_date_time_edit, 0, 5, 1, 1)

        self.label_19 = QLabel(StockDialog)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_19, 3, 2, 1, 1)

        self.stock_drug_combox = QComboBox(StockDialog)
        self.stock_drug_combox.setObjectName(u"stock_drug_combox")
        self.stock_drug_combox.setEditable(True)

        self.gridLayout.addWidget(self.stock_drug_combox, 0, 3, 1, 1)

        self.actual_incoming_quantity_spin_box = QSpinBox(StockDialog)
        self.actual_incoming_quantity_spin_box.setObjectName(u"actual_incoming_quantity_spin_box")
        self.actual_incoming_quantity_spin_box.setMaximum(999999999)

        self.gridLayout.addWidget(self.actual_incoming_quantity_spin_box, 4, 3, 1, 1)

        self.label_9 = QLabel(StockDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)

        self.label = QLabel(StockDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)

        self.label_2 = QLabel(StockDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.purchase_order_combox = QComboBox(StockDialog)
        self.purchase_order_combox.setObjectName(u"purchase_order_combox")
        self.purchase_order_combox.setEditable(True)

        self.gridLayout.addWidget(self.purchase_order_combox, 0, 1, 1, 1)

        self.incoming_quantity_spin_box = QSpinBox(StockDialog)
        self.incoming_quantity_spin_box.setObjectName(u"incoming_quantity_spin_box")
        self.incoming_quantity_spin_box.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.incoming_quantity_spin_box.setMaximum(999999999)

        self.gridLayout.addWidget(self.incoming_quantity_spin_box, 3, 3, 1, 1)

        self.label_20 = QLabel(StockDialog)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_20, 8, 0, 1, 1)

        self.warehousing_remarks_plain_text_edit = QPlainTextEdit(StockDialog)
        self.warehousing_remarks_plain_text_edit.setObjectName(u"warehousing_remarks_plain_text_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warehousing_remarks_plain_text_edit.sizePolicy().hasHeightForWidth())
        self.warehousing_remarks_plain_text_edit.setSizePolicy(sizePolicy)
        self.warehousing_remarks_plain_text_edit.setMaximumSize(QSize(16777215, 70))

        self.gridLayout.addWidget(self.warehousing_remarks_plain_text_edit, 8, 1, 1, 5)

        self.batch_lineEdit = QLineEdit(StockDialog)
        self.batch_lineEdit.setObjectName(u"batch_lineEdit")

        self.gridLayout.addWidget(self.batch_lineEdit, 4, 1, 1, 1)

        self.location_combox = QComboBox(StockDialog)
        self.location_combox.setObjectName(u"location_combox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.location_combox.sizePolicy().hasHeightForWidth())
        self.location_combox.setSizePolicy(sizePolicy1)
        self.location_combox.setMinimumSize(QSize(170, 0))
        self.location_combox.setEditable(True)

        self.gridLayout.addWidget(self.location_combox, 7, 3, 1, 1)

        self.label_7 = QLabel(StockDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 3, 4, 1, 1)

        self.inbound_amount_double = QDoubleSpinBox(StockDialog)
        self.inbound_amount_double.setObjectName(u"inbound_amount_double")
        self.inbound_amount_double.setMaximum(999999999.990000009536743)

        self.gridLayout.addWidget(self.inbound_amount_double, 3, 5, 1, 1)

        self.label_3 = QLabel(StockDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 4, 1, 1)

        self.valid_date_edit = QDateEdit(StockDialog)
        self.valid_date_edit.setObjectName(u"valid_date_edit")

        self.gridLayout.addWidget(self.valid_date_edit, 4, 5, 1, 1)


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
        self.label_12.setText(QCoreApplication.translate("StockDialog", u"\u8d27\u7269\u4f4d\u7f6e", None))
        self.label_8.setText(QCoreApplication.translate("StockDialog", u"\u5165\u5e93\u65e5\u671f", None))
        self.label_11.setText(QCoreApplication.translate("StockDialog", u"\u5b9e\u9645\u5165\u5e93\u6570\u91cf", None))
        self.label_5.setText(QCoreApplication.translate("StockDialog", u"\u53d1\u7968\u53f7", None))
        self.label_6.setText(QCoreApplication.translate("StockDialog", u"\u91c7\u8d2d\u8ba2\u5355", None))
        self.label_19.setText(QCoreApplication.translate("StockDialog", u"\u5165\u5e93\u6570\u91cf", None))
        self.label_9.setText(QCoreApplication.translate("StockDialog", u"\u5165\u5e93\u836f\u54c1", None))
        self.label.setText(QCoreApplication.translate("StockDialog", u"\u751f\u4ea7\u6279\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("StockDialog", u"\u6279\u6b21", None))
        self.label_20.setText(QCoreApplication.translate("StockDialog", u"\u5907\u6ce8", None))
        self.label_7.setText(QCoreApplication.translate("StockDialog", u"\u5165\u5e93\u603b\u91d1\u989d", None))
        self.label_3.setText(QCoreApplication.translate("StockDialog", u"\u6709\u6548\u671f", None))
    # retranslateUi

