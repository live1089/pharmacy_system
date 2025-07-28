# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drug_attribute.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_class_dialog(object):
    def setupUi(self, class_dialog):
        if not class_dialog.objectName():
            class_dialog.setObjectName(u"class_dialog")
        class_dialog.resize(478, 412)
        self.gridLayout_2 = QGridLayout(class_dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.refresh_btn = QPushButton(class_dialog)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.verticalLayout.addWidget(self.refresh_btn)

        self.add_btn = QPushButton(class_dialog)
        self.add_btn.setObjectName(u"add_btn")

        self.verticalLayout.addWidget(self.add_btn)

        self.del_btn = QPushButton(class_dialog)
        self.del_btn.setObjectName(u"del_btn")

        self.verticalLayout.addWidget(self.del_btn)

        self.modify_btn = QPushButton(class_dialog)
        self.modify_btn.setObjectName(u"modify_btn")

        self.verticalLayout.addWidget(self.modify_btn)

        self.verticalSpacer = QSpacerItem(20, 270, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.class_set_tableView = QTableView(class_dialog)
        self.class_set_tableView.setObjectName(u"class_set_tableView")

        self.gridLayout_2.addWidget(self.class_set_tableView, 0, 0, 1, 1)


        self.retranslateUi(class_dialog)

        QMetaObject.connectSlotsByName(class_dialog)
    # setupUi

    def retranslateUi(self, class_dialog):
        class_dialog.setWindowTitle(QCoreApplication.translate("class_dialog", u"\u836f\u54c1\u5c5e\u6027\u8bbe\u7f6e", None))
        self.refresh_btn.setText(QCoreApplication.translate("class_dialog", u"\u5237\u65b0", None))
        self.add_btn.setText(QCoreApplication.translate("class_dialog", u"\u6dfb\u52a0", None))
        self.del_btn.setText(QCoreApplication.translate("class_dialog", u"\u5220\u9664", None))
        self.modify_btn.setText(QCoreApplication.translate("class_dialog", u"\u4fee\u6539", None))
    # retranslateUi

