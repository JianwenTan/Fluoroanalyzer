"""
@Description：数据下载类
@Author：mysondrink@163.com
@Time：2024/2/27 16:14
"""
from PySide2.QtCore import QThread, Signal, QDateTime
import sys
import traceback
import os
import cv2 as cv
import pandas as pd
import time
import shutil
try:
    import util.frozen as frozen
    from util import dirs
    # from controller.AbstractThread import AbstractThread
    from pic_code.img_main import img_main
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.util import dirs
    # from qt0223.controller.AbstractThread import AbstractThread
    from qt0223.pic_code.img_main import img_main

time_to_sleep = 2
trylock_time = -1
failed_code = 404
succeed_code = 202


class CheckUSBThread(QThread):
    update_json = Signal(int)
    update_log = Signal(str)

    def __init__(self, name, path, data, allergy, parent=None):
        """
        初始化线程
        构造函数
        Args:
            name: 图片名称
            path: 图片路径
            data: 图片数据
            allergy: 试剂卡数据
            parent: 父类
        """
        super().__init__(parent)
        sys.excepthook = self.HandleException
        self.name_pic = name
        self.pic_path = path
        self.data = data
        self.allergy_info = allergy

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

    def run(self):
        """
        u盘下载运行函数
        进行u盘下载
        Returns:
            None
        """
        try:
            self.downLoadToUSB()
        except Exception as e:
            self.sendException()
            self.update_json.emit(failed_code)

    def downLoadToUSB(self):
        """
        下载信息到u盘
        下载内容包括图片、数据库信息
        Returns:
            None
        """
        """
        # 指定目标目录
        target_dir = '/media/orangepi/'
        # 获取U盘设备路径
        try:
            if len(os.listdir(target_dir)) == 0:
                self.update_json.emit(failed_code)
                return
            else:
                u_name = r"/media/orangepi/" + os.listdir(target_dir)[0] + "/"
        except Exception as e:
            print(e)
            self.sendException()
            self.update_json.emit(failed_code)
            return
        try:
            cmd = 'su orangepi -c "cd %s"'%u_name
            flag = os.system(cmd)
            if flag != 0:
                self.update_json.emit(failed_code)
                delete_cmd = 'echo %s | sudo rm -rf %s' % ('orangepi', u_name)
                os.system(delete_cmd)
                return
        except Exception as e:
            print(e)
            self.sendException()
            self.update_json.emit(failed_code)
            return
        # 检查U盘是否已插入
        # timenow = QDateTime.currentDateTime().toString('yyyy-MM-dd')
        timenow = self.data['time'][0]
        save_dir = u_name + timenow + "/"
        dirs.makedir(save_dir)
        # filename = str(int((len(os.listdir(save_dir)) - 1)/2) + 1).zfill(4)
        save_path = save_dir + timenow + ".csv"
        save_path = save_dir + timenow + ".xlsx"
        """
        save_path = '%s/img/%s/%s.xlsx' % (frozen.app_path(), self.pic_path, self.pic_path)
        dirs.makedir(save_path)
        save_dir = save_path
        # save_img_path_1 = save_dir + filename + "-" + self.name_pic + "生成图.jpeg"
        # save_img_path_2 = save_dir + filename + "-" + self.name_pic + "检疫图.jpeg"
        if os.path.exists(save_dir):
            # 在U盘根目录下创建示例文件
            # print(filename + file_name)
            # print("exists")
            # file_path = os.path.join(filename, file_name)
            # with open(save_path, "a") as f:
            #     msg = self.data
            #     f.write(str(msg) + "\n")

            try:
                img_origin = '%s/img/%s/%s-1.jpeg' % (frozen.app_path(), self.pic_path, self.name_pic)
                # shutil.copy(img_origin, save_img_path_1)
                # img_origin = cv.imread('%s/img/%s/%s-1.jpeg' % (frozen.app_path(), self.pic_path, self.name_pic)) # linux
                # flag_bool = cv.imwrite(save_img_path_1, img_origin)

                img_final = '%s/img/%s/%s-2.jpeg' % (frozen.app_path(), self.pic_path, self.name_pic)
                # shutil.copy(img_final, save_img_path_2)
                # img_final = cv.imread('%s/img/%s/%s-2.jpeg' % (frozen.app_path(), self.pic_path, self.name_pic)) # linux
                # flag_bool = cv.imwrite(save_img_path_2, img_final)
            except Exception as e:
                print(e)
                self.sendException()
                self.update_json.emit(failed_code + 1)
                return
            try:
                if os.path.exists(save_path):
                    df2 = pd.read_excel(save_path, sheet_name='Sheet2')
                    row2 = df2.shape[0]  # 获取原数据的行数
                    id_num = row2 + 1
                else:
                    id_num = 1
                id_num = "\t" + str(id_num).zfill(4)
                name_pic = self.name_pic
                test_time = self.data['time']
                cur_time = test_time[0] + ' ' + test_time[1]
                code_num = self.data['code_num']
                doctor = self.data['doctor']
                reagent_type = "检测组合" + self.data['item_type']
                reagent_matrix = self.data['matrix']
                name = self.data['name']
                gender = self.data['gender']
                age = self.data['age']
                reagent_matrix_info = self.allergy_info
                reagent_matrix_info_copy = reagent_matrix_info
                if type(reagent_matrix_info) == str:
                    reagent_matrix_info = reagent_matrix_info.split(',')
                row = reagent_matrix[0]
                col = int(reagent_matrix[2])
                reagent_matrix_info = self.split_string(reagent_matrix_info, col)
                k = ["序号", "图片名称", "时间", "样本条码", "医生", "类别",
                     "阵列", "病人名", "病人性别", "病人年龄", "数据"]
                k_2 = ["序号", "图片名称", "时间", "样本条码", "医生", "类别",
                       "阵列", "病人名", "病人性别", "病人年龄", "数据", "status"]
                status = 0
                v = [id_num, name_pic, cur_time, code_num, doctor, reagent_type,
                     reagent_matrix, name, gender, age, reagent_matrix_info]
                v_2 = [id_num, name_pic, cur_time, code_num, doctor, reagent_type,
                       reagent_matrix, name, gender, age, reagent_matrix_info_copy, status]
                data = dict(zip(k, v))
                data_2 = dict(zip(k_2, v_2))
                dataframe = pd.DataFrame(data)
                datatwo = pd.DataFrame(data_2, index=[0])
                info_data = dataframe['数据'].str.split(',', expand=True)  # 将list数据分割
                dataframe = dataframe[:1].drop(columns='数据')
                newdata = pd.merge(dataframe, info_data, left_index=True, right_index=True, how='outer')
                if os.path.exists(save_path):
                    df1 = pd.read_excel(save_path, sheet_name='Sheet1')
                    row1 = df1.shape[0]  # 获取原数据的行数
                    df2 = pd.read_excel(save_path, sheet_name='Sheet2')
                    row2 = df2.shape[0]  # 获取原数据的行数
                    with pd.ExcelWriter(save_path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                        # 追加
                        newdata.to_excel(writer, sheet_name='Sheet1', index=False, startrow=row1 + 2, header=False)
                        datatwo.to_excel(writer, sheet_name='Sheet2', index=False, startrow=row2 + 1, header=False)
                        writer.book.close()
                    # writer =  pd.ExcelWriter(save_path, mode='a', engine='openpyxl', if_sheet_exists='overlay')
                    # # 追加
                    # newdata.to_excel(writer, sheet_name='Sheet1', index=False, startrow=row1 + 2, header=False)
                    # datatwo.to_excel(writer, sheet_name='Sheet2', index=False, startrow=row2 + 1, header=False)
                    # writer.close()
                else:
                    with pd.ExcelWriter(save_path, mode='w', engine='openpyxl') as writer:
                        # 新建
                        newdata.to_excel(writer, sheet_name='Sheet1', index=False)
                        datatwo.to_excel(writer, sheet_name='Sheet2', index=False, header=k_2)
                        writer.book.close()
                    # writer = pd.ExcelWriter(save_path, mode='w', engine='openpyxl')
                    # # 新建
                    # newdata.to_excel(writer, sheet_name='Sheet1', index=False)
                    # datatwo.to_excel(writer, sheet_name='Sheet2', index=False, header=k_2)
                    # writer.close()
                    # path_usb = save_dir + timenow +".xlsx"
                    # shutil.copy(save_path, path_usb)
                src_path = '%s/res/test.zip' % frozen.app_path()
                identifier = "0xc009d7d1"
                Main = img_main()
                if Main.mountMove(img_origin, save_path, identifier) is not True:
                    raise Exception
                if Main.mountMove(img_final, save_path, identifier) is not True:
                    raise Exception
                if Main.mountMove(src_path, save_path, identifier) is not True:
                    raise Exception
            except Exception as e:
                print(e)
                self.update_json.emit(failed_code)
                return
            self.update_json.emit(succeed_code)
        else:
            self.update_json.emit(failed_code)

    def split_string(self, obj, sec):
        """
        分割字符，将过敏原数据设置为固定形式的二维list
        Args:
            obj: 过敏原数据
            sec: 步长，即二维list的列数

        Returns:
            result： list，分割好的二维list
        """
        result = []
        data = [obj[i:i + sec] for i in range(0, len(obj), sec)]
        num_list = [1, 4, 7, 10]
        for i in range(len(data)):
            _s = ''
            if i in num_list:
                for j in range(len(data[i])):
                    _s += '' + ','
                result.append(_s[:-1])
            else:
                for j in range(len(data[i])):
                    _s += data[i][j] + ','
                result.append(_s[:-1])
        return result