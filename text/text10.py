# import sys
# from PySide6.QtWidgets import (
#     QApplication, QMainWindow, QStackedWidget,
#     QPushButton, QLabel, QVBoxLayout, QWidget,
#     QLineEdit, QComboBox
# )
# from PySide6.QtCore import Qt
# from enum import Enum
#
#
# class PageName(Enum):
#     """页面名称枚举，避免拼写错误"""
#     HOME = "home"
#     PROFILE = "profile"
#     SETTINGS = "settings"
#     HELP = "help"
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("使用名称切换StackedWidget")
#         self.resize(600, 400)
#
#         # 创建页面字典和堆叠控件
#         self.pages = {}
#         self.stacked_widget = QStackedWidget()
#
#         # 创建所有页面
#         self.create_home_page()
#         self.create_profile_page()
#         self.create_settings_page()
#         self.create_help_page()
#
#         # 创建导航控件
#         self.create_navigation()
#
#         # 主布局
#         main_layout = QVBoxLayout()
#         main_layout.addLayout(self.nav_layout)
#         main_layout.addWidget(self.stacked_widget)
#
#         container = QWidget()
#         container.setLayout(main_layout)
#         self.setCentralWidget(container)
#
#         # 默认显示首页
#         self.show_page_by_name(PageName.HOME.value)
#
#     def create_navigation(self):
#         """创建导航栏"""
#         self.nav_layout = QVBoxLayout()
#
#         # 创建页面选择下拉框
#         self.page_selector = QComboBox()
#         self.page_selector.addItem("首页", PageName.HOME.value)
#         self.page_selector.addItem("个人资料", PageName.PROFILE.value)
#         self.page_selector.addItem("设置", PageName.SETTINGS.value)
#         self.page_selector.addItem("帮助", PageName.HELP.value)
#         self.page_selector.currentIndexChanged.connect(
#             lambda index: self.show_page_by_name(self.page_selector.itemData(index)))
#
#         # 直接跳转按钮
#         buttons_layout = QVBoxLayout()
#         buttons_layout.addWidget(self.create_nav_button("首页", PageName.HOME.value))
#         buttons_layout.addWidget(self.create_nav_button("个人资料", PageName.PROFILE.value))
#         buttons_layout.addWidget(self.create_nav_button("设置", PageName.SETTINGS.value))
#         buttons_layout.addWidget(self.create_nav_button("帮助", PageName.HELP.value))
#
#         # 添加组件到导航布局
#         self.nav_layout.addWidget(QLabel("选择页面:"))
#         self.nav_layout.addWidget(self.page_selector)
#         self.nav_layout.addSpacing(20)
#         self.nav_layout.addWidget(QLabel("快速导航:"))
#         self.nav_layout.addLayout(buttons_layout)
#
#     def create_nav_button(self, text, page_name):
#         """创建导航按钮"""
#         button = QPushButton(text)
#         button.setMinimumHeight(40)
#         button.clicked.connect(lambda: self.show_page_by_name(page_name))
#         return button
#
#     def create_page(self, title, color, page_name):
#         """创建基本页面模板"""
#         page = QWidget()
#         layout = QVBoxLayout(page)
#
#         # 标题
#         title_label = QLabel(title)
#         title_label.setAlignment(Qt.AlignCenter)
#         title_label.setStyleSheet(f"font-size: 24px; color: white;")
#         layout.addWidget(title_label)
#
#         # 状态显示
#         status_label = QLabel(f"当前页面: {page_name}")
#         status_label.setStyleSheet("font-size: 14px; color: white;")
#         layout.addWidget(status_label)
#
#         # 设置背景色
#         page.setStyleSheet(f"background-color: {color};")
#
#         # 添加到堆叠控件和页面字典
#         self.stacked_widget.addWidget(page)
#         self.pages[page_name] = page
#
#         return page
#
#     def create_home_page(self):
#         """创建首页"""
#         page = self.create_page("欢迎来到首页", "#3498db", PageName.HOME.value)
#         layout = page.layout()
#
#         # 添加首页特有内容
#         welcome_label = QLabel("这是应用程序的主页面")
#         welcome_label.setStyleSheet("font-size: 18px; color: white;")
#         welcome_label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(welcome_label)
#
#         tip_label = QLabel("尝试使用导航栏切换到其他页面")
#         tip_label.setStyleSheet("font-size: 16px; color: #f1c40f;")
#         tip_label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(tip_label)
#
#     def create_profile_page(self):
#         """创建个人资料页"""
#         page = self.create_page("个人资料", "#2ecc71", PageName.PROFILE.value)
#         layout = page.layout()
#
#         # 表单布局
#         form_layout = QVBoxLayout()
#         form_layout.setContentsMargins(50, 30, 50, 30)
#
#         form_layout.addWidget(QLabel("姓名:"))
#         form_layout.addWidget(QLineEdit())
#
#         form_layout.addWidget(QLabel("邮箱:"))
#         form_layout.addWidget(QLineEdit())
#
#         form_layout.addWidget(QLabel("电话:"))
#         form_layout.addWidget(QLineEdit())
#
#         layout.addLayout(form_layout)
#
#         # 保存按钮
#         save_btn = QPushButton("保存资料")
#         save_btn.setStyleSheet("background-color: #27ae60; color: white; padding: 10px;")
#         layout.addWidget(save_btn)
#
#     def create_settings_page(self):
#         """创建设置页"""
#         page = self.create_page("系统设置", "#9b59b6", PageName.SETTINGS.value)
#         layout = page.layout()
#
#         # 设置选项
#         settings_layout = QVBoxLayout()
#         settings_layout.setContentsMargins(50, 30, 50, 30)
#
#         settings_layout.addWidget(QLabel("主题:"))
#         theme_combo = QComboBox()
#         theme_combo.addItems(["浅色模式", "深色模式", "自动"])
#         settings_layout.addWidget(theme_combo)
#
#         settings_layout.addWidget(QLabel("语言:"))
#         lang_combo = QComboBox()
#         lang_combo.addItems(["中文", "英文", "日文"])
#         settings_layout.addWidget(lang_combo)
#
#         layout.addLayout(settings_layout)
#
#         # 应用按钮
#         apply_btn = QPushButton("应用设置")
#         apply_btn.setStyleSheet("background-color: #8e44ad; color: white; padding: 10px;")
#         layout.addWidget(apply_btn)
#
#     def create_help_page(self):
#         """创建帮助页"""
#         page = self.create_page("帮助中心", "#e74c3c", PageName.HELP.value)
#         layout = page.layout()
#
#         # 帮助内容
#         help_text = QLabel(
#             "<h2>常见问题解答</h2>"
#             "<p><b>Q: 如何切换页面？</b><br>"
#             "A: 使用导航栏中的下拉菜单或按钮。</p>"
#             "<p><b>Q: 如何保存设置？</b><br>"
#             "A: 在设置页面进行修改后点击'应用设置'按钮。</p>"
#             "<p><b>Q: 技术支持联系方式？</b><br>"
#             "A: support@example.com</p>"
#         )
#         help_text.setStyleSheet("color: white; background: rgba(0,0,0,0.2); padding: 20px; border-radius: 10px;")
#         help_text.setWordWrap(True)
#         layout.addWidget(help_text)
#
#     def show_page_by_name(self, page_name):
#         """通过页面名称切换页面"""
#         if page_name in self.pages:
#             # 更新下拉框选中项
#             index = self.page_selector.findData(page_name)
#             if index >= 0:
#                 self.page_selector.setCurrentIndex(index)
#
#             # 切换到目标页面
#             self.stacked_widget.setCurrentWidget(self.pages[page_name])
#
#             # 这里可以添加页面切换时的额外逻辑
#             print(f"已切换到页面: {page_name}")
#         else:
#             print(f"错误: 找不到页面 '{page_name}'")
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     # 设置应用样式
#     app.setStyleSheet("""
#         QMainWindow {
#             background-color: #2c3e50;
#         }
#         QWidget {
#             font-family: 'Microsoft YaHei';
#         }
#         QPushButton {
#             background-color: #34495e;
#             color: white;
#             border-radius: 5px;
#             padding: 8px 16px;
#             font-size: 14px;
#         }
#         QPushButton:hover {
#             background-color: #3d566e;
#         }
#         QComboBox {
#             padding: 5px;
#             background: white;
#             border: 1px solid #bdc3c7;
#             border-radius: 4px;
#         }
#         QLabel {
#             color: #ecf0f1;
#         }
#     """)
#
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())



from PySide6.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel

app = QApplication([])

# 创建一个 QStackedWidget
stacked_widget = QStackedWidget()

# 创建多个页面，并为每个页面设置一个唯一的名称
page1 = QWidget()
page1.setObjectName("Page1")  # 设置页面名称
label1 = QLabel("This is Page 1")
layout1 = QVBoxLayout(page1)
layout1.addWidget(label1)

page2 = QWidget()
page2.setObjectName("Page2")  # 设置页面名称
label2 = QLabel("This is Page 2")
layout2 = QVBoxLayout(page2)
layout2.addWidget(label2)

page3 = QWidget()
page3.setObjectName("Page3")  # 设置页面名称
label3 = QLabel("This is Page 3")
layout3 = QVBoxLayout(page3)
layout3.addWidget(label3)

# 将页面添加到 QStackedWidget
stacked_widget.addWidget(page1)
stacked_widget.addWidget(page2)
stacked_widget.addWidget(page3)

# 创建一个名称到索引的映射
page_mapping = {
    "Page1": 0,
    "Page2": 1,
    "Page3": 2
}

# 创建一个按钮，点击后切换到指定页面
def switch_page(page_name):
    index = page_mapping.get(page_name)
    if index is not None:
        stacked_widget.setCurrentIndex(index)

button1 = QPushButton("Go to Page 1")
button1.clicked.connect(lambda: switch_page("Page1"))

button2 = QPushButton("Go to Page 2")
button2.clicked.connect(lambda: switch_page("Page2"))

button3 = QPushButton("Go to Page 3")
button3.clicked.connect(lambda: switch_page("Page3"))

# 布局
layout = QVBoxLayout()
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(stacked_widget)

main_widget = QWidget()
main_widget.setLayout(layout)
main_widget.show()

app.exec()
