# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sell_drug.ui'
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
    QSizePolicy, QSpacerItem, QWidget)

class Ui_SellDialog(object):
    def setupUi(self, SellDialog):
        if not SellDialog.objectName():
            SellDialog.setObjectName(u"SellDialog")
        SellDialog.resize(706, 363)
        self.gridLayout_2 = QGridLayout(SellDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(83, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(83, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(SellDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.sell_drug_time = QDateTimeEdit(SellDialog)
        self.sell_drug_time.setObjectName(u"sell_drug_time")
        self.sell_drug_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sell_drug_time.setReadOnly(True)

        self.gridLayout.addWidget(self.sell_drug_time, 3, 1, 1, 1)

        self.label_3 = QLabel(SellDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.customer_line_edit = QLineEdit(SellDialog)
        self.customer_line_edit.setObjectName(u"customer_line_edit")

        self.gridLayout.addWidget(self.customer_line_edit, 2, 1, 1, 1)

        self.label_2 = QLabel(SellDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.sell_drug_combox = QComboBox(SellDialog)
        self.sell_drug_combox.setObjectName(u"sell_drug_combox")
        self.sell_drug_combox.setEditable(True)

        self.gridLayout.addWidget(self.sell_drug_combox, 0, 1, 1, 1)

        self.number_lineEdit = QLineEdit(SellDialog)
        self.number_lineEdit.setObjectName(u"number_lineEdit")

        self.gridLayout.addWidget(self.number_lineEdit, 1, 1, 1, 1)

        self.label = QLabel(SellDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.sell_sure_btn = QPushButton(SellDialog)
        self.sell_sure_btn.setObjectName(u"sell_sure_btn")

        self.gridLayout_2.addWidget(self.sell_sure_btn, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)


        self.retranslateUi(SellDialog)

        QMetaObject.connectSlotsByName(SellDialog)
    # setupUi

    def retranslateUi(self, SellDialog):
        SellDialog.setWindowTitle(QCoreApplication.translate("SellDialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("SellDialog", u"\u9500\u552e\u65f6\u95f4", None))
        self.label_3.setText(QCoreApplication.translate("SellDialog", u"\u987e\u5ba2", None))
        self.label_2.setText(QCoreApplication.translate("SellDialog", u"\u6570\u91cf", None))
        self.label.setText(QCoreApplication.translate("SellDialog", u"\u836f\u54c1", None))
        self.sell_sure_btn.setText(QCoreApplication.translate("SellDialog", u"\u786e\u8ba4", None))
    # retranslateUi

