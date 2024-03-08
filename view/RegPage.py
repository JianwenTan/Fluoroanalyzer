"""
@Description：仪器设置类
@Author：mysondrink@163.com
@Time：2024/2/28 10:15
"""
try:
    import util.frozen as frozen
    from view.gui.reg import *
    from view.AbstractPage import AbstractPage, ProcessDialog
    from third_party.keyboard.keyboard import KeyBoard
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.view.gui.reg import *
    from qt0223.view.AbstractPage import AbstractPage, ProcessDialog
    from qt0223.third_party.keyboard.keyboard import KeyBoard

CONFIG_FILE = frozen.app_path() + r"/config/configname.ini"


class RegPage(Ui_Form, AbstractPage):
    def __init__(self):
        """
        仪器设置界面，进行仪器名和型号的命名设置
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
        self.setBtnIcon()
        self.setFocusWidget()
        self.installEvent()
        settings = QSettings(CONFIG_FILE, QSettings.IniFormat)
        settings.setIniCodec("UTF-8")
        self.ui.nameLine.setText(settings.value("MACHINE/machine_name"))
        self.ui.modeLine.setText(settings.value("MACHINE/machine_mode"))
        self.ui.serialLine.setText(settings.value("MACHINE/machine_serial"))

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
        self.focuswidget = [self.ui.nameLine, self.ui.modeLine, self.ui.serialLine]
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
            self.keyboardtext.nameLabel.setText("仪器名称")
        elif obj_name == "modeLine":
            self.keyboardtext.nameLabel.setText("仪器型号")
        elif obj_name == "serialLine":
            self.keyboardtext.nameLabel.setText("仪器批号")
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

    def setBtnIcon(self):
        """
        设置按钮图标
        Returns:
            None
        """
        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnConfirm.setIconSize(QSize(32, 32))
        self.ui.btnConfirm.setIcon(QIcon(confirm_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

    @Slot()
    def on_btnReturn_clicked(self):
        """
        槽函数
        返回按钮返回到菜单界面
        Returns:
            None
        """
        page_msg = 'HomePage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnConfirm_clicked(self):
        """
        槽函数
        确认按钮保存仪器设置
        Returns:
            None
        """
        info = "修改中。。。"
        dialog = ProcessDialog()
        dialog.setInfo(info)
        dialog.setParent(self)
        dialog.hideBtn()
        dialog.show()
        settings = QSettings(CONFIG_FILE, QSettings.IniFormat)
        settings.setIniCodec("UTF-8")
        settings.setValue("MACHINE/machine_name", self.ui.nameLine.text())
        settings.setValue("MACHINE/machine_mode", self.ui.modeLine.text())
        settings.setValue("MACHINE/machine_serial", self.ui.serialLine.text())
        dialog.closeDialog()
        info = "修改成功！"
        self.showInfoDialog(info)