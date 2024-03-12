import sys
import traceback

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
try:
    from controller.LogController import LogThread
except ModuleNotFoundError:
    from qt0922.controller.LogController import LogThread


class AbstractWidget(QWidget):
    update_log = Signal(str)
    update_json = Signal(dict)
    next_page = Signal(str)
    update_info = Signal(str)

    def __init__(self):
        super().__init__()
        self.logThread = LogThread()
        self.logThread.start()
        self.update_log.connect(self.logThread.getLogMsg)
        self.logThread.error_info.connect(self.showErrorDialog)
        sys.excepthook = self.HandleException

    def __del__(self):
        print(f"delete widget{self.__class__.__name__}")

    def deleteLater(self) -> None:
        super().deleteLater()
        print(f"delete widget{self.__class__.__name__}")

    def HandleException(self, excType, excValue, tb) -> None:
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
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        self.update_log.emit(err_msg)

    def getData(self, msg) -> None:
        pass

    def infoMessage(self) -> None:
        pass

    def showErrorDialog(self) -> None:
        pass