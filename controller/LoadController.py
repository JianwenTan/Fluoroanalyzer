"""
@Description：加载界面控制
@Author：mysondrink@163.com
@Time：2024/1/9 10:54
"""
from PySide2.QtCore import Signal, QTimer, QThreadPool
try:
    from controller.AbstractController import AbstractController
    from controller.DBController import CheckDataBaseThread
    from controller.CameraController import CheckCameraThread
    from controller.SerialController import CheckSerialThread
except ModuleNotFoundError:
    from qt0223.controller.AbstractController import AbstractController
    from qt0223.controller.DBController import CheckDataBaseThread
    from qt0223.controller.CameraController import CheckCameraThread
    from qt0223.controller.SerialController import CheckSerialThread

FLAG_NUM = 0
FAILED_CODE = 404
SUCCEED_CODE = 202


class LoadController(AbstractController):
    update_page = Signal()      # page signal to send next page name
    update_retry = Signal()     # retry signal to send detection

    def __init__(self) -> object:
        """
        初始化类成员变量
        Returns:
            None
        """
        super().__init__()
        self._len = 0
        self.thread_len = 0
        self.thread_list = []
        self.thread_id = []
        self.change_timer = None

    def startThread(self):
        """
        开启相机、数据库、串口的线程检测
        Returns:
            None
        """
        self.flag_num = FLAG_NUM
        self.thread_list = [CheckCameraThread(), CheckSerialThread(), CheckDataBaseThread()]
        self.thread_id = []
        self.thread_len = len(self.thread_list) * 2
        self.pool = QThreadPool()
        self.pool.globalInstance()
        for num in range(len(self.thread_list)):
            self.thread_id.append(self.thread_list[num])
            self.thread_list[num].update_json.connect(self.setInfoLabel)
            # self.thread_list[num].setAutoDelete(True)
            # self.pool.start(self.thread_list[num])
            self.thread_list[num].finished.connect(lambda: self.thread_list[num].deleteLater())
            self.thread_list[num].start()

    # @Slot()
    def setInfoLabel(self, msg):
        """
        槽函数
        开启相机、数据库、串口的线程检测
        创建线程池来同时检测上述线程
        Args:
            msg: 发送来的信号

        Returns:
            None
        """
        try:
            info_msg, code_msg, status_msg = msg['info'], msg['code'], msg['status']
            if status_msg in self.thread_id:
                self.thread_id.remove(status_msg)
            self.update_json.emit(dict(info=info_msg))
            if code_msg == FAILED_CODE:
                self.flag_num = -1
                self.update_retry.emit()
            self._len = self._len + 1
            if self._len % self.thread_len == 0 and self.flag_num == FLAG_NUM:
                # create a timer
                self.change_timer = QTimer()
                self.change_timer.timeout.connect(lambda: self.update_page.emit())
                self.change_timer.timeout.connect(lambda: self.change_timer.stop())
                # set timer delay time, unit is second
                # delay time is 2
                delay_time = 2000
                self.change_timer.start(delay_time)
        except Exception as e:
            self.sendException()
            print(e)
            # m_title = ""
            # m_info = "系统错误！"
            # infoMessage(m_info, m_title, 300)
