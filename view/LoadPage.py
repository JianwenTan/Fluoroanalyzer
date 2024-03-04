"""
@Description：加载界面
@Author：mysondrink@163.com
@Time：2024/1/9 9:56
"""
import time
try:
    from view.AbstractPage import AbstractPage
    from controller.BlinkController import CheckBlinkThread
    from controller.LoadController import LoadController
    import util.frozen as frozen
    from view.gui.loading import *
    from view.LoginPage import LoginPage
    from view.HomePage import HomePage
    from view.RegisterPage import RegisterPage
    from view.DataPage import DataPage
    from view.TestPage import TestPage
    from view.PowerPage import PowerPage
    from view.HistoryPage import HistoryPage
    # from view.EditPage import EditPage
    from view.SysPage import SysPage
    from view.WifiPage import WifiPage
    from view.ClearPage import ClearPage
    from view.SetPage import SetPage
    from view.AboutPage import AboutPage
    from view.RegPage import RegPage
    from view.UpdatePage import UpdatePage
except ModuleNotFoundError:
    from qt0223.view.AbstractPage import AbstractPage
    from qt0223.controller.BlinkController import CheckBlinkThread
    from qt0223.controller.LoadController import LoadController
    import qt0223.util.frozen as frozen
    from qt0223.view.gui.loading import *
    from qt0223.view.LoginPage import LoginPage
    from qt0223.view.HomePage import HomePage
    from qt0223.view.RegisterPage import RegisterPage
    from qt0223.view.DataPage import DataPage
    from qt0223.view.TestPage import TestPage
    from qt0223.view.PowerPage import PowerPage
    from qt0223.view.HistoryPage import HistoryPage
    # from qt0223.view.EditPage import EditPage
    from qt0223.view.SysPage import SysPage
    from qt0223.view.WifiPage import WifiPage
    from qt0223.view.ClearPage import ClearPage
    from qt0223.view.SetPage import SetPage
    from qt0223.view.AboutPage import AboutPage
    from qt0223.view.RegPage import RegPage
    from qt0223.view.UpdatePage import UpdatePage

FLAG_NUM = 0
FAILED_CODE = 404
SUCCEED_CODE = 202
CONFIG_FILE = frozen.app_path() + r"/config/configname.ini"


class LoadPage(Ui_Form, AbstractPage):
    """
    这部分controller只实现线程检测
    """
    def __init__(self) -> object:
        """
        构造函数
        初始化类变量
        Returns:
            object
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()
        # self.list_widget = None  # 当前页面list，MAX 2
        # self.cur_page = None  # 记录当前页面
        self.flag_num = FLAG_NUM  # 界面跳转标志位
        # self.blink_timer = QTime()  # 图标闪烁定时器
        # self.blink_flag = True  # 图标闪烁定时器标志位
        # self.myBlinkThread = None  # 图标闪烁线程
        # self.thread_timer = QTime()  # 闪烁线程运行定时器
        # self.controller = None  # loadPage controller
        # self._s = None  # 定义QStackedLayout
        # self._h = None  # 定义QHBoxLayout
        # self.q_ptr = None  # 定义QStackedLayout尾指针
        # self.p_ptr = None   # 定义QStackedLayout头指针
        # self.timer = QTime()

    def InitUI(self) -> None:
        """
        设置界面相关信息
        Returns:
            None
        """
        self.statusShowTime()
        self.title_timer = QTimer()
        self.title_timer.timeout.connect(self.setTitle)
        thread_delay_time = 2000
        self.title_timer.start(thread_delay_time)
        # self.ui.title_label.setText('  荧光分析仪')
        self.ui.retry_icon_label.hide()
        self.ui.btnRetry.hide()
        # self.ui.textEdit.setEnabled(False)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉窗口状态栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗口背景透明
        self.setFocusPolicy(Qt.NoFocus)
        self.ui.centerframe.setFrameStyle(QFrame.NoFrame)
        self.ui.topframe.setFrameStyle(QFrame.NoFrame)

        screen = QDesktopWidget().screenGeometry()
        self.move(screen.left(), screen.top())
        self.showMaximized()

        # 创建定时器
        self.blink_timer = QTimer()
        self.blink_flag = True
        self.blink_timer.timeout.connect(self.blinkIcon)
        self.myBlinkThread = CheckBlinkThread()
        self.myBlinkThread.update_json.connect(self.blinkAssess)
        self.thread_timer = QTimer()
        self.thread_timer.timeout.connect(self.myBlinkThread.start)
        # self.thread_timer.timeout.connect(lambda: print("thread_timer"))
        thread_delay_time = 2000
        self.thread_timer.start(thread_delay_time)

        self.next_page.connect(self.changePage)

        self.controller = LoadController()
        self.controller.update_json.connect(self.setInfoLabel)
        self.controller.update_page.connect(self.showPage)
        self.controller.update_retry.connect(self.retryThread)
        self.controller.startThread()

    def setTitle(self):
        settings = QSettings(CONFIG_FILE, QSettings.IniFormat)
        settings.setIniCodec("UTF-8")
        self.ui.title_label.setText("  " + settings.value("MACHINE/machine_name"))

    def blinkAssess(self, msg) -> None:
        """
        检测设备wifi连接情况，同时设置图标进行显示
        Args:
            msg: wifi连接标志位

        Returns:
            None
        """
        self.blink_timer.stop()
        code = msg['code']
        # print(code)
        if code == 202:
            self.ui.wifi_label.show()
            wifi_icon_path = frozen.app_path() + r"/res/icon/icon-wi-fi.png"
            pixImg = self.mySetIconSize(wifi_icon_path)
            self.ui.wifi_label.setPixmap(pixImg)
            self.ui.wifi_label.setAlignment(Qt.AlignCenter)
        elif code == 404:
            wifi_icon_path = frozen.app_path() + r"/res/icon/icon-wi-fi-disconnected.png"
            pixImg = self.mySetIconSize(wifi_icon_path)
            self.ui.wifi_label.setPixmap(pixImg)
            self.ui.wifi_label.setAlignment(Qt.AlignCenter)
            # 设置定时器延迟时间，单位为毫秒
            # 延迟0.5秒跳转
            delay_time = 500
            self.blink_timer.start(delay_time)

    def blinkIcon(self) -> None:
        """
        图标闪烁提示
        Returns:
            None
        """
        if self.blink_flag:
            self.blink_flag = False
            self.ui.wifi_label.hide()
        else:
            self.blink_flag = True
            self.ui.wifi_label.show()

    def mySetIconSize(self, path) -> None:
        """
        设置按钮图标比例
        Args:
            path: 图片路径

        Returns:
            None
        """
        img = QImage(path)  # 创建图片实例
        mgnWidth = 30
        mgnHeight = 30  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        pixImg = QPixmap.fromImage(
            img.scaled(size, Qt.IgnoreAspectRatio))  # 修改图片实例大小并从QImage实例中生成QPixmap实例以备放入QLabel控件中
        return pixImg

    # @Slot()
    def setInfoLabel(self, msg) -> None:
        """
        槽函数
        获取相机、数据库、串口的线程检测反馈信息
        Args:
            msg: 检测反馈信息

        Returns:
            None
        """
        try:
            info_msg = msg['info']
            self.ui.textEdit.append(info_msg)
        except Exception as e:
            self.sendException()
            print(e)

    def showPage(self) -> None:
        """
        槽函数
        设置主界面中子界面的显示位置，同时显示登录界面
        Returns:
            None
        """
        # print("showPage")
        self.list_widget = []
        if self.flag_num == 0:
            self._s = QStackedLayout()
            self._h = QHBoxLayout()
            # self.cur_page = perinfoPage()

            self._h.addLayout(self._s)
            self.ui.centerframe.setLayout(self._h)

            self._s.setSpacing(0)
            self._h.setSpacing(0)

            self._s.setContentsMargins(0, 0, 0, 0)
            self._h.setContentsMargins(0, 0, 0, 0)

            self.flag_num = -1
            # 尾指针
            self.q_ptr = self._s.currentIndex()
            # 头指针
            self.p_ptr = self._s.currentIndex()
            self.next_page.emit("LoginPage")

    def changePage(self, msg):
        try:
            # 设置栈为2
            num = len(self.list_widget)
            if msg == 'history':
                temp = self.list_widget[1]
                self._s.removeWidget(self._s.currentWidget())
                self.list_widget.remove(self.list_widget[1])
                self.p_ptr -= 1
                temp.close()
                return
            # if num > 1:
            #     self._s.removeWidget(self.list_widget[0])
            #     self.list_widget.remove(self.list_widget[0])
            #     self.p_ptr += 1
            #     time.sleep(0.5)
            self.cur_page = globals()[msg]()
            self.update_json.connect(self.cur_page.getData)  # 更改，发送给controller
            self.cur_page.next_page.connect(self.changePage)
            self.cur_page.update_json.connect(lambda data: self.update_json.emit(data))  # 获取子界面发送的信息，同时发送给其他子界面
            # self.cur_page.update_log.connect(self.log_thread.getLogMsg)
            self.cur_page.setFocus()

            # 防止页面重复
            # num = len(self.list_widget)
            # if self._s.indexOf(self.cur_page) > -1:
            #     self._s.removeWidget(self.list_widget[1])
            #     self.list_widget.remove(self.list_widget[1])
            #     self.q_ptr -= 1
            #     time.sleep(0.5)
            #     return
            if num > 1:
                temp = self.list_widget[0]
                self._s.removeWidget(self.list_widget[0])
                self.list_widget.remove(self.list_widget[0])
                self.p_ptr += 1
                temp.close()
                time.sleep(0.5)

            self._s.addWidget(self.cur_page)
            self._s.setCurrentIndex(self._s.count() - 1)
            self.list_widget.append(self._s.currentWidget())
            self.q_ptr += 1
            # self.ui.centerframe.setLayout(self._s)
            # self.cur_page.show()
        except Exception as e:
            self.sendException()
            print(e)
            # m_title = ""
            # m_info = "系统错误！"
            # infoMessage(m_info, m_title, 300)

    def statusShowTime(self) -> None:
        """
        设置时间显示，间隔为1秒
        Returns:
            None
        """
        self.timer = QTimer()
        self.timer.timeout.connect(self.showCurrentTime)

        self.timer.start(1000)

    def showCurrentTime(self) -> None:
        """
        设置显示时间格式
        Returns:
            None
        """
        cur_time = QDateTime.currentDateTime()
        time_display = cur_time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.ui.time_label.setText(time_display)

    def retryThread(self) -> None:
        """
        槽函数
        显示重试标签、按钮
        Returns:
            None
        """
        self.ui.retry_icon_label.show()
        self.ui.btnRetry.show()

    def getJsonData(self, msg) -> None:
        """
        弃用
        槽函数
        获取子界面发送的信息，同时发送给其他子界面
        Args:
            msg: 发送的信号，获取子页面返回的信号，信号是子界面的信息

        Returns:
            None
        """
        self.update_json.connect(self.cur_page.getData)  # 更改，发送给controller
        self.update_json.emit(msg)

    # def showErrorDialog(self) -> None:
    #     """
    #     弃用
    #
    #     显示系统错误弹窗
    #     Returns:
    #         None
    #     """
    #     info = "系统错误"
    #     code = 404
    #     print(info + " from ", self._s.currentWidget())
    #     # self.showInfoDialog(info)
    #     self.showInfoDialog(dict(info=info, code=code))

    @Slot()
    def on_btnRetry_clicked(self) -> None:
        """
        槽函数
        重试按钮，重新进行相机、数据库、串口的线程检测
        Returns:
            None
        """
        self.ui.textEdit.clear()
        # self.flag_num = FLAG_NUM
        self.ui.retry_icon_label.hide()
        self.ui.btnRetry.hide()
        # for num in range(len(self.thread_id)):
        #     stat = self.thread_id[num].isFinished()
        #     if self.thread_id[num].isFinished() is False:
        #         continue
        #     self.thread_id[num].deleteLater()
        # self.thread_id.clear()
        # self.startThread()
        self.controller.startThread()
