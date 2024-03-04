"""
@Description：
@Author：mysondrink@163.com
@Time：2024/2/28 20:09
"""
from PySide2.QtCore import QThread, Signal
import sys
import traceback
import time
import subprocess
import os

time_to_sleep = 2
trylock_time = -1
failed_code = 404
succeed_code = 202


class WifiThread(QThread):
    update_json = Signal(int)
    update_log = Signal(str)

    """
    @detail 初始化线程，同时创建记录异常的信息
    @detail 构造函数
    """
    def __init__(self, wifiSSID, wifiPwd, parent=None):
        super().__init__(parent)
        sys.excepthook = self.HandleException
        self.wifiSSID = wifiSSID
        self.wifiPwd = wifiPwd

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
    @detail 进行摄像头的检测
    """
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