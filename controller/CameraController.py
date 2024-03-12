import time
try:
    from controller.AbstractThread import AbstractThread
    from pic_code.img_main import img_main
except ModuleNotFoundError:
    from qt0922.pic_code.img_main import img_main
    from qt0922.controller.AbstractThread import AbstractThread


TIME_TO_SLEEP = 2
TRYLOCK_TIME = -1
FAILED_CODE = 404
SUCCEED_CODE = 202


class CheckCameraThread(AbstractThread):
    def __init__(self):
        super().__init__()

    def run(self):
        try:
            # qmutex.tryLock(trylock_time)
            info_msg = "摄像头检测中。。。"
            code_msg = SUCCEED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            time.sleep(TIME_TO_SLEEP)
            # check the camera is True or False
            Main = img_main()
            if Main.imgLed_init() and Main.imgCamera_init():
                info_msg = "摄像头检测成功！"
                code_msg = SUCCEED_CODE
                status_msg = self.currentThread()
                self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            else:
                info_msg = "摄像头检测失败！"
                code_msg = FAILED_CODE
                status_msg = self.currentThread()
                self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            # qmutex.unlock()
        except Exception as e:
            self.sendException()
            info_msg = "camera error！"
            code_msg = FAILED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
        finally:
            self.log_thread.deleteLater()