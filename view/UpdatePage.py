try:
    import util.frozen as frozen
    from view.gui.update import *
    from view.AbstractPage import AbstractPage, ProcessDialog
    from pic_code.img_main import img_main
    from controller.UpdateController import MyUpdateThread
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.view.gui.update import *
    from qt0922.view.AbstractPage import AbstractPage, ProcessDialog
    from qt0922.pic_code.img_main import img_main
    from qt0922.controller.UpdateController import MyUpdateThread


class UpdatePage(Ui_Form, AbstractPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self):
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setBtnIcon()

    def setBtnIcon(self):
        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnConfirm.setIconSize(QSize(32, 32))
        self.ui.btnConfirm.setIcon(QIcon(confirm_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

        logout_icon_path = frozen.app_path() + r"/res/icon/logout.png"
        pixImg = self.mySetIconSize(logout_icon_path)
        self.ui.restart_icon_label.setPixmap(pixImg)
        self.ui.restart_icon_label.setAlignment(Qt.AlignCenter)

    def updateInfo(self, msg):
        src_path = "/mnt/mydev/update.zip"
        identifier = "0xc009d7d1"
        save_path = '/home/orangepi/Desktop/qt0922/update.zip'
        # Main = img_main()
        # if Main.mountMove(src_path, save_path, identifier):
        #     info = "更新成功！请自行重启"
        # else:
        #     info = "更新失败！"
        code = msg['code']
        if code == 202:
            info = "更新成功！请自行重启"
        elif code == 404:
            info = "更新失败！"
        self.showInfoDialog(info)

    @Slot()
    def on_btnReturn_clicked(self):
        page_msg = 'SysPage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnConfirm_clicked(self):
        info = "更新中。。。"
        dialog = ProcessDialog()
        dialog.setInfo(info)
        dialog.setParent(self)
        dialog.hideBtn()
        dialog.show()
        updatethread = MyUpdateThread()
        updatethread.finished.connect(dialog.closeDialog)
        updatethread.update_json.connect(self.updateInfo)
        updatethread.start()

    @Slot()
    def on_btnRestart_clicked(self):
        import os
        import sys
        app = QApplication.instance()
        app.quit()
        p = QProcess()
        cur_dir = os.path.dirname(sys.argv[0])
        print("cur_dir:", cur_dir)
        p.startDetached(app.applicationFilePath(), [os.path.join(cur_dir, 'main.py')])