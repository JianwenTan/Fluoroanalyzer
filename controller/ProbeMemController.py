from PySide2.QtCore import QThread, Signal, QStorageInfo
try:
    from controller.AbstractThread import AbstractThread
except ModuleNotFoundError:
    from qt0922.controller.AbstractThread import AbstractThread

failed_code = 404
succeed_code = 202


class MyProbe(AbstractThread):
    update_progress = Signal(int)

    def __init__(self):
        super().__init__()

    def run(self):
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