"""
@Description：键盘按键组件类
@Author：mysondrink@163.com
@Time：2024/1/8 15:31
"""
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

DEFAULT_STYLE_SHEET = "QPushButton { background: #4395ff; border-radius: 5px;" \
                      "margin: 5px;font-size: 26px; color:white;}" \
                      "QPushButton:pressed { background: #01ddfd}"


class keybutton(QPushButton):
    pressed = Signal(str)

    def __init__(self, value) -> object:
        """
        构造函数
        初始化按钮
        Args:
            value:

        Returns:
            object: 键盘按钮类
        """
        super().__init__()
        self.setFocusPolicy(Qt.NoFocus)
        self.setStyleSheet(DEFAULT_STYLE_SHEET)
        self.enum = {"Auto": 0, "LowerCase": 1, "UpperCase": 2, "SpecialChar": 3}

        self.key = 0
        self.value = value
        self.display = ""

    def mousePressEvent(self, event) -> None:
        """
        鼠标点击事件响应重写，获取点击事件
        Args:
            event: 点击事件

        Returns:
            None
        """
        if event.button() == Qt.LeftButton:
            self.pressed.emit(self.value)
        super().mousePressEvent(event)

    def setValue(self, value) -> None:
        """
        设置键盘按键的值
        Args:
            value: 键盘按键的值

        Returns:
            None
        """
        self.value = value

    def onReponse(self) -> None:
        """
        虚函数
        Returns:
            None
        """
        pass

    def swtichCapsLock(self) -> None:
        """
        虚函数
        Returns:
            None
        """
        pass

    def switchSpecialChar(self) -> None:
        """
        虚函数
        Returns:
            None
        """
        pass

    def switching(self) -> None:
        """
        虚函数
        Returns:
            None
        """
        pass

    def findEnum(self) -> None:
        """
        虚函数
        Returns:
            None
        """
        pass

    def setDisplayContent(self) -> None:
        """
        虚函数
        Returns:
            None
        """
        pass