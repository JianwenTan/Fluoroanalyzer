"""
@Description：设备信息界面显示
@Author：mysondrink@163.com
@Time：2024/1/11 11:04
"""
# from func.infoPage import infoMessage
import os
import shutil
import sys
import traceback
try:
    import util.frozen as frozen
    from view.gui.about import *
    from view.AbstractPage import AbstractPage, ProcessDialog
    from controller.uploadController import UploadThread
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.view.gui.about import *
    from qt0223.view.AbstractPage import AbstractPage, ProcessDialog
    from qt0223.controller.uploadController import UploadThread

CONFIG_FILE = frozen.app_path() + r"/config/configname.ini"


class AboutPage(Ui_Form, AbstractPage):
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

    """
    @detail u盘上传信息到软件
    @detail 默认上传文件为example.txt，上传内容为6个数字，每个数字各占一行
    """
    def uploadFromUSB(self):
        # 指定目标目录
        target_dir = '/media/xiao/'

        # 获取U盘设备路径
        try:
            filename = r"/media/xiao/" + os.listdir(target_dir)[0]
        except Exception as e:
            m_title = ""
            m_info = "U盘未插入或无法访问！"
            # infoMessage(m_info, m_title, 240)
            return

            # 检查U盘是否已插入
        if os.path.exists(filename):
            # 在U盘根目录下查找指定文件
            file_path = os.path.join(filename, "example.txt")
            if os.path.exists(file_path):
                # 读取文件内容并打印到控制台
                with open(file_path, "r") as f:
                    # print(f.read())
                    m_title = ""
                    m_info = f.read()
                    # infoMessage(m_info, m_title)
            else:
                # print("文件不存在")
                m_title = ""
                m_info = "文件不存在!"
                # infoMessage(m_info, m_title, 300)
        else:
            # print("U盘未插入或无法访问")
            m_title = ""
            m_info = "U盘未插入或无法访问!"
            # infoMessage(m_info, m_title, 240)

    """
    @detail 上传按钮操作
    @detail 槽函数
    """
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
            os.system("sudo mount /dev/sda1 /mnt/mydev")
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
        if not upload_file_list:
            try:
                # self.testinfo.closeWin()
                dialog.closeDialog()
                # m_title = ""
                # m_info = "上传完成!"
                # infoMessage(m_info, m_title, 300)
                info = "上传完成!"
                self.showInfoDialog(info)
                os.system("sudo umount /mnt/mydev")
            except Exception as e:
                print("aboutPage：", e)
            return
        self.upload_thread_list = []
        for i in upload_file_list:
            thread = UploadThread(i)
            self.upload_thread_list.append(thread)
            thread.finished.connect(lambda: thread.deleteLater())
            thread.finished.connect(lambda: self.countUploadThread(dialog))
            thread.start()

    def countUploadThread(self, obj):
        self.count_num = self.count_num + 1
        if len(self.upload_thread_list) <= self.count_num:
            try:
                os.system("sudo umount /mnt/mydev")
            except Exception as e:
                print("aboutPage：", e)
            # self.testinfo.closeWin()
            try:
                obj.closeDialog()
            except Exception as e:
                return
            return


    """
    @detail 返回按钮操作
    @detail 槽函数
    """
    @Slot()
    def on_btnReturn_clicked(self):
        page_msg = 'SysPage'
        self.next_page.emit(page_msg)

    def getData(self):
        pass
