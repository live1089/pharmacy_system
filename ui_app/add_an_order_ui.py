# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_an_order.ui'
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
    QDoubleSpinBox, QGridLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_AnOrderDialog(object):
    def setupUi(self, AnOrderDialog):
        if not AnOrderDialog.objectName():
            AnOrderDialog.setObjectName(u"AnOrderDialog")
        AnOrderDialog.resize(569, 197)
        self.gridLayout_2 = QGridLayout(AnOrderDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(AnOrderDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(AnOrderDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)

        self.label = QLabel(AnOrderDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(AnOrderDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.supplier_order_comboBox = QComboBox(AnOrderDialog)
        self.supplier_order_comboBox.setObjectName(u"supplier_order_comboBox")
        self.supplier_order_comboBox.setEditable(True)

        self.gridLayout.addWidget(self.supplier_order_comboBox, 1, 1, 1, 1)

        self.label_5 = QLabel(AnOrderDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(AnOrderDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(AnOrderDialog)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMaximum(999999999.990000009536743)

        self.gridLayout.addWidget(self.doubleSpinBox, 2, 1, 1, 1)

        self.label_3 = QLabel(AnOrderDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.down_order_dateEdit = QDateEdit(AnOrderDialog)
        self.down_order_dateEdit.setObjectName(u"down_order_dateEdit")

        self.gridLayout.addWidget(self.down_order_dateEdit, 0, 4, 1, 1)

        self.up_googs_dateEdit = QDateEdit(AnOrderDialog)
        self.up_googs_dateEdit.setObjectName(u"up_googs_dateEdit")

        self.gridLayout.addWidget(self.up_googs_dateEdit, 1, 4, 1, 1)

        self.plainTextEdit = QPlainTextEdit(AnOrderDialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(190, 16777215))

        self.gridLayout.addWidget(self.plainTextEdit, 2, 4, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.order_save_btn = QPushButton(AnOrderDialog)
        self.order_save_btn.setObjectName(u"order_save_btn")

        self.gridLayout_2.addWidget(self.order_save_btn, 2, 0, 1, 1)


        self.retranslateUi(AnOrderDialog)

        QMetaObject.connectSlotsByName(AnOrderDialog)
    # setupUi

    def retranslateUi(self, AnOrderDialog):
        AnOrderDialog.setWindowTitle(QCoreApplication.translate("AnOrderDialog", u"\u6dfb\u52a0\u8ba2\u5355", None))
        self.label_4.setText(QCoreApplication.translate("AnOrderDialog", u"\u4ea4\u8d27\u65e5\u671f", None))
        self.label.setText(QCoreApplication.translate("AnOrderDialog", u"\u8ba2\u5355\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("AnOrderDialog", u"\u4f9b\u5e94\u5546", None))
        self.label_5.setText(QCoreApplication.translate("AnOrderDialog", u"\u91c7\u8d2d\u603b\u4ef7", None))
        self.label_6.setText(QCoreApplication.translate("AnOrderDialog", u"\u5907\u6ce8", None))
        self.label_3.setText(QCoreApplication.translate("AnOrderDialog", u"\u4e0b\u5355\u65e5\u671f", None))
        self.order_save_btn.setText(QCoreApplication.translate("AnOrderDialog", u"\u4fdd\u5b58", None))
    # retranslateUi

