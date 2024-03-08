"""
@Description：登录界面
@Author：mysondrink@163.com
@Time：2024/1/9 17:12
"""
try:
    import util.frozen as frozen
    from view.gui.login import *
    from third_party.keyboard.keyboard import KeyBoard
    from view.AbstractPage import AbstractPage
    from controller.LoginController import LoginController
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.view.gui.login import *
    from qt0223.third_party.keyboard.keyboard import KeyBoard
    from qt0223.view.AbstractPage import AbstractPage
    from qt0223.controller.LoginController import LoginController

SCREEN_TOP = 30


class LoginPage(Ui_Form, AbstractPage):
    def __init__(self):
        """
        构造函数，初始化界面
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()
        # self.setUserDict()

    def InitUI(self):
        """
        设置界面相关信息
        Returns:
            None
        """
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
        """
        获取controller的信息
        Args:
            msg: 返回的信息

        Returns:
            None
        """
        code = msg['code']
        if code == 202:
            page_msg = 'HomePage'
            self.next_page.emit(page_msg)
        elif code == 404:
            info = "用户名或密码错误!"
            # self.update_info.emit(info)
            self.update_info.emit(info)

    def mytest(self):
        """
        测试账号
        Returns:
            None
        """
        self.ui.nameLine.setText("test")
        self.ui.numLine.setText("123456")

    def setBtnIcon(self):
        """
        设置按钮图标
        Returns:
            None
        """
        login_icon_path = frozen.app_path() + r"/res/icon/login.png"
        pixImg = self.mySetIconSize(login_icon_path)
        self.ui.login_icon_label.setPixmap(pixImg)
        self.ui.login_icon_label.setAlignment(Qt.AlignCenter)

        register_icon_path = frozen.app_path() + r"/res/icon/register.png"
        pixImg = self.mySetIconSize(register_icon_path)
        self.ui.register_icon_label.setPixmap(pixImg)
        self.ui.register_icon_label.setAlignment(Qt.AlignCenter)

    def installEvent(self):
        """
        安装事件监听
        Returns:
            None
        """
        for item in self.focuswidget:
            item.installEventFilter(self)

    def setFocusWidget(self):
        """
        设置组件点击焦点
        Returns:
            None
        """
        self.focuswidget = [self.ui.nameLine, self.ui.numLine]
        for item in self.focuswidget:
            item.setFocusPolicy(Qt.ClickFocus)

    def eventFilter(self, obj, event):
        """
        槽函数
        事件过滤
        Args:
            obj: 发生事件的组件
            event: 发生的事件

        Returns:
            bool: 处理掉事件
        """
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
        """
        槽函数
        设置可以键盘弹出的组件
        Args:
            obj: 键盘弹出的组件

        Returns:
            None
        """
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
        """
        槽函数
        获取键盘的文本信息
        Args:
            msg: 信号，键盘文本信息

        Returns:
            None
        """
        self.focusWidget().setText(msg)
        self.focusWidget().clearFocus()

    @Slot()
    def on_loginBtn_clicked(self):
        """
        槽函数
        登录按钮操作，对用户信息进行简单判断
        Returns:
            None
        """
        # super().on_loginBtn_clicked()
        # a = 1/0
        if self.ui.nameLine.text() == "" or self.ui.numLine.text() == "":
            info = "用户名或密码未填写！"
            self.update_info.emit(info)
        else:
            # print("send msg")
            # self.update_json.disconnect(self.controller.authUser)
            self.update_json.connect(self.controller.authUser, Qt.UniqueConnection)
            self.update_json.emit(dict(name=self.ui.nameLine.text(), password=self.ui.numLine.text()))
        return

    @Slot()
    def on_registerBtn_clicked(self):
        """
        槽函数
        注册按钮槽函数，跳转到注册界面
        Returns:
            None
        """
        # page_msg = registerPage()
        page_msg = 'RegisterPage'
        self.next_page.emit(page_msg)
