# -*- coding: utf-8 -*-

from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QVBoxLayout, QWidget, QLabel, QLineEdit,
                               QDialogButtonBox, QDialog)
from PySide6.QtCore import Qt


class PopupDialog(QDialog):
    """自定义弹窗对话框"""

    def __init__(self, parent=None, title="输入数据"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(320, 188)

        # 设置布局
        layout = QVBoxLayout()

        # 添加输入框
        self.input_lineEdit = QLineEdit()
        self.input_lineEdit.setPlaceholderText("请输入内容...")
        layout.addWidget(self.input_lineEdit)

        # 添加按钮组
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    """主窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("弹窗嵌套示例")
        self.setFixedSize(400, 300)

        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 设置布局
        layout = QVBoxLayout()

        # 添加说明标签
        label = QLabel("点击下方按钮打开嵌套弹窗")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # 添加按钮
        self.btn_open = QPushButton("打开第一个弹窗")
        self.btn_open.clicked.connect(self.open_first_dialog)
        layout.addWidget(self.btn_open)

        # 添加结果显示标签
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)

        central_widget.setLayout(layout)

    def open_first_dialog(self):
        """打开第一个弹窗"""
        dialog = PopupDialog(self, "第一个弹窗")
        if dialog.exec() == QDialog.DialogCode.Accepted:
            input_text = dialog.input_lineEdit.text()
            self.result_label.setText(f"第一个弹窗输入: {input_text}")

            # 嵌套打开第二个弹窗
            self.open_second_dialog()

    def open_second_dialog(self):
        """打开第二个弹窗"""
        dialog = PopupDialog(self, "第二个弹窗(嵌套)")
        if dialog.exec() == QDialog.DialogCode.Accepted:
            input_text = dialog.input_lineEdit.text()
            current_text = self.result_label.text()
            self.result_label.setText(f"{current_text}\n第二个弹窗输入: {input_text}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()