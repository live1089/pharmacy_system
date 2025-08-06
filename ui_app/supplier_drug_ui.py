# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supplier_drug.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDialog, QGridLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_SupDialog(object):
    def setupUi(self, SupDialog):
        if not SupDialog.objectName():
            SupDialog.setObjectName(u"SupDialog")
        SupDialog.resize(766, 315)
        self.gridLayout_2 = QGridLayout(SupDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 3, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 3, 5, 1, 1)

        self.updater_line_edit = QLineEdit(SupDialog)
        self.updater_line_edit.setObjectName(u"updater_line_edit")

        self.gridLayout.addWidget(self.updater_line_edit, 2, 5, 1, 1)

        self.contact_line_edit = QLineEdit(SupDialog)
        self.contact_line_edit.setObjectName(u"contact_line_edit")

        self.gridLayout.addWidget(self.contact_line_edit, 2, 2, 1, 1)

        self.update_time = QDateTimeEdit(SupDialog)
        self.update_time.setObjectName(u"update_time")

        self.gridLayout.addWidget(self.update_time, 0, 5, 1, 1)

        self.label_3 = QLabel(SupDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_9 = QLabel(SupDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.label_5 = QLabel(SupDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)

        self.label = QLabel(SupDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_12 = QLabel(SupDialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 6, 3, 1, 1)

        self.email_line_edit = QLineEdit(SupDialog)
        self.email_line_edit.setObjectName(u"email_line_edit")

        self.gridLayout.addWidget(self.email_line_edit, 8, 2, 1, 1)

        self.label_6 = QLabel(SupDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_7 = QLabel(SupDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.creator_line_edit = QLineEdit(SupDialog)
        self.creator_line_edit.setObjectName(u"creator_line_edit")

        self.gridLayout.addWidget(self.creator_line_edit, 6, 5, 1, 1)

        self.create_time = QDateTimeEdit(SupDialog)
        self.create_time.setObjectName(u"create_time")

        self.gridLayout.addWidget(self.create_time, 4, 5, 1, 1)

        self.plainTextEdit_remark = QPlainTextEdit(SupDialog)
        self.plainTextEdit_remark.setObjectName(u"plainTextEdit_remark")

        self.gridLayout.addWidget(self.plainTextEdit_remark, 0, 7, 9, 1)

        self.label_10 = QLabel(SupDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 1)

        self.supplier_line_edit = QLineEdit(SupDialog)
        self.supplier_line_edit.setObjectName(u"supplier_line_edit")

        self.gridLayout.addWidget(self.supplier_line_edit, 0, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 5, 1, 1)

        self.address_line_edit = QLineEdit(SupDialog)
        self.address_line_edit.setObjectName(u"address_line_edit")

        self.gridLayout.addWidget(self.address_line_edit, 6, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 5, 5, 1, 1)

        self.label_2 = QLabel(SupDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.phone_line_edit = QLineEdit(SupDialog)
        self.phone_line_edit.setObjectName(u"phone_line_edit")

        self.gridLayout.addWidget(self.phone_line_edit, 4, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 7, 5, 1, 1)

        self.label_4 = QLabel(SupDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 4, 6, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.supplier_save_btn = QPushButton(SupDialog)
        self.supplier_save_btn.setObjectName(u"supplier_save_btn")

        self.gridLayout_2.addWidget(self.supplier_save_btn, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 23, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(47, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(47, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 4, 1, 1, 1)


        self.retranslateUi(SupDialog)

        QMetaObject.connectSlotsByName(SupDialog)
    # setupUi

    def retranslateUi(self, SupDialog):
        SupDialog.setWindowTitle(QCoreApplication.translate("SupDialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("SupDialog", u"\u8054\u7cfb\u7535\u8bdd", None))
        self.label_9.setText(QCoreApplication.translate("SupDialog", u"\u90ae\u7bb1", None))
        self.label_5.setText(QCoreApplication.translate("SupDialog", u"\u66f4\u65b0\u4eba", None))
        self.label.setText(QCoreApplication.translate("SupDialog", u"\u4f9b\u5e94\u5546", None))
        self.label_12.setText(QCoreApplication.translate("SupDialog", u"\u521b\u5efa\u4eba", None))
        self.label_6.setText(QCoreApplication.translate("SupDialog", u"\u66f4\u65b0\u65f6\u95f4", None))
        self.label_7.setText(QCoreApplication.translate("SupDialog", u"\u5730\u5740", None))
        self.label_10.setText(QCoreApplication.translate("SupDialog", u"\u521b\u5efa\u65f6\u95f4", None))
        self.label_2.setText(QCoreApplication.translate("SupDialog", u"\u8054\u7cfb\u4eba", None))
        self.label_4.setText(QCoreApplication.translate("SupDialog", u"\u5907\u6ce8", None))
        self.supplier_save_btn.setText(QCoreApplication.translate("SupDialog", u"\u4fdd\u5b58", None))
    # retranslateUi

