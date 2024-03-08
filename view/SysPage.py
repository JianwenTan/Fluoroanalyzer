"""
@Description：系统设置界面显示
@Author：mysondrink@163.com
@Time：2024/1/11 10:48
"""
try:
    import util.frozen as frozen
    from view.gui.sys import *
    from view.AbstractPage import AbstractPage
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.view.gui.sys import *
    from qt0223.view.AbstractPage import AbstractPage


class SysPage(Ui_Form, AbstractPage):
    def __init__(self):
        """
        系统设置界面，进行wifi界面、清理界面、软件更新界面、关于仪器界面的跳转
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
        self.ui.btnSet.setText("   软件更新")
        self.setBtnIcon()

    def setBtnIcon(self):
        """
        设置按钮图标
        Returns:
            None
        """
        wifi_icon_path = frozen.app_path() + r"/res/icon/wifi.png"
        pixImg = self.mySetIconSize(wifi_icon_path)
        self.ui.wifi_icon_label.setPixmap(pixImg)
        self.ui.wifi_icon_label.setAlignment(Qt.AlignCenter)

        camera_icon_path = frozen.app_path() + r"/res/icon/camera.png"
        pixImg = self.mySetIconSize(camera_icon_path)
        self.ui.camera_icon_label.setPixmap(pixImg)
        self.ui.camera_icon_label.setAlignment(Qt.AlignCenter)

        clear_icon_path = frozen.app_path() + r"/res/icon/clear.png"
        pixImg = self.mySetIconSize(clear_icon_path)
        self.ui.clear_icon_label.setPixmap(pixImg)
        self.ui.clear_icon_label.setAlignment(Qt.AlignCenter)

        about_icon_path = frozen.app_path() + r"/res/icon/about.png"
        pixImg = self.mySetIconSize(about_icon_path)
        self.ui.about_icon_label.setPixmap(pixImg)
        self.ui.about_icon_label.setAlignment(Qt.AlignCenter)

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

    def mySetIconSize(self, path):
        """
        设置按钮图标比例
        Args:
            path: 图标的路径

        Returns:
            QPixmap: 设置好图标的QPixmap类实例
        """
        img = QImage(path)  # 创建图片实例
        mgnWidth = 50
        mgnHeight = 50  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        pixImg = QPixmap.fromImage(
            img.scaled(size, Qt.IgnoreAspectRatio))  # 修改图片实例大小并从QImage实例中生成QPixmap实例以备放入QLabel控件中
        return pixImg

    @Slot()
    def on_btnWifi_clicked(self):
        """
        槽函数
        wifi页面跳转
        Returns:
            None
        """
        page_msg = 'WifiPage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnClear_clicked(self):
        """
        槽函数
        清理页面跳转
        Returns:
            None
        """
        page_msg = 'ClearPage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnSet_clicked(self):
        """
        槽函数
        软件更新页面跳转
        Returns:
            None
        """
        page_msg = 'UpdatePage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnAbout_clicked(self):
        """
        槽函数
        关于页面跳转
        Returns:
            None
        """
        page_msg = 'AboutPage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnReturn_clicked(self):
        """
        槽函数
        返回到菜单界面
        Returns:
            None
        """
        page_msg = 'HomePage'
        self.next_page.emit(page_msg)