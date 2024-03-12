import time

try:
    import util.frozen as frozen
    from view.gui.register import *
    from third_party.keyboard.keyboard import KeyBoard
    from view.AbstractPage import AbstractPage
    from controller.RegisterController import RegisterController
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.view.gui.register import *
    from qt0922.third_party.keyboard.keyboard import KeyBoard
    from qt0922.view.AbstractPage import AbstractPage
    from qt0922.controller.RegisterController import RegisterController


class RegisterPage(Ui_Form, AbstractPage):
    def __init__(self):

        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()
        self.controller = RegisterController()
        self.controller.update_json.connect(self.getControllerInfo)

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

    def installEvent(self):

        for item in self.focuswidget:
            item.installEventFilter(self)

    def setFocusWidget(self):

        self.focuswidget = [self.ui.nameLine, self.ui.pwdLine, self.ui.pwdLine_2]
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

    def getKeyBoardText(self, msg):

        self.focusWidget().setText(msg)
        self.focusWidget().clearFocus()

    def setKeyBoard(self, obj):
        self.keyboardtext = KeyBoard()
        self.keyboardtext.text_msg.connect(self.getKeyBoardText)
        obj_name = obj.objectName()
        obj_text = obj.text()
        self.keyboardtext.textInput.setText(obj_text)
        if obj_name == "nameLine":
            self.keyboardtext.nameLabel.setText("用户名")
        elif obj_name == "pwdLine":
            self.keyboardtext.nameLabel.setText("新密码")
        else:
            self.keyboardtext.nameLabel.setText("再次输入")
        self.keyboardtext.showWindow()

    def getControllerInfo(self, msg):

        code = msg['code']
        if code == 202:
            info = "注册成功!"
            # self.showInfo(info)
            self.showInfoDialog(info)
            page_msg = 'LoginPage'
            self.next_page.emit(page_msg)
        elif code == 404:
            info = "注册失败!"
            # self.showInfo(info)
            self.showInfoDialog(info)
        return

    def checkName(self):
        if self.ui.pwdLine.text() == "" or self.ui.nameLine.text() == "" or self.ui.pwdLine_2.text() == "" :
            info = "请输入用户名或密码！"
            self.showInfoDialog(info)
        elif self.ui.pwdLine.text() != self.ui.pwdLine_2.text():
            info = "两次输入不正确！"
            self.showInfoDialog(info)
        else:
            name = self.ui.nameLine.text()
            password = self.ui.pwdLine.text()
            self.controller.insertUser(name, password)
        return

    @Slot()
    def on_btnReturn_clicked(self):

        page_msg = 'LoginPage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnConfirm_clicked(self):
        self.checkName()

