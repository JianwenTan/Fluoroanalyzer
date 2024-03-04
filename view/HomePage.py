"""
@Description：菜单界面显示
@Author：mysondrink@163.com
@Time：2024/1/11 10:18
"""
try:
    import util.frozen as frozen
    # from func.infoPage import infoMessage
    from view.gui.home import *
    # from inf.probeThread import MyProbe
    from view.AbstractPage import AbstractPage
    from controller.HomePageController import HomePageController
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    # from func.infoPage import infoMessage
    from qt0223.view.gui.home import *
    # from inf.probeThread import MyProbe
    from qt0223.view.AbstractPage import AbstractPage
    from qt0223.controller.HomePageController import HomePageController


class HomePage(Ui_Form, AbstractPage):
    next_page = Signal(str)
    update_json = Signal(dict)
    update_log = Signal(str)

    def __init__(self):
        """
        构造函数
        初始化菜单界面信息，同时创建记录异常的信息
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self) -> None:
        """
        设置界面相关信息
        Returns:
            None
        """
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.startProbeMem()
        self.setBtnIcon()
        self.controller = HomePageController()
        self.controller.update_json.connect(self.memWarning)

    def setBtnIcon(self) -> None:
        """
        设置按钮图标
        Returns:
            None
        """
        reagent_icon_path = frozen.app_path() + r"/res/icon/reagent.png"
        pixImg = self.mySetIconSize(reagent_icon_path)
        self.ui.reagent_icon_label.setPixmap(pixImg)
        self.ui.reagent_icon_label.setAlignment(Qt.AlignCenter)

        history_icon_path = frozen.app_path() + r"/res/icon/history.png"
        pixImg = self.mySetIconSize(history_icon_path)
        self.ui.history_icon_label.setPixmap(pixImg)
        self.ui.history_icon_label.setAlignment(Qt.AlignCenter)

        reagent_set_icon_path = frozen.app_path() + r"/res/icon/set.png"
        pixImg = self.mySetIconSize(reagent_set_icon_path)
        self.ui.reagent_set_icon_label.setPixmap(pixImg)
        self.ui.reagent_set_icon_label.setAlignment(Qt.AlignCenter)

        sys_icon_path = frozen.app_path() + r"/res/icon/sys.png"
        pixImg = self.mySetIconSize(sys_icon_path)
        self.ui.sys_icon_label.setPixmap(pixImg)
        self.ui.sys_icon_label.setAlignment(Qt.AlignCenter)

        power_icon_path = frozen.app_path() + r"/res/icon/power.png"
        self.ui.btnPower.setIconSize(QSize(32, 32))
        self.ui.btnPower.setIcon(QIcon(power_icon_path))

    def mySetIconSize(self, path) -> QPixmap:
        """
        设置按钮图标比例
        Args:
            path: 图片路径

        Returns:
            None
        """
        img = QImage(path)  # 创建图片实例
        mgnWidth = 50
        mgnHeight = 50  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        pixImg = QPixmap.fromImage(
            img.scaled(size, Qt.IgnoreAspectRatio))  # 修改图片实例大小并从QImage实例中生成QPixmap实例以备放入QLabel控件中
        return pixImg

    def memWarning(self, msg) -> None:
        """
        存储满后警告或直接跳转
        Args:
            msg: 存储探测的结果

        Returns:
            None
        """
        code = msg['code']
        if code == 404:
            m_title = "警告"
            m_info = "存储已经占满，请清理图片！"
            self.showInfo(m_info)
            return
        elif code == 202:
            page_msg = 'TestPage'
            self.next_page.emit(page_msg)
            # self.myprobe.deleteLater()

    @Slot()
    def on_btnPower_clicked(self) -> None:
        """
        槽函数
        电源按钮操作，跳转到电源界面
        Returns:
            None
        """
        page_msg = 'PowerPage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnData_clicked(self) -> None:
        """
        槽函数
        荧光检测按钮操作，跳转到荧光检测界面
        Returns:
            None
        """
        self.controller.startProbeMem()
        # page_msg = 'testPage'
        # self.next_page.emit(page_msg)

    @Slot()
    def on_btnHistory_clicked(self) -> None:
        """
        槽函数
        历史记录按钮操作，跳转到历史记录界面
        Returns:
            None
        """
        page_msg = 'HistoryPage'
        self.next_page.emit(page_msg)

    # @Slot()
    # def on_btnSet_clicked(self) -> None:
    #     """
    #     弃用
    #
    #     槽函数
    #     检疫设置按钮操作，跳转到检疫设置界面
    #     Returns:
    #         None
    #     """
    #     page_msg = 'EditPage'
    #     self.next_page.emit(page_msg)

    @Slot()
    def on_btnSet_clicked(self) -> None:
        page_msg = 'RegPage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnPara_clicked(self) -> None:
        """
        槽函数
        系统设置按钮操作，跳转到系统设置界面
        Returns:
            None
        """
        page_msg = 'SysPage'
        self.next_page.emit(page_msg)