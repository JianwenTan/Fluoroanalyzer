import sys
import os

sys.path.append(os.path.dirname(__file__))

from Code.img_sample.imgProcess import Img_run
from Code.img_sample.imgAcquire import Acq_Run


class img(object):

    def __init__(self):
        self.imgP = Img_run()
        self.imgA = Acq_Run()
        pass

    def ledInit(self):
        RunFlag = self.imgA.Led_init()
        return RunFlag

    def camInit(self):
        RunFlag = self.imgA.Camera_init()
        return RunFlag

    def imgAcq(self, path_cache, path_save, name):
        RunFlag = self.imgA.img_acquire(path_cache, path_save, name)
        return RunFlag

    def imgPro(self, path_read, path_write, combina, radius):
        RunFlag = self.imgP.process(path_read, path_write, combina, radius)
        return RunFlag
