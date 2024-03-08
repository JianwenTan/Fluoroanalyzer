"""
@Description：清理存储控制类
@Author：mysondrink@163.com
@Time：2024/2/28 20:31
"""
from PySide2.QtCore import QThread, Signal
try:
    import util.frozen as frozen
    from controller.AbstractThread import AbstractThread
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.controller.AbstractThread import AbstractThread

import os

failed_code = 404
succeed_code = 202


class ClearThread(AbstractThread):
    update_progress = Signal(int)   # progress signal to send memory storage

    def __init__(self, clear_time=None, parent=None):
        """
        初始化线程，构造函数
        Args:
            clear_time: 清除保留的时间
            parent: 父类
        """
        super().__init__()
        self.clear_time = clear_time

    def run(self):
        """
        线程运行函数
        进行系统存储的检测
        检测目录位于img
        Returns:
            None
        """
        pic_path = frozen.app_path() + "/img/"
        root_list = []
        dirs_list = []
        files_list = []
        for root, dirs, files in os.walk(pic_path):
            root_list.append(root)
            dirs_list.append(dirs)
            files_list.append(files)
        if self.clear_time is None:
            self.deletePicFile(pic_path)
        else:
            self.deleteDirs(self.clear_time, root_list)

    def deleteDirs(self, now_time, root_list):
        """
        遍历本地图片文件
        当文件名小于清除保留的时间，进行文件目录的清除
        Args:
            now_time: 清除保留的时间
            root_list: 清除的目录

        Returns:
            None
        """
        for i in range(1, len(root_list)):
            if now_time > root_list[i][-10:]:
                self.deletePicFile(root_list[i])

    def deletePicFile(self, path):
        """
        批量删除目录下的文件
        Args:
            path: 文件目录路径

        Returns:
            None
        """
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                self.deletePicFile(c_path)
            else:
                os.remove(c_path)