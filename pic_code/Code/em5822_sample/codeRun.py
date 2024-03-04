import sys
import os

# sys.path.append(os.path.dirname(__file__))

from Code.em5822_sample.Em5822 import Em5822_out

class em5822(object):

    def __init__(self):
        self.em = Em5822_out()
        pass

    def emInit(self):
        RunFlag = self.em.em5822_init()
        return RunFlag

    def emPrint(self, Base, Nature, Data_Light):
        RunFlag = self.em.em5822_out(Base, Nature, Data_Light)
        return RunFlag
