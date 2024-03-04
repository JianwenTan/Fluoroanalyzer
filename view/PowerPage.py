"""
@Description：电源界面显示
@Author：mysondrink@163.com
@Time：2024/1/11 10:30
"""
import os
import time
import sys
import traceback
try:
    import util.frozen as frozen
    from view.gui.power import *
    # from func.infoPage import infoMessage
    from view.AbstractPage import AbstractPage
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.view.gui.power import *
    # from func.infoPage import infoMessage
    from qt0223.view.AbstractPage import AbstractPage

class PowerPage(Ui_Form, AbstractPage):
    next_page = Signal(str)
    update_json = Signal(dict)
    update_log = Signal(str)

    """
    @detail 初始化加载界面信息，同时创建记录异常的信息
    @detail 构造函数
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    """
    @detail 设置界面相关信息
    """
    def InitUI(self):
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setBtnIcon()

    """
    @detail 设置按钮图标
    """
    def setBtnIcon(self):
        shutdown_icon_path = frozen.app_path() + r"/res/icon/shutdown.png"
        pixImg = self.mySetIconSize(shutdown_icon_path)
        self.ui.shutdown_icon_label.setPixmap(pixImg)
        self.ui.shutdown_icon_label.setAlignment(Qt.AlignCenter)

        logout_icon_path = frozen.app_path() + r"/res/icon/logout.png"
        pixImg = self.mySetIconSize(logout_icon_path)
        self.ui.logout_icon_label.setPixmap(pixImg)
        self.ui.logout_icon_label.setAlignment(Qt.AlignCenter)

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

    """
    @detail 设置按钮图标比例
    """
    def mySetIconSize(self, path):
        img = QImage(path)  # 创建图片实例
        mgnWidth = 50
        mgnHeight = 50  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        pixImg = QPixmap.fromImage(
            img.scaled(size, Qt.IgnoreAspectRatio))  # 修改图片实例大小并从QImage实例中生成QPixmap实例以备放入QLabel控件中
        return pixImg

    """
    @detail 返回按钮操作
    @detail 槽函数
    """
    @Slot()
    def on_btnReturn_clicked(self):
        page_msg = 'HomePage'
        self.next_page.emit(page_msg)

    """
    @detail 注销按钮操作
    @detail 槽函数
    """
    @Slot()
    def on_btnLogout_clicked(self):
        page_msg = 'LoginPage'
        self.next_page.emit(page_msg)

    """
    @detail 关机按钮操作
    @detail 槽函数
    """
    @Slot()
    def on_btnShutdown_clicked(self):
        # m_title = "提示"
        # m_title = ""
        # m_info = "请关闭电源！"
        # infoMessage(m_info, m_title, 300)
        info = "请在提示语关闭后关闭电源！"
        self.showInfoDialog(info)
        time.sleep(1)
        return
        # order_str = "sudo shutdown -h now"
        order_str = 'echo %s | sudo %s' % ('orangepi', 'shutdown -h now')
        os.system(order_str)