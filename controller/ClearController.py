"""
@Description：
@Author：mysondrink@163.com
@Time：2024/2/28 20:31
"""
from PySide2.QtCore import QThread, Signal
import sys
import traceback
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
    update_progress = Signal(int)
    update_log = Signal(str)

    """
    @detail 初始化线程，同时创建记录异常的信息
    @detail 构造函数
    """
    def __init__(self, clear_time=None, parent=None):
        super().__init__(parent)
        sys.excepthook = self.HandleException
        self.clear_time = clear_time

    """
    @detail 捕获及输出异常类
    @param excType: 异常类型
    @param excValue: 异常对象
    @param tb: 异常的trace back
    """
    def HandleException(self, excType, excValue, tb):
        sys.__excepthook__(excType, excValue, tb)
        err_msg = ''.join(traceback.format_exception(excType, excValue, tb))
        self.update_log.emit(err_msg)

    """
    @detail 发送异常信息
    @detail 在正常抛出异常时使用
    @detail 未使用
    """
    def sendException(self):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        self.update_log.emit(err_msg)

    """
    @detail 线程运行函数
    @detail 进行系统存储的检测
    """
    def run(self):
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

    """
    @detail 遍历本地图片文件
    """
    def deleteDirs(self, now_time, root_list):
        for i in range(1, len(root_list)):
            if now_time > root_list[i][-10:]:
                self.deletePicFile(root_list[i])

    """
    @detail 批量删除文件
    """
    def deletePicFile(self, path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                self.deletePicFile(c_path)
            else:
                os.remove(c_path)