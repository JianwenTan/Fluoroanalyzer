"""
@Description：wifi获取
@Author：mysondrink@163.com
@Time：2024/1/8 16:29
"""
import re
import os
try:
    import util.frozen as frozen
except ImportError:
    import qt0223.util.frozen as frozen


# 连接wifi网络
class wifisearch():
    def __init__(self) -> object:
        """
        构造函数
        Returns:
            object: wifi类
        """
        pass

    def getwifiname(self):
        """
        获取wifi名str列表
        Returns:
            list[str]: wifi名list
        """
        wifipath = frozen.app_path() + '/res/wifi.ini'
        # cmd_on_wifi = 'sudo nmcli r wifi on'
        # cmd_search_wifi = 'sudo nmcli dev wifi > %s'%wifipath
        cmd_on_wifi = 'echo %s | sudo nmcli r wifi on' % ('orangepi')
        cmd_search_wifi = 'echo %s | sudo nmcli dev wifi > %s' % ("orangepi", wifipath)
        os.system(cmd_on_wifi)
        os.system(cmd_search_wifi)

        f = open(wifipath, 'r', encoding="utf-8")
        lines = f.readlines()
        wifiFlag = 'SSID'
        modeFlag = 'MODE'
        wifiFind = re.finditer(wifiFlag, lines[0])
        wifiList = []
        for router in wifiFind:
            wifiList.append(router.span())

        wifiIndex = wifiList[1][0]
        modeIndex = lines[0].find(modeFlag)
        flen = len(lines)

        wifiName = []
        for i in range(1, flen):
            line = lines[i]
            wifiName.append(line[wifiIndex:modeIndex].rstrip())
            # print(wifiName)
        return wifiName
