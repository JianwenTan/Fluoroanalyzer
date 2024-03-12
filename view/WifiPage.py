import os
import time
try:
    import util.frozen as frozen
    from view.gui.wifi import *
    from third_party.keyboard.keyboard import KeyBoard
    from util.wifi import wifisearch
    from view.AbstractPage import AbstractPage, ProcessDialog
    from controller.WifiController import WifiThread
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.view.gui.wifi import *
    from qt0922.third_party.keyboard.keyboard import KeyBoard
    from qt0922.util.wifi import wifisearch
    from qt0922.view.AbstractPage import AbstractPage, ProcessDialog
    from qt0922.controller.WifiController import WifiThread


class WifiPage(Ui_Form, AbstractPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self):
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnConfirm.setIconSize(QSize(32, 32))
        self.ui.btnConfirm.setIcon(QIcon(confirm_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

        self.setFocusWidget()
        self.installEvent()
        # self.mytest()

    def getWifiMsg(self, msg):
        if msg == 202:
            # m_title = "确认"
            # m_title = ""
            # m_info = "wifi连接成功，正在进行时间同步"
            # infoMessage(m_info, m_title)
            info = "wifi连接成功，正在进行时间同步"
            self.showInfoDialog(info)
        elif msg == 404:
            self.mywifithread.deleteLater()
            # m_title = "确认"
            # m_title = ""
            # m_info = "wifi连接失败！"
            # infoMessage(m_info, m_title, 280)
            info = "wifi连接失败！"
            self.showInfoDialog(info)
        elif msg == 403:
            self.mywifithread.deleteLater()
            # m_title = "确认"
            # m_title = ""
            # m_info = "时间同步失败！"
            # infoMessage(m_info, m_title, 280)
            info = "时间同步失败！"
            self.showInfoDialog(info)
        elif msg == 203:
            self.mywifithread.deleteLater()
            # m_title = "确认"
            # m_title = ""
            # m_info = "时间同步成功！"
            # infoMessage(m_info, m_title, 280)
            info = "时间同步成功！"
            self.showInfoDialog(info)

    def mytest(self):
        self.ui.wifiCb.addItems(["TPLink","TPLink2023"])

    def installEvent(self):
        for item in self.focuswidget:
            item.installEventFilter(self)

    def setFocusWidget(self):
        self.focuswidget = [self.ui.pwdLine]
        for item in self.focuswidget:
            item.setFocusPolicy(Qt.ClickFocus)

    def eventFilter(self, obj, event):
        if obj in self.focuswidget:
            if event.type() == QEvent.Type.FocusIn:
                # print(obj.setText("hello"))
                self.setKeyBoard(obj)
                return True
            else:
                return False
        else:
            return False

    def setKeyBoard(self, obj):
        self.keyboardtext = KeyBoard()
        self.keyboardtext.text_msg.connect(self.getKeyBoardText)
        obj_name = obj.objectName()
        obj_text = obj.text()
        self.keyboardtext.textInput.setText(obj_text)
        if obj_name == "pwdLine":
            self.keyboardtext.nameLabel.setText("密码")
        self.keyboardtext.showWindow()

    def getKeyBoardText(self, msg):
        self.focusWidget().setText(msg)
        self.focusWidget().clearFocus()

    def setWifiName(self):
        wifi = wifisearch()
        self.wifiName = wifi.getwifiname()
        self.ui.wifiCb.addItems(self.wifiName)

    @Slot()
    def on_btnConfirm_clicked(self):
        try:
            flag = -100
            self.wifiPwd = self.ui.pwdLine.text()
            self.wifiSSID = self.ui.wifiCb.currentText()
            self.mywifithread = WifiThread(self.wifiSSID, self.wifiPwd)
            self.mywifithread.update_json.connect(self.getWifiMsg)
            self.mywifithread.start()
            # self.mywifithread.connectWifi(self.wifiSSID, self.wifiPwd)
            # m_title = ""
            # m_info = "wifi连接中。。。"
            # infoMessage(m_info, m_title, 280)
            info = "wifi连接中。。。"
            dialog = ProcessDialog()
            dialog.setInfo(info)
            dialog.setParent(self)
            dialog.hideBtn()
            dialog.show()
            self.mywifithread.finished.connect(dialog.closeDialog)
            return
            if self.wifiPwd != '':
                cmd_wifi = 'echo %s | sudo nmcli dev wifi connect %s password %s' % (
                'orangepi', self.wifiSSID, self.wifiPwd)
            else:
                cmd_wifi = 'echo %s | sudo nmcli dev wifi connect %s' % ('orangepi', self.wifiSSID)
            result = os.popen(cmd_wifi)
            info = 'Error'
            for i in result:
                flag = i.find(info)
                if flag != -1:
                    break
            if flag == -1:
                m_title = "确认"
                m_title = ""
                m_info = "wifi连接成功！"
                infoMessage(m_info, m_title, 280)
                cmd_date = 'echo %s | sudo ntpdate cn.pool.ntp.org' % ('orangepi')
                os.system(cmd_date)
            else:
                m_title = "确认"
                m_title = ""
                m_info = "wifi连接失败！"
                infoMessage(m_info, m_title, 280)

            time.sleep(1)
        except Exception as e:
            m_title = "确认"
            m_title = ""
            m_info = "wifi连接失败！"
            infoMessage(m_info, m_title, 280)

    @Slot()
    def on_btnReturn_clicked(self):
        page_msg = 'SysPage'
        self.next_page.emit(page_msg)

