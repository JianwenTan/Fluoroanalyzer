import time
import os
try:
    import util.frozen as frozen
    from controller.AbstractThread import AbstractThread
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.controller.AbstractThread import AbstractThread

TIME_TO_SLEEP = 2
TRYLOCK_TIME = -1
FAILED_CODE = 404
SUCCEED_CODE = 202

SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'


class CheckDataBaseThread(AbstractThread):
    def __init__(self) -> object:
        super().__init__()

    def run(self):
        try:
            info_msg = "数据库检测中。。。"
            code_msg = SUCCEED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            connection = True
            # check the db file is exist True of False
            if os.path.exists(SQL_PATH):
                # qmutex.tryLock(trylock_time)
                time.sleep(TIME_TO_SLEEP)
                info_msg = "数据库检测成功！"
                code_msg = SUCCEED_CODE
                status_msg = self.currentThread()
                # qmutex.unlock()
            else:
                # qmutex.tryLock(trylock_time)
                time.sleep(TIME_TO_SLEEP)
                info_msg = "数据库检测失败！"
                code_msg = FAILED_CODE
                status_msg = self.currentThread()
                # qmutex.unlock()
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
        except Exception as e:
            self.sendException()
            info_msg = "db error！"
            code_msg = FAILED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
        finally:
            self.log_thread.deleteLater()
