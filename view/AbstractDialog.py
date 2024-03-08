"""
@Description：信息提示抽象类
@Author：mysondrink@163.com
@Time：2024/1/8 17:14
"""
from PySide2.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton, QApplication
from PySide2.QtCore import Qt, QTimer, QProcess, QCoreApplication
from PySide2.QtGui import QPainter, QColor, QPen
try:
    from view.AbstractWidget import AbstractWidget
    from third_party.widget.MaterialProgress import CircleProgressBar
except ModuleNotFoundError:
    from qt0223.view.AbstractWidget import AbstractWidget
    from qt0223.third_party.widget.MaterialProgress import CircleProgressBar


class AbsctractDialog(AbstractWidget):
    def __init__(self):
        """
        构造函数，初始化日志类
        """
        super().__init__()
        self.InitUI()
        # self.setTimeClose()

    def __del__(self):
        """
        析构函数，打印类名
        """
        print(f"delete dialog{self.__class__.__name__}")

    def InitUI(self):
        """
        界面初始化
        Returns:
            None
        """
        self.resize(800, 480)
        # self.setWindowOpacity(0.5)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        canvas = QWidget()
        canvas.setObjectName("canvas")

        canvas.setStyleSheet(
            "QWidget { background: #05abc2; font: 20pt \"\u5e7c\u5706\"; border:4px solid rgb(0,0,0);}")
        # canvas.setStyleSheet("#canvas { background: #05abc2; font: 20pt \"\u5e7c\u5706\"; }")
        layout = QVBoxLayout()
        layout_1 = QVBoxLayout()
        canvas.setLayout(layout_1)
        canvas.setMinimumHeight(100)
        canvas.setMaximumWidth(800)
        layout.addWidget(canvas)
        self.label = QLabel()
        # self.setInfo("hello world")
        self.progress = CircleProgressBar()
        self.buttonRestart = QPushButton()
        btnStyleSheet = "QPushButton { " \
                        "font: 20pt \"\u5e7c\u5706\"; " \
                        "border:4px solid rgb(0,0,0); " \
                        "background-color:#05abc2; " \
                        "border-radius: 35px; } " \
                        "QPushButton:pressed{ " \
                        "background-color: rgb(255, 0, 0); }"
        self.buttonRestart.setText("软件重启")
        self.buttonRestart.setFixedSize(140, 80)
        self.buttonRestart.setStyleSheet(btnStyleSheet)
        self.buttonRestart.clicked.connect(self.restart_real_live)
        layout_1.addWidget(self.label)
        # desk = QApplication.desktop()
        # wd = desk.width()
        # ht = desk.height()
        # canvas.move(100, 100)
        # canvas.move((wd - canvas.width()) / 2, (ht - canvas.height()) / 2)
        layout.setContentsMargins(0, 0, 0, 0)
        layout_1.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.progress)
        layout.addWidget(self.buttonRestart)

        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

    def paintEvent(self, event):
        """
        绘制对话框的底色
        Args:
            event: 事件

        Returns:
            None
        """
        # QPainter p(this);
        # // 边框黑色不透明 （因为设置了窗体无边框，这行代码可能没有效果）
        # p.setPen(QColor(0, 255, 0, 255));
        # p.setBrush(QColor(255, 0, 0, 150)); // 填充红色半透明
        # p.drawRect(this->rect()); // 绘制半透明矩形，覆盖整个窗体
        # QWidget::paintEvent(event);
        pen = QPainter(self)
        # pen.setPen(QColor(0, 255, 0, 255))
        pen.setRenderHint(QPainter.Antialiasing)
        pen.setPen(QPen(Qt.NoPen))
        pen.setBrush(QColor(255, 255, 255, 150))
        pen.drawRect(self.rect())

    # def mouseDoubleClickEvent(self, event) -> None:
    #     self.setParent(None)
    #     self.close()

    def setTimeClose(self):
        """
        设置定时器关闭
        Returns:
            None
        """
        timer = QTimer()
        timer.timeout.connect(lambda: self.close())
        timer.timeout.connect(lambda: timer.stop())
        timer.start(2500)

    def show(self):
        """
        打开对话框
        Returns:
            None
        """
        super().show()
        self.raise_()

    def hideDialog(self):
        """
        隐藏对话框
        Returns:
            None
        """
        self.hide()

    def closeDialog(self):
        """
        关闭对话框
        Returns:
            None
        """
        self.close()

    def hideProgress(self):
        """
        隐藏进度条
        Returns:
            None
        """
        self.progress.hide()

    def showProgress(self):
        """
        展示进度条
        Returns:
            None
        """
        self.progress.show()

    def hideBtn(self):
        """
        隐藏重启按钮
        Returns:
            None
        """
        self.buttonRestart.hide()

    def showButton(self):
        """
        显示重启按钮
        Returns:
            None
        """
        self.buttonRestart.show()

    def setInfo(self, msg):
        """
        设置提示框内容
        Args:
            msg: 提示框内容

        Returns:
            None
        """
        self.label.setText(msg)

    def restart_real_live(self):
        """
        进程控制实现自动重启

        :return: None
        """
        import os
        import sys
        app = QApplication.instance()
        app.quit()
        p = QProcess()
        cur_dir = os.path.dirname(sys.argv[0])
        print("cur_dir:", cur_dir)
        p.startDetached(app.applicationFilePath(), [os.path.join(cur_dir, 'main.py')])
