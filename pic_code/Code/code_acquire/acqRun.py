import sys
from PIL import Image
import os
import datetime
import time

import serial
import serial.tools.list_ports

import platform


class Acq_Run:

    def __init__(self):
        self.Core = Acq_Core()

    def Led_init_log(self):
        return True

    def Camera_init_log(self):
        return True

    def img_acquire_log(self, path_chache, path_save, name):
        img = Image.open(path_chache + "1.jpeg")
        img.save(path_save + "%s.jpeg" % name)
        return True


class Acq_Core:

    def __init__(self):
        pass
