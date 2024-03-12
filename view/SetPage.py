try:
    import util.frozen as frozen
    from view.gui.set import *
    from view.AbstractPage import AbstractPage
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.view.gui.set import *
    from qt0922.view.AbstractPage import AbstractPage

class SetPage(Ui_Form, AbstractPage):
    next_page = Signal(str)
    update_json = Signal(dict)
    update_log = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self):
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.ui.modeBox_4.addItems(["5000x4000", "3000x2000"])

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnConfirm.setIconSize(QSize(32, 32))
        self.ui.btnConfirm.setIcon(QIcon(confirm_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

        self.setBtnIcon()

    def setBtnIcon(self):
        icon_1_path = frozen.app_path() + r"/res/icon/icon-1.png"
        pixImg = self.mySetIconSize(icon_1_path)
        self.ui.label.setPixmap(pixImg)
        self.ui.label.setAlignment(Qt.AlignCenter)

        icon_2_path = frozen.app_path() + r"/res/icon/icon-2.png"
        pixImg = self.mySetIconSize(icon_2_path)
        self.ui.label_2.setPixmap(pixImg)
        self.ui.label_2.setAlignment(Qt.AlignCenter)


    def mySetIconSize(self, path):
        img = QImage(path)  # 创建图片实例
        mgnWidth = 50
        mgnHeight = 50  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        pixImg = QPixmap.fromImage(
            img.scaled(size, Qt.IgnoreAspectRatio))  # 修改图片实例大小并从QImage实例中生成QPixmap实例以备放入QLabel控件中
        return pixImg


    @Slot()
    def on_btnConfirm_clicked(self):
        # m_title = ""
        # m_info = "成功！"
        # infoMessage(m_info, m_title, 400)
        info = "成功！"
        self.showInfoDialog(info)


    @Slot()
    def on_btnReturn_clicked(self):
        page_msg = 'SysPage'
        self.next_page.emit(page_msg)

