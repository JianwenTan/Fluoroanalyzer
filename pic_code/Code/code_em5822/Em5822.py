import random
import datetime
import numpy as np
import serial
import serial.tools.list_ports
import os
import sys
import time
import platform

out = ['0'] * 100


class Em5822_out:
    def __init__(self):
        pass

    def em5822_init_log(self):
        return True

    def em5822_out_log(self, Base, Nature, Data_Light):
        if not len(Base) == 7:
            return False
        if (len(Nature) != 9) or (len(Nature[0]) != 5):
            return False
        if (len(Data_Light) != 9) or ( len(Data_Light[0]) != 5):
            return False
        return True
