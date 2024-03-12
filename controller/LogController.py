from PySide2.QtCore import QThread, Signal
import logging
import sys
import traceback
try:
    import util.frozen as frozen
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen

LOG_FILE = frozen.app_path() + r"/log/reagent.log"


class LogThread(QThread):
    error_info = Signal()       

    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = None
        self.log_file = LOG_FILE

    def run(self):
        try:
            # create an instance logger
            self.logger = logging.getLogger()
            self.logger.setLevel(logging.INFO)  # Log等级总开关  此时是INFO

            # create an instance handler to write log file
            # logfile = frozen.app_path() + r'/log/reagent.log'
            fh = logging.FileHandler(self.log_file, mode='a')  # open的打开模式这里可以进行参考
            fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

            # 定义handler的输出格式（时间，文件，行数，错误级别，错误提示）
            formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
            fh.setFormatter(formatter)
            """
            如果没有移除上一次的FileHandler对象，第二次logger对象就会再次获得相同的FileHandler对象
            通过判断logger对象的handlers属性，或者hasHandlers函数，保持同一loggername对应的FileHander唯一
            """
            if not self.logger.handlers:
                # add logger to handler
                self.logger.addHandler(fh)

            # 日志级别
            #
            # DEBUG：详细的信息,通常只出现在诊断问题上
            # INFO：确认一切按预期运行
            # WARNING（默认）：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
            # ERROR：更严重的问题,软件没能执行一些功能
            # CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            self.logger.warning(err_msg)

    def getLogMsg(self, msg):
        self.error_info.emit()
        self.logger.error(msg)