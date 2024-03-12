from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QImage, QPixmap
try:
    from view.AbstractWidget import AbstractWidget
    from view.AbstractDialog import AbsctractDialog
except ModuleNotFoundError:
    from qt0922.view.AbstractWidget import AbstractWidget
    from qt0922.view.AbstractDialog import AbsctractDialog


class ProcessDialog(AbsctractDialog):
    def __init__(self):
        super().__init__()

    def mouseDoubleClickEvent(self, msg):
        pass


class ErrorDialog(AbsctractDialog):
    def __init__(self):
        super().__init__()

    def mouseDoubleClickEvent(self, msg):
        pass


class AbstractPage(AbstractWidget):
    def __init__(self):
        super().__init__()
        self.update_info.connect(self.showInfoDialog)
        # self.update_log.connect(self.showErrorDialog)

    def mySetIconSize(self, path) -> QPixmap:
        img = QImage(path)  
        mgnWidth = 50
        mgnHeight = 50  
        size = QSize(mgnWidth, mgnHeight)
        pixImg = QPixmap.fromImage(
            img.scaled(size, Qt.IgnoreAspectRatio))
        return pixImg

    def showInfoDialog(self, msg):
        dialog = AbsctractDialog()
        dialog.setInfo(msg)
        dialog.setParent(self)
        dialog.hideProgress()
        dialog.hideBtn()
        dialog.setTimeClose()
        dialog.show()

    def showErrorDialog(self):
        info = "系统错误"
        try:
            print(info + " from ", self._s.currentWidget())
        except AttributeError:
            print(info + " from ", self.objectName())
        # self.showInfoDialog(info)
        dialog = ErrorDialog()
        dialog.setInfo(info)
        dialog.setParent(self)
        dialog.hideProgress()
        dialog.show()