import re
import os
try:
    import util.frozen as frozen
except ImportError:
    import qt0922.util.frozen as frozen


class wifisearch():
    def __init__(self) -> object:
        pass

    def getwifiname(self):
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
