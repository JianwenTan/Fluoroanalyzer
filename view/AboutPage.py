import os
try:
    import util.frozen as frozen
    from view.gui.about import *
    from view.AbstractPage import AbstractPage, ProcessDialog
    from controller.uploadController import UploadThread
    from pic_code.img_main import img_main
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.view.gui.about import *
    from qt0922.view.AbstractPage import AbstractPage, ProcessDialog
    from qt0922.controller.uploadController import UploadThread
    from qt0922.pic_code.img_main import img_main

CONFIG_FILE = frozen.app_path() + r"/config/configname.ini"


class AboutPage(Ui_Form, AbstractPage):
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

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnUpload.setIconSize(QSize(32, 32))
        self.ui.btnUpload.setIcon(QIcon(confirm_icon_path))

        settings = QSettings(CONFIG_FILE, QSettings.IniFormat)
        settings.setIniCodec("UTF-8")
        self.ui.label_2.setText(settings.value("MACHINE/machine_name"))
        self.ui.label_36.setText(settings.value("MACHINE/machine_mode"))

    @Slot()
    def on_btnUpload_clicked(self):
        # self.testinfo = MyTestInfo()
        info = "数据上传中。。。"
        dialog = ProcessDialog()
        dialog.setInfo(info)
        dialog.setParent(self)
        dialog.hideBtn()
        dialog.show()

        """
        # 指定目标目录
        target_dir = '/media/orangepi/'
        # target_dir = '/media/xiao/'
        # 获取U盘设备路径
        try:
            if len(os.listdir(target_dir)) == 0:
                self.update_json.emit(failed_code)
                return
            else:
                u_name = r"/media/orangepi/" + os.listdir(target_dir)[0] + "/"
        except Exception as e:
            print(e)
            self.sendException()
            self.update_json.emit(failed_code)
            return
        try:
            cmd = 'su orangepi -c "cd %s"' % u_name
            flag = os.system(cmd)
            if flag != 0:
                self.update_json.emit(failed_code)
                delete_cmd = 'echo %s | sudo rm -rf %s' % ('orangepi', u_name)
                os.system(delete_cmd)
                return
        except Exception as e:
            print(e)
            self.sendException()
            self.update_json.emit(failed_code)
            return
        """
        try:
            Main = img_main()
            identifier = "0xb7d60506"
            flag = img_main.mountMove("1", "1", identifier)
            if flag is not True:
                raise
        except Exception as e:
            print("aboutPage :", e)
            return False
        u_name = "/mnt/mydev/"
        dir_list = os.listdir(u_name)
        upload_file_list = []
        for i in dir_list:
            path = u_name + i + "/new_data.xlsx"
            print(path)
            if os.path.exists(path):
                print("True")
                upload_file_list.append(path)
            else:
                print("False")
                dialog.closeDialog()
                # m_title = ""
                # m_info = "上传完成!"
                # infoMessage(m_info, m_title, 300)
                info = "上传失败!"
                self.showInfoDialog(info)
                self.umountDevice(Main)
        if not upload_file_list:
            try:
                # self.testinfo.closeWin()
                dialog.closeDialog()
                # m_title = ""
                # m_info = "上传完成!"
                # infoMessage(m_info, m_title, 300)
                info = "上传完成!"
                self.showInfoDialog(info)
                self.umountDevice(Main)
            except Exception as e:
                print("aboutPage：", e)
            return
        self.upload_thread_list = []
        for i in upload_file_list:
            thread = UploadThread(i)
            self.upload_thread_list.append(thread)
            thread.finished.connect(lambda: thread.deleteLater())
            thread.finished.connect(lambda: self.countUploadThread(dialog, Main))
            thread.start()

    def countUploadThread(self, obj, func):
        self.count_num = self.count_num + 1
        if len(self.upload_thread_list) <= self.count_num:
            try:
                if func is not None:
                    pass
                else:
                    self.umountDevice(func)
            except Exception as e:
                print("aboutPage：", e)
            # self.testinfo.closeWin()
            try:
                obj.closeDialog()
            except Exception as e:
                return
            return

    @Slot()
    def on_btnReturn_clicked(self):
        page_msg = 'SysPage'
        self.next_page.emit(page_msg)

    def getData(self):
        pass

    def umountDevice(self, obj):
        identifier = "0xb7d60506"
        flag = obj.mountMove("2", "1", identifier)
        if flag is not True:
                raise