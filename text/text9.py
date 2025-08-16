import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget,
    QPushButton, QLabel, QVBoxLayout, QWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StackedWidget 示例")
        self.resize(400, 300)



        # 创建堆叠部件
        self.stacked_widget = QStackedWidget()

        # 创建三个页面
        self.page1 = self.create_page("页面 1", "red")
        self.page2 = self.create_page("页面 2", "green")
        self.page3 = self.create_page("页面 3", "blue")

        # 添加页面到堆叠部件
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        # 在初始化时创建页面字典
        self.pages = {
            "home": self.page1,
            "settings": self.page2,
            "about": self.page3
        }

        # 创建切换按钮
        btn1 = QPushButton("显示页面 1")
        btn2 = QPushButton("显示页面 2")
        btn3 = QPushButton("显示页面 3")

        # 连接按钮信号
        btn1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        btn2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        btn3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page3))
        self.stacked_widget.currentChanged.connect(self.handle_page_change)



        # 主布局
        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(self.stacked_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        # 使用示例
        self.show_page("settings")

    def create_page(self, text, color):
        """创建带背景色的页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel(text)
        label.setStyleSheet(f"font-size: 24px; color: white;")
        layout.addWidget(label)
        page.setStyleSheet(f"background-color: {color};")
        return page

    def handle_page_change(self, index):
        print(f"切换到页面: {index}")



    # 通过名称切换
    def show_page(self, page_name):
        widget = self.pages.get(page_name)
        if widget:
            self.stacked_widget.setCurrentWidget(widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())