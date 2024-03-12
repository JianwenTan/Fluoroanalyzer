try:
    import util.frozen as frozen
    from view.gui.home import *
    from view.AbstractPage import AbstractPage
    from controller.HomePageController import HomePageController
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.view.gui.home import *
    from qt0922.view.AbstractPage import AbstractPage
    from qt0922.controller.HomePageController import HomePageController

CONFIG_FILE = frozen.app_path() + r"/config/configname.ini"


class HomePage(Ui_Form, AbstractPage):
    next_page = Signal(str)
    update_json = Signal(dict)
    update_log = Signal(str)

    def __init__(self):

        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self) -> None:

        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.startProbeMem()
        self.setBtnIcon()
        self.controller = HomePageController()
        self.controller.update_json.connect(self.memWarning)
        self.ui.btnSet.setText("  仪器设置")

    def setBtnIcon(self) -> None:

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

        img = QImage(path)  # 创建图片实例
        mgnWidth = 50
        mgnHeight = 50  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        pixImg = QPixmap.fromImage(
            img.scaled(size, Qt.IgnoreAspectRatio))  # 修改图片实例大小并从QImage实例中生成QPixmap实例以备放入QLabel控件中
        return pixImg

    def memWarning(self, msg) -> None:

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
        page_msg = 'PowerPage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnData_clicked(self) -> None:

        self.controller.startProbeMem()
        # page_msg = 'testPage'
        # self.next_page.emit(page_msg)

    @Slot()
    def on_btnHistory_clicked(self) -> None:
        page_msg = 'HistoryPage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnSet_clicked(self) -> None:
        if self.checkAdminName():
            page_msg = 'RegPage'
            self.next_page.emit(page_msg)
        else:
            info = "当前用户没有权限！"
            self.showInfoDialog(info)

    @Slot()
    def on_btnPara_clicked(self) -> None:
        page_msg = 'SysPage'
        self.next_page.emit(page_msg)

    def checkAdminName(self):
        settings = QSettings(CONFIG_FILE, QSettings.IniFormat)
        settings.setIniCodec("UTF-8")
        admin_name = settings.value("USER/user_name")
        return True if admin_name == "admin" else False