# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_set.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(577, 307)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.old_password_lineEdit = QLineEdit(Dialog)
        self.old_password_lineEdit.setObjectName(u"old_password_lineEdit")

        self.gridLayout.addWidget(self.old_password_lineEdit, 2, 1, 1, 1)

        self.new_password_lineEdit = QLineEdit(Dialog)
        self.new_password_lineEdit.setObjectName(u"new_password_lineEdit")

        self.gridLayout.addWidget(self.new_password_lineEdit, 3, 1, 1, 1)

        self.tip_textEdit = QTextEdit(Dialog)
        self.tip_textEdit.setObjectName(u"tip_textEdit")

        self.gridLayout.addWidget(self.tip_textEdit, 4, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.user_name_lineEdit = QLineEdit(Dialog)
        self.user_name_lineEdit.setObjectName(u"user_name_lineEdit")

        self.gridLayout.addWidget(self.user_name_lineEdit, 0, 1, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.phone_number_lineEdit = QLineEdit(Dialog)
        self.phone_number_lineEdit.setObjectName(u"phone_number_lineEdit")

        self.gridLayout.addWidget(self.phone_number_lineEdit, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.user_save_btn = QPushButton(Dialog)
        self.user_save_btn.setObjectName(u"user_save_btn")

        self.gridLayout_2.addWidget(self.user_save_btn, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4fee\u6539\u8d26\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u63d0\u793a\u8bcd", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5bc6\u7801", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u65e7\u5bc6\u7801", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u624b\u673a\u53f7", None))
        self.user_save_btn.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
    # retranslateUi

