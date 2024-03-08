"""
@Description：图标闪烁类
@Author：mysondrink@163.com
@Time：2024/1/9 10:08
"""
from PySide2.QtNetwork import QNetworkInterface, QAbstractSocket
try:
    from controller.AbstractThread import AbstractThread
    from controller.AbstractController import AbstractController
except ModuleNotFoundError:
    from qt0223.controller.AbstractThread import AbstractThread
    from qt0223.controller.AbstractController import AbstractController

TIME_TO_SLEEP = 2
TRYLOCK_TIME = -1
FAILED_CODE = 404
SUCCEED_CODE = 202


class CheckBlinkThread(AbstractThread):
    def __init__(self):
        """
        构造函数
        初始化线程，调用父类方法进行日志记录
        """
        super().__init__()

    def run(self):
        """
        线程运行函数
        进行wifi的检测
        Returns:
            None
        """
        try:
            wifi_interface = "wlan0"
            flag = 1
            # print("connect assess")
            interfaces = QNetworkInterface.allInterfaces()
            for interface in interfaces:
                if interface.name() == wifi_interface:
                    for entry in interface.addressEntries():
                        if entry.ip().protocol() == QAbstractSocket.NetworkLayerProtocol.IPv4Protocol:
                            if entry.ip().toString() != '':
                                flag = 1
                                break
                            else:
                                flag = 0
                                break
                        else:
                            flag = 0
                            break
                else:
                    flag = 0
                    break
            if flag == 1:
                # print("True")
                info_msg = "connected"
                code_msg = SUCCEED_CODE
                status_msg = 1
                self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            else:
                # print("False")
                info_msg = "not connected"
                code_msg = FAILED_CODE
                status_msg = 1
                self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
        except Exception as e:
            info_msg = "network error"
            code_msg = FAILED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            print(e)
            self.sendException()
        # finally:
        #     self.log_thread.deleteLater()
