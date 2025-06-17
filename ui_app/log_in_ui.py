# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_in.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModality.NonModal)
        Form.setEnabled(True)
        Form.resize(547, 309)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(172, 125))
        Form.setTabletTracking(False)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 12, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 7, 0, 1, 1)

        self.password_le = QLineEdit(Form)
        self.password_le.setObjectName(u"password_le")
        self.password_le.setMaximumSize(QSize(16777215, 16777215))
        self.password_le.setMaxLength(8)
        self.password_le.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_le.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.password_le, 7, 3, 1, 1)

        self.password_lb = QLabel(Form)
        self.password_lb.setObjectName(u"password_lb")
        self.password_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.password_lb, 7, 1, 1, 1)

        self.account_le = QLineEdit(Form)
        self.account_le.setObjectName(u"account_le")
        self.account_le.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.account_le.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.account_le.setMaxLength(16)
        self.account_le.setDragEnabled(False)
        self.account_le.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.account_le.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.account_le, 1, 3, 1, 1)

        self.log_on_btn = QPushButton(Form)
        self.log_on_btn.setObjectName(u"log_on_btn")

        self.gridLayout.addWidget(self.log_on_btn, 10, 3, 1, 1)

        self.account_lb = QLabel(Form)
        self.account_lb.setObjectName(u"account_lb")
        self.account_lb.setMinimumSize(QSize(0, 3))
        self.account_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.account_lb, 1, 1, 1, 1)

        self.tiplb = QLabel(Form)
        self.tiplb.setObjectName(u"tiplb")
        self.tiplb.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.tiplb.setTextFormat(Qt.TextFormat.PlainText)
        self.tiplb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tiplb.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout.addWidget(self.tiplb, 11, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u836f\u623f\u7cfb\u7edf\u767b\u5f55", None))
        self.password_le.setPlaceholderText(QCoreApplication.translate("Form", u"8\u4f4d\u5bc6\u7801\uff0c\u5305\u542b\u82f1\u6587\u4e0e\u6570\u5b57", None))
        self.password_lb.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.account_le.setInputMask("")
        self.account_le.setText("")
        self.account_le.setPlaceholderText(QCoreApplication.translate("Form", u"\u624b\u673a\u53f7\u6216\u90ae\u7bb1", None))
        self.log_on_btn.setText(QCoreApplication.translate("Form", u"\u767b\u5f55\u8d26\u53f7", None))
        self.account_lb.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7", None))
        self.tiplb.setText("")
    # retranslateUi

