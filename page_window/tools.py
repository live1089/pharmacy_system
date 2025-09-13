from PySide6.QtCore import QObject, QEvent, Qt, QDateTime


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



def safe_set_datetime(datetime_edit, value, format_str="yyyy-MM-dd hh:mm:ss"):
    """
    安全地设置 QDateTimeEdit 的时间值
    :param datetime_edit: QDateTimeEdit 控件
    :param value: 时间值（可以是字符串或 QDateTime）
    :param format_str: 字符串时间的格式
    """
    if isinstance(value, str):
        dt = QDateTime.fromString(value, format_str)
        if dt.isValid():
            datetime_edit.setDateTime(dt)
        else:
            datetime_edit.setDateTime(QDateTime.currentDateTime())
    elif isinstance(value, QDateTime):
        datetime_edit.setDateTime(value)
    else:
        datetime_edit.setDateTime(QDateTime.currentDateTime())
