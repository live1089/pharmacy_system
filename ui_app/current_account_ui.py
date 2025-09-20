# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'current_account.ui'
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
    QLineEdit, QSizePolicy, QWidget)

class Ui_CurrentDialog(object):
    def setupUi(self, CurrentDialog):
        if not CurrentDialog.objectName():
            CurrentDialog.setObjectName(u"CurrentDialog")
        CurrentDialog.resize(498, 138)
        self.gridLayout_2 = QGridLayout(CurrentDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.current_user_lineEdit = QLineEdit(CurrentDialog)
        self.current_user_lineEdit.setObjectName(u"current_user_lineEdit")
        self.current_user_lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.current_user_lineEdit, 0, 1, 1, 1)

        self.label = QLabel(CurrentDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(CurrentDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.current_phone_lineEdit = QLineEdit(CurrentDialog)
        self.current_phone_lineEdit.setObjectName(u"current_phone_lineEdit")
        self.current_phone_lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.current_phone_lineEdit, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(CurrentDialog)

        QMetaObject.connectSlotsByName(CurrentDialog)
    # setupUi

    def retranslateUi(self, CurrentDialog):
        CurrentDialog.setWindowTitle(QCoreApplication.translate("CurrentDialog", u"\u5f53\u524d\u8d26\u53f7", None))
        self.label.setText(QCoreApplication.translate("CurrentDialog", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("CurrentDialog", u"\u624b\u673a\u53f7", None))
    # retranslateUi

