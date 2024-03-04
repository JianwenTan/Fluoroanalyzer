"""
@Description：抽象widget类
@Author：mysondrink@163.com
@Time：2024/1/8 16:36
"""
import sys
import traceback

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
try:
    from controller.LogController import LogThread
except ModuleNotFoundError:
    from qt0223.controller.LogController import LogThread


class AbstractWidget(QWidget):
    update_log = Signal(str)
    update_json = Signal(dict)
    next_page = Signal(str)
    update_info = Signal(str)

    def __init__(self):
        """
        构造函数，初始化日志类
        """
        super().__init__()
        self.logThread = LogThread()
        self.logThread.start()
        self.update_log.connect(self.logThread.getLogMsg)
        self.logThread.error_info.connect(self.showErrorDialog) # 捕获线程或其他非界面类的错误
        sys.excepthook = self.HandleException

    def __del__(self):
        """
        析构函数，打印类名
        """
        print(f"delete widget{self.__class__.__name__}")

    def deleteLater(self) -> None:
        """
        打印删除的类的名
        Returns:
            None
        """
        super().deleteLater()
        print(f"delete widget{self.__class__.__name__}")

    def HandleException(self, excType, excValue, tb) -> None:
        """
        捕获和输出异常类
        Args:
            excType: 异常类型
            excValue: 异常对象
            tb: 异常的trace back

        Returns:
            None
        """
        sys.__excepthook__(excType, excValue, tb)
        err_msg = "".join(traceback.format_exception(excType, excValue, tb))
        self.update_log.emit(err_msg)
        try:
            self.logThread.getLogMsg(err_msg)
        except RuntimeError:
            self.logThread = LogThread()
            self.logThread.start()
            self.update_log.connect(self.log_thread.getLogMsg)
            self.update_log.emit(err_msg)
            self.logThread.getLogMsg(err_msg)
        print("global error")
        # m_title = ""
        # m_info = "系统错误！"
        # infoMessage(m_info, m_title, 300)

    def sendException(self) -> None:
        """
        发送异常信息
        Returns:
            None
        """
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        self.update_log.emit(err_msg)

    def getData(self, msg) -> None:
        """
        虚函数
        槽函数
        获取主进程发来的数据
        Returns:
            None
        """
        pass

    def infoMessage(self) -> None:
        """
        弃用

        虚函数
        槽函数
        显示系统错误提示框
        Returns:
            None
        """
        pass

    def showErrorDialog(self) -> None:
        """
        虚函数
        槽函数
        显示系统错误提示框
        Returns:
            None
        """
        pass