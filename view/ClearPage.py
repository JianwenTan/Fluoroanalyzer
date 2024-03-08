"""
@Description：存储清理界面显示
@Author：mysondrink@163.com
@Time：2024/1/11 10:52
"""
import datetime
try:
    import util.frozen as frozen
    # from func.infoPage import infoMessage
    from view.gui.clear import *
    # from inf.probeThread import MyProbe
    # from inf.clearThread import ClearThread
    from view.AbstractPage import AbstractPage
    from controller.ProbeMemController import MyProbe
    from controller.ClearController import ClearThread
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    # from func.infoPage import infoMessage
    from qt0223.view.gui.clear import *
    # from inf.probeThread import MyProbe
    # from inf.clearThread import ClearThread
    from qt0223.view.AbstractPage import AbstractPage
    from qt0223.controller.ProbeMemController import MyProbe
    from qt0223.controller.ClearController import ClearThread


class ClearPage(Ui_Form, AbstractPage):
    def __init__(self):
        """
        构造函数
        初始化界面信息
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self):
        """
        设置界面相关信息
        Returns:
            None
        """
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnConfirm.setIconSize(QSize(32, 32))
        self.ui.btnConfirm.setIcon(QIcon(confirm_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

        self.ui.clearCb.addItems(['7', '14', '21', '0'])
        self.ui.clearCb.setCurrentIndex(-1)
        self.ui.clearBar.setMinimum(0)
        self.ui.clearBar.setMaximum(100)

        self.setClearBar()

    def setClearBar(self):
        """
        设置存储条
        Returns:
            None
        """
        memorystr = QStorageInfo().root()
        memorystr.refresh()
        mem_total = memorystr.bytesTotal() / (1024 * 1024 * 1024)
        mem_avail = memorystr.bytesAvailable() / (1024 * 1024 * 1024)
        mem_progress = (1 - (mem_avail / mem_total)) * 100
        print('mem_progress:', mem_progress)
        self.ui.clearBar.setValue(int(mem_progress))

    def getInfo(self, msg):
        """
        槽函数
        清理结果处理，同时设置进度条显示
        Args:
            msg: 信号

        Returns:
            None
        """
        self.setClearBar()
        # m_title = "确认"
        # m_title = ""
        # m_info = "已经完成清理!"
        # infoMessage(m_info, m_title, 260)
        info = "已经完成清理!"
        self.showInfoDialog(info)
        return

    @Slot()
    def on_btnConfirm_clicked(self):
        """
        槽函数
        确认按钮操作
        Returns:
            None
        """
        # pic_path = frozen.app_path() + "/img/"
        # root_list = []
        # dirs_list = []
        # files_list = []
        # for root, dirs, files in os.walk(pic_path):
        #     root_list.append(root)
        #     dirs_list.append(dirs)
        #     files_list.append(files)

        if self.ui.clearCb.currentIndex() == -1:
            # m_title = "错误"
            # m_title = ""
            # m_info = "未选择时间，请选择后执行该操作！"
            # infoMessage(m_info, m_title)
            info = "未选择时间，请选择后执行该操作！"
            self.showInfoDialog(info)
            return
        dict_mode = {
            "7": 1,
            "14": 2,
            "21": 3,
            "0": 4
        }
        if dict_mode.get(self.ui.clearCb.currentText()) == 1:
            day = -7
            now_time = datetime.datetime.now()
            now_time = now_time + datetime.timedelta(days=day)
            # self.deleteDirs(str(now_time)[:10], root_list)
        elif dict_mode.get(self.ui.clearCb.currentText()) == 2:
            day = -14
            now_time = datetime.datetime.now()
            now_time = now_time + datetime.timedelta(days=day)
            # self.deleteDirs(str(now_time)[:10], root_list)

        elif dict_mode.get(self.ui.clearCb.currentText()) == 3:
            day = -21
            now_time = datetime.datetime.now()
            now_time = now_time + datetime.timedelta(days=day)
            # self.deleteDirs(str(now_time)[:10], root_list)
        elif dict_mode.get(self.ui.clearCb.currentText()) == 4:
            now_time = None
        self.myClearThread = ClearThread(str(now_time)[:10])
        self.myClearThread.finished.connect(self.myClearThread.deleteLater())
        self.myClearThread.finished.connect(self.getInfo)
        self.myClearThread.start()

    @Slot()
    def on_btnReturn_clicked(self):
        """
        槽函数
        返回按钮操作
        Returns:
            None
        """
        page_msg = 'SysPage'
        self.next_page.emit(page_msg)