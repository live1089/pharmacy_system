# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory_count_entry.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateTimeEdit,
    QDialog, QDialogButtonBox, QGridLayout, QLabel,
    QPlainTextEdit, QSizePolicy, QSpinBox, QWidget)

class Ui_InventoryCountDialog(object):
    def setupUi(self, InventoryCountDialog):
        if not InventoryCountDialog.objectName():
            InventoryCountDialog.setObjectName(u"InventoryCountDialog")
        InventoryCountDialog.resize(522, 215)
        self.gridLayout_2 = QGridLayout(InventoryCountDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.inventory_count_number_suspinBox = QSpinBox(InventoryCountDialog)
        self.inventory_count_number_suspinBox.setObjectName(u"inventory_count_number_suspinBox")
        self.inventory_count_number_suspinBox.setMaximum(999999999)

        self.gridLayout.addWidget(self.inventory_count_number_suspinBox, 0, 3, 1, 1)

        self.inventory_count_drug_comboBox = QComboBox(InventoryCountDialog)
        self.inventory_count_drug_comboBox.setObjectName(u"inventory_count_drug_comboBox")

        self.gridLayout.addWidget(self.inventory_count_drug_comboBox, 0, 1, 1, 1)

        self.label = QLabel(InventoryCountDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(InventoryCountDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_6 = QLabel(InventoryCountDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.actual_quantity_lab = QLabel(InventoryCountDialog)
        self.actual_quantity_lab.setObjectName(u"actual_quantity_lab")
        self.actual_quantity_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.actual_quantity_lab, 1, 3, 1, 1)

        self.label_2 = QLabel(InventoryCountDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.inventory_count_user_comboBox = QComboBox(InventoryCountDialog)
        self.inventory_count_user_comboBox.setObjectName(u"inventory_count_user_comboBox")

        self.gridLayout.addWidget(self.inventory_count_user_comboBox, 1, 1, 1, 1)

        self.label_4 = QLabel(InventoryCountDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.inventory_count_dateTimeEdit = QDateTimeEdit(InventoryCountDialog)
        self.inventory_count_dateTimeEdit.setObjectName(u"inventory_count_dateTimeEdit")

        self.gridLayout.addWidget(self.inventory_count_dateTimeEdit, 2, 1, 1, 1)

        self.label_5 = QLabel(InventoryCountDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.inventory_count_plainTextEdit = QPlainTextEdit(InventoryCountDialog)
        self.inventory_count_plainTextEdit.setObjectName(u"inventory_count_plainTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inventory_count_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.inventory_count_plainTextEdit.setSizePolicy(sizePolicy)
        self.inventory_count_plainTextEdit.setMinimumSize(QSize(100, 0))
        self.inventory_count_plainTextEdit.setMaximumSize(QSize(16777215, 60))

        self.gridLayout.addWidget(self.inventory_count_plainTextEdit, 2, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(InventoryCountDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(InventoryCountDialog)
        self.buttonBox.accepted.connect(InventoryCountDialog.accept)
        self.buttonBox.rejected.connect(InventoryCountDialog.reject)

        QMetaObject.connectSlotsByName(InventoryCountDialog)
    # setupUi

    def retranslateUi(self, InventoryCountDialog):
        InventoryCountDialog.setWindowTitle(QCoreApplication.translate("InventoryCountDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("InventoryCountDialog", u"\u76d8\u70b9\u836f\u54c1", None))
        self.label_3.setText(QCoreApplication.translate("InventoryCountDialog", u"\u76d8\u70b9\u6570\u91cf", None))
        self.label_6.setText(QCoreApplication.translate("InventoryCountDialog", u"\u5b9e\u9645\u6570\u91cf", None))
        self.actual_quantity_lab.setText("")
        self.label_2.setText(QCoreApplication.translate("InventoryCountDialog", u"\u76d8\u70b9\u4eba", None))
        self.label_4.setText(QCoreApplication.translate("InventoryCountDialog", u"\u76d8\u70b9\u65e5\u671f", None))
        self.label_5.setText(QCoreApplication.translate("InventoryCountDialog", u"\u76d8\u70b9\u7ed3\u679c", None))
    # retranslateUi

