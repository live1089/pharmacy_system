# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sell_list.ui'
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
    QSizePolicy, QWidget)

class Ui_SellListDialog(object):
    def setupUi(self, SellListDialog):
        if not SellListDialog.objectName():
            SellListDialog.setObjectName(u"SellListDialog")
        SellListDialog.resize(393, 148)
        self.gridLayout_2 = QGridLayout(SellListDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(SellListDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(SellListDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(SellListDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.sell_dateTimeEdit = QDateTimeEdit(SellListDialog)
        self.sell_dateTimeEdit.setObjectName(u"sell_dateTimeEdit")

        self.gridLayout.addWidget(self.sell_dateTimeEdit, 2, 1, 1, 1)

        self.sell_user_comboBox = QComboBox(SellListDialog)
        self.sell_user_comboBox.setObjectName(u"sell_user_comboBox")

        self.gridLayout.addWidget(self.sell_user_comboBox, 1, 1, 1, 1)

        self.sell_list_lineEdit = QLineEdit(SellListDialog)
        self.sell_list_lineEdit.setObjectName(u"sell_list_lineEdit")

        self.gridLayout.addWidget(self.sell_list_lineEdit, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.sell_list_save_btn = QPushButton(SellListDialog)
        self.sell_list_save_btn.setObjectName(u"sell_list_save_btn")

        self.gridLayout_2.addWidget(self.sell_list_save_btn, 1, 0, 1, 1)


        self.retranslateUi(SellListDialog)

        QMetaObject.connectSlotsByName(SellListDialog)
    # setupUi

    def retranslateUi(self, SellListDialog):
        SellListDialog.setWindowTitle(QCoreApplication.translate("SellListDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SellListDialog", u"\u9500\u552e\u5355\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("SellListDialog", u"\u9500\u552e\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("SellListDialog", u"\u7528\u6237", None))
        self.sell_list_save_btn.setText(QCoreApplication.translate("SellListDialog", u"\u4fdd\u5b58", None))
    # retranslateUi

