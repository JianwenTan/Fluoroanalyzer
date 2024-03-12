from PySide2.QtCore import QThread, Signal
import subprocess
import os
try:
    from controller.AbstractThread import AbstractThread
except ModuleNotFoundError:
    from qt0922.controller.AbstractThread import AbstractThread

time_to_sleep = 2
trylock_time = -1
failed_code = 404
succeed_code = 202


class WifiThread(AbstractThread):
    update_json = Signal(int)

    def __init__(self, wifiSSID, wifiPwd, parent=None):
        super().__init__()
        self.wifiSSID = wifiSSID
        self.wifiPwd = wifiPwd

    def run(self):
        try:
            print("wifi connecting")
            self.connectWifi(self.wifiSSID, self.wifiPwd)
        except Exception as e:
            self.sendException()

    def connectWifi(self, wifiSSID, wifiPwd):
        try:
            if len(wifiPwd) != 0:
                cmd_wifi = 'echo %s | sudo nmcli dev wifi connect %s password %s' % (
                    'orangepi', wifiSSID, wifiPwd)
            else:
                cmd_wifi = 'echo %s | sudo nmcli dev wifi connect %s' % ('orangepi', wifiSSID)
            result = os.popen(cmd_wifi)
            info = 'Error'
            for i in result:
                flag = i.find(info)
                if flag != -1:
                    break
            if flag == -1:
                self.update_json.emit(succeed_code)
                cmd_date = 'echo %s | sudo ntpdate cn.pool.ntp.org' % ('orangepi')
                result = subprocess.Popen(cmd_date, shell=True)
                p = result.wait()
                if p == 0:
                    self.update_json.emit(203)
                    return
                else:
                    self.update_json.emit(403)
                    return
            else:
                self.update_json.emit(failed_code)
                return
        except Exception as e:
            self.update_json.emit(404)
            self.sendException()