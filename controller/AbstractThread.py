"""
@Description：抽象线程类
@Author：mysondrink@163.com
@Time：2024/1/9 10:09
"""
import sys
import traceback
from PySide2.QtCore import QThread, Signal
try:
    from controller.LogController import LogThread
except ModuleNotFoundError:
    from qt0223.controller.LogController import LogThread


class AbstractThread(QThread):
    update_log = Signal(str)
    update_json = Signal(dict)

    def __init__(self):
        """
        构造函数，初始化日志类
        """
        super().__init__()
        self.log_thread = LogThread()
        self.log_thread.start()
        self.update_log.connect(self.log_thread.getLogMsg)
        self.old_hook = sys.excepthook
        sys.excepthook = self.HandleException

    def __del__(self):
        """
        析构函数，打印类名
        """
        print(f"delete thread {self.__class__.__name__}")

    def deleteLater(self) -> None:
        """
        打印删除的类的名
        Returns:
            None
        """
        if self.parent() is None:
            pass
        else:
            super().deleteLater()
            print(f"delete thread {self.__class__.__name__}")

    def HandleException(self, excType, excValue, tb) -> None:
        """
        自动捕获和输出异常类
        Args:
            excType: 异常类型
            excValue: 异常对象
            tb: 异常的trace back

        Returns:

        """
        print("m_info")
        sys.__excepthook__(excType, excValue, tb)
        # self.old_hook(excType, excValue, tb)
        err_msg = "".join(traceback.format_exception(excType, excValue, tb))
        self.update_log.emit(err_msg)
        try:
            self.log_thread.getLogMsg(err_msg)
        except RuntimeError:
            self.log_thread = LogThread()
            self.log_thread.start()
            self.update_log.connect(self.log_thread.getLogMsg)
            self.update_log.emit(err_msg)
            self.log_thread.getLogMsg(err_msg)
        # m_title = ""
        # m_info = "系统错误！"
        # infoMessage(m_info, m_title, 300)

    def sendException(self) -> None:
        """
        手动发送异常信息
        Returns:
            None
        """
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        self.update_log.emit(err_msg)
