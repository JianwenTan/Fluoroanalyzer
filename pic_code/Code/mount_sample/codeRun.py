import sys
import os

sys.path.append(os.path.dirname(__file__))

from Code.mount_sample.mount import Mount_move


class mount(object):

    def __init__(self):
        self.mount = Mount_move()

    def mount(self, original, final, identifier):
        RunFlag = self.mount.Move(original, final, identifier)
        return RunFlag
