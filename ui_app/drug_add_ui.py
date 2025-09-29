# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drug_add.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(624, 250)
        Dialog.setMinimumSize(QSize(0, 0))
        Dialog.setMaximumSize(QSize(5316, 2024))
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.drug_add_save_btn = QPushButton(Dialog)
        self.drug_add_save_btn.setObjectName(u"drug_add_save_btn")

        self.gridLayout_2.addWidget(self.drug_add_save_btn, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.drug_name_line_edit = QLineEdit(Dialog)
        self.drug_name_line_edit.setObjectName(u"drug_name_line_edit")

        self.gridLayout.addWidget(self.drug_name_line_edit, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.drug_unit_combox = QComboBox(Dialog)
        self.drug_unit_combox.setObjectName(u"drug_unit_combox")

        self.gridLayout.addWidget(self.drug_unit_combox, 2, 3, 1, 1)

        self.manufacturer_line_edit = QLineEdit(Dialog)
        self.manufacturer_line_edit.setObjectName(u"manufacturer_line_edit")

        self.gridLayout.addWidget(self.manufacturer_line_edit, 3, 3, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 4, 2, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)

        self.pack_combox = QComboBox(Dialog)
        self.pack_combox.setObjectName(u"pack_combox")

        self.gridLayout.addWidget(self.pack_combox, 1, 3, 1, 1)

        self.dosage_combox = QComboBox(Dialog)
        self.dosage_combox.setObjectName(u"dosage_combox")

        self.gridLayout.addWidget(self.dosage_combox, 4, 1, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.generic_name_line_edit = QLineEdit(Dialog)
        self.generic_name_line_edit.setObjectName(u"generic_name_line_edit")

        self.gridLayout.addWidget(self.generic_name_line_edit, 0, 3, 1, 1)

        self.cmsw_line_edit = QLineEdit(Dialog)
        self.cmsw_line_edit.setObjectName(u"cmsw_line_edit")

        self.gridLayout.addWidget(self.cmsw_line_edit, 2, 1, 1, 1)

        self.drug_classify_combox = QComboBox(Dialog)
        self.drug_classify_combox.setObjectName(u"drug_classify_combox")

        self.gridLayout.addWidget(self.drug_classify_combox, 1, 1, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.price_line_edit = QLineEdit(Dialog)
        self.price_line_edit.setObjectName(u"price_line_edit")

        self.gridLayout.addWidget(self.price_line_edit, 3, 1, 1, 1)

        self.label_21 = QLabel(Dialog)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_21, 5, 0, 1, 1)

        self.display_area_threshold_spinBox = QSpinBox(Dialog)
        self.display_area_threshold_spinBox.setObjectName(u"display_area_threshold_spinBox")
        self.display_area_threshold_spinBox.setMaximum(99999999)
        self.display_area_threshold_spinBox.setValue(15)

        self.gridLayout.addWidget(self.display_area_threshold_spinBox, 4, 3, 1, 1)

        self.pharmacy_threshold_spinBox = QSpinBox(Dialog)
        self.pharmacy_threshold_spinBox.setObjectName(u"pharmacy_threshold_spinBox")
        self.pharmacy_threshold_spinBox.setMaximum(9999999)
        self.pharmacy_threshold_spinBox.setValue(100)

        self.gridLayout.addWidget(self.pharmacy_threshold_spinBox, 5, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u6dfb\u52a0", None))
        self.drug_add_save_btn.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u751f\u4ea7\u5382\u5bb6", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5305\u88c5\u89c4\u683c", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u56fd\u836f\u51c6\u5b57", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u4ef7      \u683c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u540d\u79f0", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u901a\u7528\u540d\u79f0", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u67b6\u9608\u503c\u5e93\u5b58", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u5355\u4f4d", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u5242      \u578b", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u836f\u54c1\u5206\u7c7b", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"\u836f\u5e93\u5e93\u5b58\u9608\u503c", None))
    # retranslateUi

