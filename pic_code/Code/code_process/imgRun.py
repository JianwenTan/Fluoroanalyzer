import datetime
import random

import numpy as np
import cv2 as cv
import os
import sys
import time
import platform


class Img_run:

    def __init__(self):
        pass

    def process_log(self, path_read, path_write, combina, radius):
        #   参数设置
        gray_aver = np.zeros((9, 5), dtype=int)  # 发光值输出矩阵
        nature_aver = np.zeros((9, 5), dtype=int)  # 过敏原输出矩阵
        nature_aver = nature_aver.astype(str)

        for i in range(len(gray_aver)):
            for j in range(len(gray_aver[0])):
                gray_aver[i][j] = random.randint(1, 999999)

        nat = ["阴性", "弱阳性", "中阳性", "强阳性"]

        for i in range(len(nature_aver)):
            for j in range(len(nature_aver[0])):
                nature_aver[i][j] = nat[random.randint(0, 3)]

        img = cv.cvtColor(cv.imread(path_read), cv.COLOR_RGB2GRAY)
        #   保存最终图像
        cv.imwrite(path_write + 'img_0ori.jpeg', img)
        cv.imwrite(path_write + 'img_final.jpeg', img)

        return True, gray_aver, nature_aver
