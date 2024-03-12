try:
    from controller.AbstractController import AbstractController
    from controller.ProbeMemController import MyProbe
except ModuleNotFoundError:
    from qt0922.controller.AbstractController import AbstractController
    from qt0922.controller.ProbeMemController import MyProbe

FAILED_CODE = 404
SUCCEED_CODE = 202


class HomePageController(AbstractController):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

    def startProbeMem(self):
        self.myprobe = MyProbe()
        self.myprobe.update_progress.connect(self.memWarning)
        self.myprobe.finished.connect(lambda: self.myprobe.deleteLater())
        self.myprobe.start()

    def memWarning(self, msg):
        self.update_json.emit(dict(code=msg))