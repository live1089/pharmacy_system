import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from qt_material import apply_stylesheet
from qt_material import list_themes
app = QApplication(sys.argv)

# 应用Material主题 (dark_teal是内置主题名之一)
apply_stylesheet(app, theme='dark_teal.xml')

list_themes()
# 创建简单界面
window = QWidget()
layout = QVBoxLayout()
button = QPushButton('Material 按钮')
layout.addWidget(button)
window.setLayout(layout)
window.show()

sys.exit(app.exec())

# ['dark_amber.xml',
#  'dark_blue.xml',
#  'dark_cyan.xml',
#  'dark_lightgreen.xml',
#  'dark_pink.xml',
#  'dark_purple.xml',
#  'dark_red.xml',
#  'dark_teal.xml',
#  'dark_yellow.xml',
#  'light_amber.xml',
#  'light_blue.xml',
#  'light_cyan.xml',
#  'light_cyan_500.xml',
#  'light_lightgreen.xml',
#  'light_pink.xml',
#  'light_purple.xml',
#  'light_red.xml',
#  'light_teal.xml',
#  'light_yellow.xml']