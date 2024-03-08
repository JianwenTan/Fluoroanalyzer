"""
@Description：存储检测控制类
@Author：mysondrink@163.com
@Time：2024/1/15 16:06
"""
from PySide2.QtCore import QThread, Signal, QStorageInfo
try:
    from controller.AbstractThread import AbstractThread
except ModuleNotFoundError:
    from qt0223.controller.AbstractThread import AbstractThread

failed_code = 404
succeed_code = 202


class MyProbe(AbstractThread):
    update_progress = Signal(int)

    def __init__(self):
        """
        构造函数
        初始化线程，同时创建记录异常的信息
        """
        super().__init__()

    def run(self):
        """
        线程运行函数
        进行系统存储的检测
        Returns:
            None
        """
        try:
            memorystr = QStorageInfo().root()
            # clear the memory storage last time record
            memorystr.refresh()
            mem_total = memorystr.bytesTotal() / (1024 * 1024 * 1024)
            mem_avail = memorystr.bytesAvailable() / (1024 * 1024 * 1024)
            mem_progress = mem_avail / mem_total
            if mem_progress < 0.02:
                self.update_progress.emit(failed_code)
            else:
                self.update_progress.emit(succeed_code)
        except Exception as e:
            self.update_progress.emit(failed_code)
            self.sendException()
        finally:
            self.log_thread.deleteLater()