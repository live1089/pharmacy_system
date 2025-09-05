# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shelves_drug.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_ShelvesDialog(object):
    def setupUi(self, ShelvesDialog):
        if not ShelvesDialog.objectName():
            ShelvesDialog.setObjectName(u"ShelvesDialog")
        ShelvesDialog.resize(441, 192)
        self.gridLayout_2 = QGridLayout(ShelvesDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.stock_out_list_combox = QComboBox(ShelvesDialog)
        self.stock_out_list_combox.setObjectName(u"stock_out_list_combox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_out_list_combox.sizePolicy().hasHeightForWidth())
        self.stock_out_list_combox.setSizePolicy(sizePolicy)
        self.stock_out_list_combox.setMinimumSize(QSize(350, 0))
        self.stock_out_list_combox.setEditable(True)

        self.gridLayout.addWidget(self.stock_out_list_combox, 0, 1, 1, 1)

        self.shelves_drug_combox = QComboBox(ShelvesDialog)
        self.shelves_drug_combox.setObjectName(u"shelves_drug_combox")
        self.shelves_drug_combox.setEditable(True)

        self.gridLayout.addWidget(self.shelves_drug_combox, 2, 1, 1, 1)

        self.label_2 = QLabel(ShelvesDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.shelves_number_spinBox = QSpinBox(ShelvesDialog)
        self.shelves_number_spinBox.setObjectName(u"shelves_number_spinBox")
        self.shelves_number_spinBox.setMinimum(1)
        self.shelves_number_spinBox.setMaximum(999999999)

        self.gridLayout.addWidget(self.shelves_number_spinBox, 3, 1, 1, 1)

        self.label_4 = QLabel(ShelvesDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label = QLabel(ShelvesDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(ShelvesDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.stock_out_batch_combox = QComboBox(ShelvesDialog)
        self.stock_out_batch_combox.setObjectName(u"stock_out_batch_combox")
        self.stock_out_batch_combox.setEditable(True)

        self.gridLayout.addWidget(self.stock_out_batch_combox, 1, 1, 1, 1)

        self.label_5 = QLabel(ShelvesDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.shelves_location_combox = QComboBox(ShelvesDialog)
        self.shelves_location_combox.setObjectName(u"shelves_location_combox")
        self.shelves_location_combox.setEditable(True)

        self.gridLayout.addWidget(self.shelves_location_combox, 4, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.shelves_add_save_btn = QPushButton(ShelvesDialog)
        self.shelves_add_save_btn.setObjectName(u"shelves_add_save_btn")

        self.gridLayout_2.addWidget(self.shelves_add_save_btn, 2, 0, 1, 1)


        self.retranslateUi(ShelvesDialog)

        QMetaObject.connectSlotsByName(ShelvesDialog)
    # setupUi

    def retranslateUi(self, ShelvesDialog):
        ShelvesDialog.setWindowTitle(QCoreApplication.translate("ShelvesDialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("ShelvesDialog", u"\u4e0a\u67b6\u836f\u54c1", None))
        self.label_4.setText(QCoreApplication.translate("ShelvesDialog", u"\u51fa\u5e93\u6279\u6b21", None))
        self.label.setText(QCoreApplication.translate("ShelvesDialog", u"\u51fa\u5e93\u5355", None))
        self.label_3.setText(QCoreApplication.translate("ShelvesDialog", u"\u4e0a\u67b6\u6570\u91cf", None))
        self.label_5.setText(QCoreApplication.translate("ShelvesDialog", u"\u4e0a\u67b6\u4f4d\u7f6e", None))
        self.shelves_add_save_btn.setText(QCoreApplication.translate("ShelvesDialog", u"\u4fdd\u5b58", None))
    # retranslateUi

