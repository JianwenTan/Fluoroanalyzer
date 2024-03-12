from PySide2.QtCore import QThread, Signal
try:
    import util.frozen as frozen
    from controller.AbstractThread import AbstractThread
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.controller.AbstractThread import AbstractThread

import os

failed_code = 404
succeed_code = 202


class ClearThread(AbstractThread):
    update_progress = Signal(int)   

    def __init__(self, clear_time=None, parent=None):
        super().__init__()
        self.clear_time = clear_time

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

    def deleteDirs(self, now_time, root_list):
        for i in range(1, len(root_list)):
            if now_time > root_list[i][-10:]:
                self.deletePicFile(root_list[i])

    def deletePicFile(self, path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                self.deletePicFile(c_path)
            else:
                os.remove(c_path)