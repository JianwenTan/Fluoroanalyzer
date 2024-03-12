import sys
import traceback
from PySide2.QtCore import QThread, Signal
try:
    from controller.LogController import LogThread
except ModuleNotFoundError:
    from qt0922.controller.LogController import LogThread


class AbstractThread(QThread):
    update_log = Signal(str)    # log signal to send msg
    update_json = Signal(dict)  # json signal to send data

    def __init__(self):
        super().__init__()
        self.log_thread = LogThread()
        self.log_thread.start()
        self.update_log.connect(self.log_thread.getLogMsg)
        self.old_hook = sys.excepthook
        sys.excepthook = self.HandleException

    def __del__(self):
        print(f"delete thread {self.__class__.__name__}")

    def deleteLater(self):
        if self.parent() is None:
            pass
        else:
            super().deleteLater()
            print(f"delete thread {self.__class__.__name__}")

    def HandleException(self, excType, excValue, tb):
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

    def sendException(self):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        self.update_log.emit(err_msg)
