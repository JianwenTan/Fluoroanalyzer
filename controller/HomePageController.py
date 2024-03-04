"""
@Description：菜单页面控制类
@Author：mysondrink@163.com
@Time：2024/1/15 16:03
"""
try:
    from controller.AbstractController import AbstractController
    from controller.ProbeMemController import MyProbe
except ModuleNotFoundError:
    from qt0223.controller.AbstractController import AbstractController
    from qt0223.controller.ProbeMemController import MyProbe

FAILED_CODE = 404
SUCCEED_CODE = 202


class HomePageController(AbstractController):
    def __init__(self):
        """
        构造函数
        Returns:

        """
        super().__init__()

    def __del__(self):
        """
        析构函数
        """
        super().__del__()

    def startProbeMem(self) -> None:
        """
        开始存储探测
        Returns:
            None
        """
        self.myprobe = MyProbe()
        self.myprobe.update_progress.connect(self.memWarning)
        self.myprobe.finished.connect(lambda: self.myprobe.deleteLater())
        self.myprobe.start()

    def memWarning(self, msg) -> None:
        """
        存储满后警告
        Args:
            msg: 线程检测结果

        Returns:
            None
        """
        self.update_json.emit(dict(code=msg))