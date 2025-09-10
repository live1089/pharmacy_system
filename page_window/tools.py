from PySide6.QtCore import QObject, QEvent, Qt


def install_enter_key_filter(widget):
    """
    为控件安装回车键过滤器

    Args:
        widget: 需要安装过滤器的控件
    """

    class EnterKeyFilter(QObject):
        def eventFilter(self, obj, event):
            if event.type() == QEvent.KeyPress:
                if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                    return True
            return super().eventFilter(obj, event)

    # 为控件创建并安装过滤器
    if not hasattr(widget, '_enter_key_filter'):
        widget._enter_key_filter = EnterKeyFilter()
        widget.installEventFilter(widget._enter_key_filter)