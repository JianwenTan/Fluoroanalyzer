import cv2 as cv
import random
from PySide2.QtCore import QDateTime, Signal
try:
    from controller.AbstractController import AbstractController
    from controller.PicController import MyPicThread
    import util.frozen as frozen
    import util.dirs as dirs
except ModuleNotFoundError:
    from qt0922.controller.AbstractController import AbstractController
    from qt0922.controller.PicController import MyPicThread
    import qt0922.util.frozen as frozen
    import qt0922.util.dirs as dirs


FAILED_CODE = 404
SUCCEED_CODE = 202

class TestPageController(AbstractController):
    def __init__(self):
        super().__init__()
        self.item_type = ""
        self.mypicthread = MyPicThread()
        self.mypicthread.finished.connect(self.takePicture)

    def __del__(self):
        super().__del__()

    def takePicture(self):
        self.mypicthread = MyPicThread()
        self.mypicthread.finished.connect(self.getImgPixel)
        self.mypicthread.start()

    def getImgPixel(self, msg):
        cur_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        # time_now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        pic_path = QDateTime.currentDateTime().toString('yyyy-MM-dd')
        time_now = msg

        img_final = cv.imread(frozen.app_path() + r'/third_party/img/img_out/img_final.jpeg')
        img_origin = cv.imread(frozen.app_path() + r'/third_party/img/img_out/img_0ori.jpeg')
        # 测试
        gray_aver = img_final[0]
        gray_row = 8
        gray_column = 5
        nature_aver = [['弱阳性' '0.0' '强阳性' '0.0' '弱阳性'],
                       ['0.0' '强阳性' '0.0' '强阳性' '0.0'],
                       ['阴性' '0.0' '强阳性' '0.0' '弱阳性'],
                       ['0.0' '弱阳性' '0.0' '强阳性' '0.0'],
                       ['阴性' '0.0' '弱阳性' '0.0' '阴性'],
                       ['0.0' '强阳性' '0.0' '弱阳性' '0.0'],
                       ['阴性' '0.0' '弱阳性' '0.0' '弱阳性'],
                       ['0.0' '弱阳性' '0.0' '强阳性' '0.0']]
        gray_aver_str = ",1323184,-349869,1323181,-349869,1323186" \
                        ",100528,1323179,1323186,1323157,104541" \
                        ",64049,1323186,1323186,1323186,84718" \
                        ",26193,130751,1323186,1323186,69341" \
                        ",4302,80113,144806,1323186,42978" \
                        ",35213,1323184,94057,68700,77" \
                        ",44898,1323186,75788,64454,0" \
                        ",24805,66857,113782,1323181,85446" \
                        ",1323106,77360,1323186,1323186,1323175"
        nature_aver_str = ",弱阳性,0,强阳性,0,弱阳性" \
                          ",0,强阳性,0,强阳性,0" \
                          ",阴性,0,强阳性,0,弱阳性" \
                          ",0,弱阳性,0,强阳性,0" \
                          ",阴性,0,弱阳性,0,阴性" \
                          ",0,强阳性,0,弱阳性,0" \
                          ",阴性,0,弱阳性,0,弱阳性" \
                          ",0,弱阳性,0,强阳性,0"
        gray_aver = [[100528, 1323179, 1323186, 1323157, 104541],
                     [64049, 1323186, 1323186, 1323186, 84718],
                     [26193, 130751, 1323186, 1323186, 69341],
                     [4302, 80113, 144806, 1323186, 42978],
                     [35213, 1323184, 94057, 68700, 77],
                     [44898, 1323186, 75788, 64454, 0],
                     [24805, 66857, 113782, 1323181, 85446],
                     [1323106, 77360, 1323186, 1323186, 1323175]]
        point_str = '1323184,, 1323181,, 1323186'
        name_pic = time_now
        name_pic = "1"

        try:
            judge_flag, gray_aver, nature_aver, gray_aver_str, nature_aver_str = self.mypicthread.getGrayAver()
            # judge_flag, gray_aver, nature_aver, gray_aver_str, nature_aver_str = self.controller.getGrayAver()
            if judge_flag != 1:
                code = FAILED_CODE
                nature_aver = nature_aver
                gray_aver_str = gray_aver_str
                nature_aver_str = nature_aver_str
                point_str = FAILED_CODE
                self.update_json.emit(dict(code=code, nature_aver=nature_aver, gray_aver_str=gray_aver_str,
                                           nature_aver_str=nature_aver_str, point_str=point_str))
                return
            # gray_row = len(_matrix) - 1
            # gray_column = len(_matrix[0])
            # point_list = _matrix[0]
            gray_row = 8
            gray_column = 5
            point_list = gray_aver[0]
            point_str = ''
            for i in point_list:
                if i < 0:
                    point_str = point_str + ','
                else:
                    point_str = point_str + ',' + str(i)
            point_str = point_str[1:]
            # gray_aver = _matrix[1:]
        except Exception as e:
            self.sendException()
            return

        img_final = cv.imread(frozen.app_path() + r'/third_party/img/img_out/img_final.jpeg')
        img_origin = cv.imread(frozen.app_path() + r'/third_party/img/img_out/img_0ori.jpeg')
        img_show_final = cv.imread(frozen.app_path() + r'/third_party/img/img_out/img_show_final.jpeg')
        img_show_origin = cv.imread(frozen.app_path() + r'/third_party/img/img_out/img_show_0ori.jpeg')

        save_path = frozen.app_path() + r'/img/' + r'/' + pic_path + r'/' + name_pic + '-1.jpeg'
        dirs.makedir(save_path)
        flag_bool = cv.imwrite(save_path, img_origin)
        save_path = frozen.app_path() + r'/img/' + r'/' + pic_path + r'/' + name_pic + '-2.jpeg'
        dirs.makedir(save_path)
        flag_bool = cv.imwrite(save_path, img_final)
        save_path = frozen.app_path() + r'/img/' + r'/' + pic_path + r'/' + name_pic + '-3.jpeg'
        dirs.makedir(save_path)
        flag_bool = cv.imwrite(save_path, img_show_origin)
        save_path = frozen.app_path() + r'/img/' + r'/' + pic_path + r'/' + name_pic + '-4.jpeg'
        dirs.makedir(save_path)
        flag_bool = cv.imwrite(save_path, img_show_final)

        self.testinfo.closeWin()
        page_msg = 'dataPage'
        # page_msg = 'newDataPage'
        self.next_page.emit(page_msg)

        patient_id = random.randint(1000, 1999)

        # name_id = random.randint(1,199)
        # patient_name = self.name_file[name_id].get("name")
        # patient_age = self.name_file[name_id].get("age")
        # patient_gender = self.name_file[name_id].get("gender")

        patient_name = self.ui.nameLine.text()
        patient_age = self.ui.ageLine.text()
        id_num = self.genderCb.checkedId()
        if id_num == 0:
            patient_gender = "男"
        else:
            patient_gender = "女"

        # patient_gender = self.ui.genderCb.currentText()

        item_type = self.ui.modeBox_1.currentText()
        pic_name = name_pic

        # 时间进行切片
        test_time = cur_time.split()

        doctor = self.ui.docCb.text()
        depart = self.ui.departCb.text()
        age = self.ui.ageLine.text()
        gender = patient_gender
        name = self.ui.nameLine.text()

        matrix = self.ui.typeLabel.text()
        code_num = random.randint(1000, 19999)
        reagent_matrix_info = self.readPixtable()
        # reagent_matrix_info = self.global_allergen
        data_json = dict(patient_id=patient_id, patient_name=patient_name,
                         patient_age=patient_age, patient_gender=patient_gender,
                         item_type=item_type, pic_name=pic_name,
                         time=test_time, doctor=doctor,
                         depart=depart, age=age,
                         gender=gender, name=name,
                         matrix=matrix, code_num=code_num,
                         gray_aver=gray_aver, gray_row=gray_row,
                         gray_column=gray_column, pic_path=pic_path,
                         name_pic=name_pic, row_exetable=self.row_exetable,
                         column_exetable=self.column_exetable, reagent_matrix_info=reagent_matrix_info)
        # new data
        data_json = dict(patient_id=patient_id, patient_name=patient_name,
                         patient_age=patient_age, patient_gender=patient_gender,
                         item_type=item_type, pic_name=pic_name,
                         time=test_time, doctor=doctor,
                         depart=depart, age=age,
                         gender=gender, name=name,
                         matrix=matrix, code_num=code_num,
                         gray_aver=gray_aver, gray_row=gray_row,
                         gray_column=gray_column, pic_path=pic_path,
                         name_pic=name_pic, row_exetable=self.row_exetable,
                         column_exetable=self.column_exetable, reagent_matrix_info=reagent_matrix_info,
                         nature_aver=nature_aver, gray_aver_str=gray_aver_str,
                         nature_aver_str=nature_aver_str, point_str=point_str)
        info_msg = 201
        self.update_json.emit(dict(info=info_msg, data=data_json))
        return

    def setType(self, item_type):
        self.item_type = item_type