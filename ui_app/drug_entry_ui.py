# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drug_entry.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_DrugEntryDialog(object):
    def setupUi(self, DrugEntryDialog):
        if not DrugEntryDialog.objectName():
            DrugEntryDialog.setObjectName(u"DrugEntryDialog")
        DrugEntryDialog.resize(627, 335)
        self.gridLayout_2 = QGridLayout(DrugEntryDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.drug_entry_save_btn = QPushButton(DrugEntryDialog)
        self.drug_entry_save_btn.setObjectName(u"drug_entry_save_btn")

        self.gridLayout_2.addWidget(self.drug_entry_save_btn, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.location_line_edit = QLineEdit(DrugEntryDialog)
        self.location_line_edit.setObjectName(u"location_line_edit")

        self.gridLayout.addWidget(self.location_line_edit, 9, 1, 1, 1)

        self.stock_drug_combox = QComboBox(DrugEntryDialog)
        self.stock_drug_combox.setObjectName(u"stock_drug_combox")
        self.stock_drug_combox.setEditable(True)

        self.gridLayout.addWidget(self.stock_drug_combox, 1, 1, 1, 1)

        self.label_9 = QLabel(DrugEntryDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.expiration_date_edit = QDateEdit(DrugEntryDialog)
        self.expiration_date_edit.setObjectName(u"expiration_date_edit")

        self.gridLayout.addWidget(self.expiration_date_edit, 2, 1, 1, 1)

        self.label_12 = QLabel(DrugEntryDialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)

        self.label_11 = QLabel(DrugEntryDialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)

        self.label = QLabel(DrugEntryDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(DrugEntryDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_19 = QLabel(DrugEntryDialog)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)

        self.label_3 = QLabel(DrugEntryDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.incoming_quantity_spin_box = QSpinBox(DrugEntryDialog)
        self.incoming_quantity_spin_box.setObjectName(u"incoming_quantity_spin_box")
        self.incoming_quantity_spin_box.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.incoming_quantity_spin_box.setMaximum(99999)

        self.gridLayout.addWidget(self.incoming_quantity_spin_box, 3, 1, 1, 1)

        self.actual_incoming_quantity_spin_box = QSpinBox(DrugEntryDialog)
        self.actual_incoming_quantity_spin_box.setObjectName(u"actual_incoming_quantity_spin_box")

        self.gridLayout.addWidget(self.actual_incoming_quantity_spin_box, 5, 1, 1, 1)

        self.in_id_combox = QComboBox(DrugEntryDialog)
        self.in_id_combox.setObjectName(u"in_id_combox")
        self.in_id_combox.setEditable(True)

        self.gridLayout.addWidget(self.in_id_combox, 0, 1, 1, 1)

        self.purchase_unit_price_spin_box = QSpinBox(DrugEntryDialog)
        self.purchase_unit_price_spin_box.setObjectName(u"purchase_unit_price_spin_box")

        self.gridLayout.addWidget(self.purchase_unit_price_spin_box, 7, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(DrugEntryDialog)

        QMetaObject.connectSlotsByName(DrugEntryDialog)
    # setupUi

    def retranslateUi(self, DrugEntryDialog):
        DrugEntryDialog.setWindowTitle(QCoreApplication.translate("DrugEntryDialog", u"\u836f\u54c1\u5f55\u5165", None))
        self.drug_entry_save_btn.setText(QCoreApplication.translate("DrugEntryDialog", u"\u4fdd\u5b58", None))
        self.label_9.setText(QCoreApplication.translate("DrugEntryDialog", u"\u91c7\u8d2d\u5355\u4ef7", None))
        self.label_12.setText(QCoreApplication.translate("DrugEntryDialog", u"\u8d27\u7269\u4f4d\u7f6e", None))
        self.label_11.setText(QCoreApplication.translate("DrugEntryDialog", u"\u5b9e\u9645\u5165\u5e93\u6570\u91cf", None))
        self.label.setText(QCoreApplication.translate("DrugEntryDialog", u"\u5165\u5e93\u836f\u54c1", None))
        self.label_2.setText(QCoreApplication.translate("DrugEntryDialog", u"\u5165\u5e93\u5355", None))
        self.label_19.setText(QCoreApplication.translate("DrugEntryDialog", u"\u5165\u5e93\u6570\u91cf", None))
        self.label_3.setText(QCoreApplication.translate("DrugEntryDialog", u"\u6709\u6548\u671f", None))
    # retranslateUi

