"""
@Description：串口检测控制类
@Author：mysondrink@163.com
@Time：2024/1/9 10:31
"""
import time
try:
    from controller.AbstractThread import AbstractThread
    from pic_code.img_main import img_main
except ModuleNotFoundError:
    from qt0223.controller.AbstractThread import AbstractThread
    from qt0223.pic_code.img_main import img_main

TIME_TO_SLEEP = 2
TRYLOCK_TIME = -1
FAILED_CODE = 404
SUCCEED_CODE = 202


class CheckSerialThread(AbstractThread):
    def __init__(self):
        """
        构造函数
        初始化线程，调用父类方法进行日志记录
        """
        super().__init__()

    def run(self):
        """
        线程运行函数
        进行串口的检测
        Returns:
            None
        """
        # qmutex.tryLock(trylock_time)
        try:
            info_msg = "串口检测中。。。"
            code_msg = SUCCEED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            time.sleep(TIME_TO_SLEEP)
            # check serial is True or False
            Main = img_main()
            if Main.natPrint_init():
                info_msg = "串口检测成功！"
                code_msg = SUCCEED_CODE
                status_msg = self.currentThread()
                self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            else:
                info_msg = "串口检测失败！"
                code_msg = FAILED_CODE
                status_msg = self.currentThread()
                self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            # qmutex.unlock()
        except Exception as e:
            self.sendException()
            info_msg = "serial error！"
            code_msg = FAILED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
        finally:
            self.log_thread.deleteLater()
