"""
@Description：数据上传类
@Author：mysondrink@163.com
@Time：2024/2/27 16:14
"""
from PySide2.QtCore import QThread, Signal
import pandas as pd
import numpy as np
import os
import time
try:
    import util.frozen as frozen
    from controller.AbstractThread import AbstractThread
    import middleware.database as insertdb
except:
    import qt0223.util.frozen as frozen
    from qt0223.controller.AbstractThread import AbstractThread
    import qt0223.middleware.database as insertdb


time_to_sleep = 2
trylock_time = -1
failed_code = 404
succeed_code = 202
SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'


class UploadThread(AbstractThread):
    finished = Signal()

    def __init__(self, file_path='./res/new_data.xlsx'):
        """
        构造函数
        初始化线程，调用父类方法进行日志记录
        Args:
            file_path: 上传文件的路径
        """
        super().__init__()
        self.file_path = file_path

    def run(self):
        """
        读取文件，将文件中的数据分离处理
        Returns:
            None
        """
        csv_data = []
        id_data = []
        reagent_data = []
        status_data = []
        input_table = pd.read_excel(self.file_path, sheet_name="Sheet2")
        input_table_rows = input_table.shape[0]
        # input_table_columns = input_table.shape[1]
        # input_table_header = input_table.columns.values.tolist()
        for i in range(input_table_rows):
            input_table_rows_values = input_table.iloc[[i]]
            input_table_rows_values_array = np.array(input_table_rows_values)
            input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
            csv_data.append(input_table_rows_values_list)
            id_data.append(input_table_rows_values_list[1])
            reagent_data.append(input_table_rows_values_list[-2])
            status_data.append(input_table_rows_values_list[-1])
        self.insertMysql(id_data, status_data, *self.filterReagentData(reagent_data))
        # ["序号", "图片名称", "时间", "样本条码", "医生", "类别",
        #  "阵列", "病人名", "病人性别", "病人年龄", "数据", "status"]
        # [id_num, name_pic, cur_time, code_num, doctor, reagent_type,
        #  reagent_matrix, name, gender, age, reagent_matrix_info]

    def filterReagentData(self, data):
        """
        过滤过敏原数据
        Args:
            data: 需要过滤的过敏原数据

        Returns:
            reagent_info_list: 过敏原数据
            points_list: 定位点数据
            gray_aver_list: 像素点数据
        """
        reagent_info_list = []
        points_list = []
        gray_aver_list = []
        for i in data:
            temp = i.split(",")
            points_list.append(",".join(i for i in temp[0:5]))
            reagent_info_list.append(",".join(i for i in temp[5:]))
            b = temp[10:]
            c = [b[k:k+10] for k in [j for j in range(0, 55, 15)]]
            str_list = []
            for j in [i for i in c]:
                str_list = str_list + [i for i in j]
            gray_aver_list.append(",".join(str_list))
        return reagent_info_list, points_list, gray_aver_list

    def insertMysql(self, id_list, status_list, reagent_info_list, points_list, gray_aver_list):
        """
        进行数据更新
        根据照片名进行数据的更新
        Args:
            id_list: 照片名
            status_list: status状态list
            reagent_info_list: 过敏原数据
            points_list: 定位点数据
            gray_aver_list: 像素点数据

        Returns:
            None
        """
        sum = insertdb.insertMySql(id_list, status_list, reagent_info_list, points_list, gray_aver_list)
        print('新增' + str(sum) + "数据")
        time.sleep(0.5)
        self.deleteFile()
        self.finished.emit()

    def deleteFile(self):
        """
        数据更新完后，删除更新文件
        Returns:
            None
        """
        os.remove(self.file_path)

