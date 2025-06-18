# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
# from qtmodern.windows import ModernWindow
# from qtmodern.styles import dark, light
#
# app = QApplication(sys.argv)
#
# # 创建普通窗口
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("原始窗口")
#         self.setGeometry(100, 100, 300, 200)
#         btn = QPushButton("普通按钮", self)
#         btn.move(100, 80)
#
# # 转换为 Modern 风格窗口
# window = MainWindow()
# modern_window = ModernWindow(window)  # 包裹原始窗口
# modern_window.show()
#
# # 应用暗色主题
# # app.setStyleSheet(dark(app))
#
# # 亮色主题
# app.setStyleSheet(light(app))
# sys.exit(app.exec())

# from qtmodern.styles import dark, light
#
# # 暗色主题
# app.setStyleSheet(dark(app))
#
# # 亮色主题
# app.setStyleSheet(light(app))

#-------------------------------------------------------------------------------------------

import sys
from PySide6 import QtWidgets
# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
apply_stylesheet(app, theme='dark_teal.xml')

# run
window.show()
app.exec()


# import sys
#
# from PySide6.QtWidgets import QApplication
# from qframelesswindow import FramelessWindow
#
#
# class Window(FramelessWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent=parent)
#         self.setWindowTitle("PySide6-Frameless-Window")
#         self.titleBar.raise_()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Window()
#     demo.show()
#     app.exec()

# --------------------------------------------------------------------------------------------------
