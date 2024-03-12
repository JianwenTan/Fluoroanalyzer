try:
    import util.frozen as frozen
    from view.gui.login import *
    from third_party.keyboard.keyboard import KeyBoard
    from view.AbstractPage import AbstractPage
    from controller.LoginController import LoginController
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.view.gui.login import *
    from qt0922.third_party.keyboard.keyboard import KeyBoard
    from qt0922.view.AbstractPage import AbstractPage
    from qt0922.controller.LoginController import LoginController

SCREEN_TOP = 30
CONFIG_FILE = frozen.app_path() + r"/config/configname.ini"


class LoginPage(Ui_Form, AbstractPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()
        # self.setUserDict()

    def InitUI(self):

        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setBtnIcon()
        self.mytest()
        self.setFocusWidget()
        self.installEvent()
        self.controller = LoginController()
        self.controller.update_json.connect(self.getControllerInfo)

    def getControllerInfo(self, msg):

        code = msg['code']
        if code == 202:
            page_msg = 'HomePage'
            self.next_page.emit(page_msg)
        elif code == 404:
            info = "用户名或密码错误!"
            # self.update_info.emit(info)
            self.update_info.emit(info)

    def mytest(self):

        self.ui.nameLine.setText("test")
        self.ui.numLine.setText("123456")

    def setBtnIcon(self):
        login_icon_path = frozen.app_path() + r"/res/icon/login.png"
        pixImg = self.mySetIconSize(login_icon_path)
        self.ui.login_icon_label.setPixmap(pixImg)
        self.ui.login_icon_label.setAlignment(Qt.AlignCenter)

        register_icon_path = frozen.app_path() + r"/res/icon/register.png"
        pixImg = self.mySetIconSize(register_icon_path)
        self.ui.register_icon_label.setPixmap(pixImg)
        self.ui.register_icon_label.setAlignment(Qt.AlignCenter)

    def installEvent(self):
        for item in self.focuswidget:
            item.installEventFilter(self)

    def setFocusWidget(self):
        self.focuswidget = [self.ui.nameLine, self.ui.numLine]
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
        if obj_name == "nameLine":
            self.keyboardtext.nameLabel.setText("用户名")
        else:
            self.keyboardtext.nameLabel.setText("密码")
        self.keyboardtext.showWindow()

    def getKeyBoardText(self, msg):
        self.focusWidget().setText(msg)
        self.focusWidget().clearFocus()

    @Slot()
    def on_loginBtn_clicked(self):
        # super().on_loginBtn_clicked()
        # a = 1/0
        if self.ui.nameLine.text() == "" or self.ui.numLine.text() == "":
            info = "用户名或密码未填写！"
            self.update_info.emit(info)
        else:
            # print("send msg")
            # self.update_json.disconnect(self.controller.authUser)
            self.writeUserName()
            self.update_json.connect(self.controller.authUser, Qt.UniqueConnection)
            self.update_json.emit(dict(name=self.ui.nameLine.text(), password=self.ui.numLine.text()))
        return

    @Slot()
    def on_registerBtn_clicked(self):
        # page_msg = registerPage()
        page_msg = 'RegisterPage'
        self.next_page.emit(page_msg)

    def writeUserName(self):
        settings = QSettings(CONFIG_FILE, QSettings.IniFormat)
        settings.setIniCodec("UTF-8")
        settings.setValue("USER/user_name", self.ui.nameLine.text())
