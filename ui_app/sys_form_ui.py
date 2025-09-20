# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sys_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_SysDialog(object):
    def setupUi(self, SysDialog):
        if not SysDialog.objectName():
            SysDialog.setObjectName(u"SysDialog")
        SysDialog.resize(479, 172)
        self.gridLayout_2 = QGridLayout(SysDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.back_data_btn = QPushButton(SysDialog)
        self.back_data_btn.setObjectName(u"back_data_btn")

        self.gridLayout.addWidget(self.back_data_btn, 1, 0, 1, 1)

        self.system_formatting_btn = QPushButton(SysDialog)
        self.system_formatting_btn.setObjectName(u"system_formatting_btn")

        self.gridLayout.addWidget(self.system_formatting_btn, 0, 0, 1, 1)

        self.action_restore_btn = QPushButton(SysDialog)
        self.action_restore_btn.setObjectName(u"action_restore_btn")

        self.gridLayout.addWidget(self.action_restore_btn, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.action_auto_backup_btn = QPushButton(SysDialog)
        self.action_auto_backup_btn.setObjectName(u"action_auto_backup_btn")

        self.gridLayout_2.addWidget(self.action_auto_backup_btn, 1, 0, 1, 1)


        self.retranslateUi(SysDialog)

        QMetaObject.connectSlotsByName(SysDialog)
    # setupUi

    def retranslateUi(self, SysDialog):
        SysDialog.setWindowTitle(QCoreApplication.translate("SysDialog", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.back_data_btn.setText(QCoreApplication.translate("SysDialog", u"\u5907\u4efd\u6570\u636e", None))
        self.system_formatting_btn.setText(QCoreApplication.translate("SysDialog", u"\u6062\u590d\u51fa\u5382\u8bbe\u7f6e", None))
        self.action_restore_btn.setText(QCoreApplication.translate("SysDialog", u"\u6062\u590d\u6570\u636e", None))
        self.action_auto_backup_btn.setText(QCoreApplication.translate("SysDialog", u"\u81ea\u52a8\u5907\u4efd", None))
    # retranslateUi

