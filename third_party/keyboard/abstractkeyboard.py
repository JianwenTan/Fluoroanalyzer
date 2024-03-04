"""
@Description：抽象键盘类，定义键盘按键响应事件
@Author：mysondrink@163.com
@Time：2024/1/8 15:15
"""
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class abstractkeyboard(QWidget):

    def __init__(self) -> object:
        """
        初始化界面
        构造函数
        Returns:
            object

        """
        super().__init__()
        self.m_name = ""

    def update(self) -> None:
        """
        虚函数
        Returns:

        """
        pass

    def getName(self) -> str:
        """
        获取名称
        Returns:
            str
        """
        return self.m_name

    def setName(self, name) -> None:
        """
        设置组件名称
        Args:
            name: 组件名称

        Returns:
            None
        """
        self.m_name = name

    def onKeyPressed(self, key, value) -> bool:
        """

        Args:
            key: 响应键盘按键
            value: 键盘按键的值

        Returns:

        """
        recevier = QApplication.focusWidget()
        # print(recevier)
        if recevier is None:
            return
        keyPress = QKeyEvent(QEvent.KeyPress, key, Qt.NoModifier, value)
        keyRelease = QKeyEvent(QEvent.KeyRelease, key, Qt.NoModifier,value)

        QApplication.sendEvent(recevier, keyPress)
        QApplication.sendEvent(recevier, keyRelease)

        return False