from PySide2.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton, QApplication
from PySide2.QtCore import Qt, QTimer, QProcess, QCoreApplication
from PySide2.QtGui import QPainter, QColor, QPen
try:
    from view.AbstractWidget import AbstractWidget
    from third_party.widget.MaterialProgress import CircleProgressBar
except ModuleNotFoundError:
    from qt0922.view.AbstractWidget import AbstractWidget
    from qt0922.third_party.widget.MaterialProgress import CircleProgressBar


class AbsctractDialog(AbstractWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()
        # self.setTimeClose()

    def __del__(self):
        print(f"delete dialog{self.__class__.__name__}")

    def InitUI(self):
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
        timer = QTimer()
        timer.timeout.connect(lambda: self.close())
        timer.timeout.connect(lambda: timer.stop())
        timer.start(2500)

    def show(self):
        super().show()
        self.raise_()

    def hideDialog(self):
        self.hide()

    def closeDialog(self):
        self.close()

    def hideProgress(self):
        self.progress.hide()

    def showProgress(self):
        self.progress.show()

    def hideBtn(self):
        self.buttonRestart.hide()

    def showButton(self):
        self.buttonRestart.show()

    def setInfo(self, msg):
        self.label.setText(msg)

    def restart_real_live(self):
        import os
        import sys
        app = QApplication.instance()
        app.quit()
        p = QProcess()
        cur_dir = os.path.dirname(sys.argv[0])
        print("cur_dir:", cur_dir)
        p.startDetached(app.applicationFilePath(), [os.path.join(cur_dir, 'main.py')])
