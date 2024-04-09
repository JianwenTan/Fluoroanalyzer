from PySide2.QtCore import Signal
import os
import cv2 as cv
import pandas as pd
import time
import shutil
try:
    import util.frozen as frozen
    from util import dirs
    from controller.AbstractThread import AbstractThread
    from pic_code.img_main import img_main
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.util import dirs
    from qt0922.controller.AbstractThread import AbstractThread
    from qt0922.pic_code.img_main import img_main

time_to_sleep = 2
trylock_time = -1
failed_code = 404
succeed_code = 202


class CheckUSBThread(AbstractThread):
    update_json = Signal(int)

    def __init__(self, name, path, data, allergy):
        super().__init__()
        self.name_pic = name
        self.pic_path = path
        self.data = data
        self.allergy_info = allergy

    def run(self):
        try:
            self.downLoadToUSB()
        except Exception as e:
            self.sendException()
            self.update_json.emit(failed_code)

    def downLoadToUSB(self):
        move_picture_flag = True
        save_path = '%s/img/%s/%s.xlsx' % (frozen.app_path(), self.pic_path, self.pic_path)
        dirs.makedir(save_path)
        save_dir = '%s/img/%s/' % (frozen.app_path(), self.pic_path)
        move_picture_flag = True
        cache_path = '%s/cache/picture/' % frozen.app_path()
        dirs.makedir(cache_path)
        if os.path.exists(save_dir):
            try:
                img_origin = '%s/img/%s/%s-1.jpeg' % (frozen.app_path(), self.pic_path, self.name_pic)
                save_img_path_1 = '%s/cache/picture/%s' % (frozen.app_path(), self.name_pic + "生成图.jpeg")
                shutil.copy(img_origin, save_img_path_1)

                img_final = '%s/img/%s/%s-2.jpeg' % (frozen.app_path(), self.pic_path, self.name_pic)
                save_img_path_2 = '%s/cache/picture/%s' % (frozen.app_path(), self.name_pic + "检疫图.jpeg")
                shutil.copy(img_final, save_img_path_2)
            except Exception as e:
                # print(e)
                # self.sendException()
                # self.update_json.emit(failed_code + 1)
                # return
                move_picture_flag = False
            try:
                if os.path.exists(save_path):
                    try :
                        df2 = pd.read_excel(save_path, sheet_name='Sheet2')
                        row2 = df2.shape[0]  # 获取原数据的行数
                        id_num = row2 + 1
                    except Exception as e:
                        os.remove(save_path)
                        id_num = 1
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
                    df1 = pd.read_excel(save_path, engine='openpyxl', sheet_name='Sheet1')
                    row1 = df1.shape[0]  # 获取原数据的行数
                    df2 = pd.read_excel(save_path, engine='openpyxl', sheet_name='Sheet2')
                    row2 = df2.shape[0]  # 获取原数据的行数
                    with pd.ExcelWriter(save_path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                        # 追加
                        newdata.to_excel(writer, sheet_name='Sheet1', index=False, startrow=row1 + 2, header=False)
                        datatwo.to_excel(writer, sheet_name='Sheet2', index=False, startrow=row2 + 1, header=False)
                else:
                    with pd.ExcelWriter(save_path, mode='w', engine='openpyxl') as writer:
                        # 新建
                        newdata.to_excel(writer, sheet_name='Sheet1', index=False)
                        datatwo.to_excel(writer, sheet_name='Sheet2', index=False, header=k_2)
                src_path = '%s/res/test.zip' % frozen.app_path()
                identifier = "0xb7d60506"
                Main = img_main()
                save_usb_path = "/mnt/mydev/%s/" % self.pic_path
                save_usb_path = "/mnt/mydev/"
                if move_picture_flag:
                    # if Main.mountMove(img_origin, save_usb_path, identifier) is not True:
                    #     raise Exception
                    # if Main.mountMove(img_final, save_usb_path, identifier) is not True:
                    #     raise Exception
                    if Main.mountMove(save_img_path_1, save_usb_path, identifier) is not True:
                        raise Exception
                    if Main.mountMove(save_img_path_2, save_usb_path, identifier) is not True:
                        raise Exception
                if Main.mountMove(save_path, save_usb_path, identifier) is not True:
                    raise Exception
                if Main.mountMove(src_path, save_usb_path, identifier) is not True:
                    raise Exception
                self.update_json.emit(succeed_code)
            except Exception as e:
                print(e)
                self.update_json.emit(failed_code)
                return
        else:
            self.update_json.emit(failed_code)

    def split_string(self, obj, sec):
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
