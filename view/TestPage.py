import os
import cv2 as cv
import random
import sqlite3
import re
try:
    from view.gui.test import *
    from controller.PicController import MyPicThread
    from third_party.keyboard.keyboard import KeyBoard
    from view.AbstractPage import AbstractPage, ProcessDialog
    import util.frozen as frozen
    import util.dirs as dirs
    import middleware.database as insertdb
except ModuleNotFoundError:
    from qt0922.view.gui.test import *
    from qt0922.controller.PicController import MyPicThread
    from qt0922.third_party.keyboard.keyboard import KeyBoard
    from qt0922.view.AbstractPage import AbstractPage, ProcessDialog
    import qt0922.util.frozen as frozen
    import qt0922.util.dirs as dirs
    import qt0922.middleware.database as insertdb

allergen = [' ', '柳树', '普通豚草', '艾蒿', '屋尘螨']
SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'


class TestPage(Ui_Form, AbstractPage):
    def __init__(self):
        """
        荧光检疫界面
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self):

        self.ui.btnExe.hide()
        self.ui.btnPrint.hide()
        self.ui.btnDownload.hide()
        self.ui.btnSwitch.hide()
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.radioButton_2.setChecked(True)
        # 测试
        self.ui.typeLabel.setText("8x5")
        self.genderCb = QButtonGroup()
        self.genderCb.addButton(self.ui.radioButton)
        self.genderCb.addButton(self.ui.radioButton_2)
        self.genderCb.setId(self.ui.radioButton, 1)
        self.genderCb.setId(self.ui.radioButton_2, 2)
        self.ui.exeTable.horizontalHeader().close()
        self.ui.exeTable.verticalHeader().close()

        self.setFocusWidget()
        self.installEvent()
        self.setAllergenCb()
        # self.setReagentCb()
        self.mytest()
        self.setBtnIcon()
        self.ui.tableView.horizontalHeader().close()
        self.ui.tableView.verticalHeader().close()
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def setBtnIcon(self):

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnConfirm.setIconSize(QSize(32, 32))
        self.ui.btnConfirm.setIcon(QIcon(confirm_icon_path))

        exe_icon_path = frozen.app_path() + r"/res/icon/exe.png"
        self.ui.btnExe.setIconSize(QSize(32, 32))
        self.ui.btnExe.setIcon(QIcon(exe_icon_path))

        exe_icon_path = frozen.app_path() + r"/res/icon/exe.png"
        self.ui.btnPrint.setIconSize(QSize(32, 32))
        self.ui.btnPrint.setIcon(QIcon(exe_icon_path))

        switch_icon_path = frozen.app_path() + r"/res/icon/switch.png"
        self.ui.btnSwitch.setIconSize(QSize(32, 32))
        self.ui.btnSwitch.setIcon(QIcon(switch_icon_path))

        exe_icon_path = frozen.app_path() + r"/res/icon/compute.png"
        self.ui.btnDownload.setIconSize(QSize(32, 32))
        self.ui.btnDownload.setIcon(QIcon(exe_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

    def mytest(self):

        name_list = ["佚名", "00", "检验", "佚名"]
        self.ui.nameLine.setText(name_list[0])
        self.ui.docCb.setText(name_list[3])
        self.ui.ageLine.setText(name_list[1])
        self.ui.departCb.setText(name_list[2])

    def installEvent(self):

        for item in self.focuswidget:
            item.installEventFilter(self)

    def setFocusWidget(self):

        self.focuswidget = [self.ui.nameLine, self.ui.paraLine, self.ui.ageLine, self.ui.departCb, self.ui.docCb]
        for item in self.focuswidget:
            item.setFocusPolicy(Qt.ClickFocus)

    def eventFilter(self, obj, event):
        if obj in self.focuswidget:
            if event.type() == QEvent.Type.FocusIn:
                # print(obj.setText("hello"))
                self.setKeyBoard(obj)
                return True
            else:
                return False
        else:
            return False

    def setKeyBoard(self, obj):

        self.keyboardtext = KeyBoard()
        self.keyboardtext.text_msg.connect(self.getKeyBoardText)
        obj_name = obj.objectName()
        obj_text = obj.text()
        self.keyboardtext.textInput.setText(obj_text)
        if obj_name == "paraLine":
            self.keyboardtext.nameLabel.setText("参数")
        elif obj_name == "nameLine":
            self.keyboardtext.nameLabel.setText("姓名")
        elif obj_name == "ageLine":
            self.keyboardtext.nameLabel.setText("年龄")
        elif obj_name == "departCb":
            self.keyboardtext.nameLabel.setText("科室")
        else:
            self.keyboardtext.nameLabel.setText("送检医生")
        self.keyboardtext.showWindow()

    def getKeyBoardText(self, msg):

        self.focusWidget().setText(msg)
        self.focusWidget().clearFocus()

    def resetBtn(self):

        self.ui.btnSwitch.hide()
        self.ui.btnExe.hide()
        self.ui.btnPrint.hide()
        self.ui.btnDownload.hide()
        self.ui.btnConfirm.show()
        self.ui.btnReturn.setGeometry(410, 10, 380, 80)

    def setAllergenTableView(self):
        f_name = self.ui.modeBox_1.currentText()
        path = frozen.app_path() + r"/res/allergen/"
        f = open(path + f_name, "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
        allergen = []
        for i in lines:
            allergen.append(i.rstrip())
        row = 8 + 1
        column = 5
        self.global_allergen = allergen
        allergen_table_model = QStandardItemModel(row, column)
        self.ui.tableView.setModel(allergen_table_model)

        coordinates = [(0, 0), (0, 4), (8, 0), (8, 4)]
        for coord in coordinates:
            color = QColor(255, 255, 127)
            item = QStandardItem()
            item.setData(color, Qt.BackgroundColorRole)
            item.setTextAlignment(Qt.AlignCenter)
            allergen_table_model.setItem(coord[0], coord[1], item)
        for i in range(row):
            for j in range(column):
                if allergen[i * column + j] != '':
                    color = QColor(0, 255, 0)
                    # print(allergen[num])
                    item = QStandardItem(allergen[i * column + j])
                    item.setData(color, Qt.BackgroundColorRole)
                    item.setTextAlignment(Qt.AlignCenter)
                    allergen_table_model.setItem(i, j, item)

    def setAllergenCb(self):
        # 指定要读取的路径
        path = frozen.app_path() + r"/res/allergen/"
        # path = r"/res/allergen/"
        # 获取指定路径下的所有文件名
        filenames = os.listdir(path)
        self.ui.modeBox_1.clear()
        # 输出所有文件名
        for filename in filenames:
            # self.ui.modeBox_3.clear()
            self.ui.modeBox_1.addItem(filename)
            self.ui.modeBox_1.setCurrentIndex(-1)

    def setTableView(self):
        if self.ui.modeBox_1.currentIndex() == -1:
            return
        # self.ui.photolabel.setText("表格生成中。。。")
        dict_mode = {
            "2x3": 1,
            "2x5": 2,
            "4x5": 3,
            "8x5": 4,
        }
        if dict_mode.get(self.ui.typeLabel.text()) == 1:
            self.row_exetable = 2
            self.column_exetable = 3
        elif dict_mode.get(self.ui.typeLabel.text()) == 2:
            self.row_exetable = 2
            self.column_exetable = 5
        elif dict_mode.get(self.ui.typeLabel.text()) == 3:
            self.row_exetable = 4
            self.column_exetable = 5
        else:
            self.row_exetable = 8
            self.column_exetable = 5

        self.pix_table_model = QStandardItemModel(self.row_exetable + int(self.row_exetable / 2), self.column_exetable)
        self.ui.exeTable.setModel(self.pix_table_model)

        self.ui.exeTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.exeTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # str_num = self.reagent_matrix_info[self.reagent_type.index(self.ui.modeBox_1.currentText())]
        # 测试
        str_num = self.reagent_matrix_info[self.reagent_type.index("58")]

        for i in range(0, self.row_exetable + int(self.row_exetable / 2)):
            if i % 3 == 0:
                for j in range(0, self.column_exetable):
                    content_cb = QComboBox(self)
                    content_cb.addItems(allergen)
                    num = int(str_num[j + (i % 3) * self.row_exetable])
                    content_cb.setCurrentIndex(num)
                    content_cb.setEditable(True)
                    _lineEdit = content_cb.lineEdit()
                    _lineEdit.setAlignment(Qt.AlignCenter)
                    # content_cb.setStyleSheet(self.cb_style_sheet)
                    self.ui.exeTable.setIndexWidget(self.pix_table_model.index(i, j), content_cb)

    def takePicture(self, msg):
        cur_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        # time_now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        pic_path = QDateTime.currentDateTime().toString('yyyy-MM-dd')
        time_now = msg['timenow']
        judge_flag = msg['flag']
        name_pic = time_now
        try:
            # judge_flag, gray_aver, nature_aver, gray_aver_str, nature_aver_str = self.mypicthread.getGrayAver()
            # judge_flag = self.mypicthread.getGrayAver()
            if judge_flag is False:
                m_title = ""
                m_info = "本次检测结果无效，建议重新进行检测"
                # infoMessage(m_info, m_title, 180)
                # self.update_info.emit(m_info)
                self.showInfoDialog(m_info)
                # self.update_info.emit(dict(info=m_info, code=201))
                return
            # return
            # gray_row = 8
            # gray_column = 5
            # point_list = gray_aver[0]
            # point_str = ''
            # for i in point_list:
            #     if i < 0:
            #         point_str = point_str + ','
            #     else:
            #         point_str = point_str + ',' + str(i)
            # point_str = point_str[1:]
            # gray_aver = _matrix[1:]
        except Exception as e:
            self.sendException()
            m_title = ""
            m_info = "系统错误！"
            # infoMessage(m_info, m_title, 300)
            self.update_info.emit(m_info)
            return


        img_final = cv.imread(frozen.app_path() + r'/pic_code/dataset/img_result/img_out/img_final.jpeg')
        img_origin = cv.imread(frozen.app_path() + r'/pic_code/dataset/img_result/img_out/img_0ori.jpeg')
        # img_show_final = cv.imread(frozen.app_path() + r'/pic_code/img/img_out/img_show_final.jpeg')
        # img_show_origin = cv.imread(frozen.app_path() + r'/pic_code/img/img_out/img_show_0ori.jpeg')
        img_show_final = img_final
        img_show_origin = img_origin

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

        page_msg = 'DataPage'
        self.next_page.emit(page_msg)

        patient_id = random.randint(1000, 1999)

        patient_name = self.ui.nameLine.text()
        patient_age = self.ui.ageLine.text()
        id_num = self.genderCb.checkedId()
        patient_gender = "男" if id_num == 1 else "女"

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
        reagent_matrix_info = self.readPixtableNum()
        matrix_str = ','.join(','.join(row) for row in reagent_matrix_info)
        reagent_matrix_info = re.split(r",", matrix_str)

        # selecting database get info eg: gray_aver allergen-points about reagent-test result
        gray_aver_sql = insertdb.selectMySql(time_now)
        gray_list = re.split(r",", gray_aver_sql)
        point_list = gray_list[:5]
        point_str = ""
        for i in point_list:
            if int(i) < 0:
                point_str = point_str + ','
            else:
                point_str = point_str + ',' + i
        point_str = point_str[1:]

        # creating empty list to merge
        result = []
        # looping merge two list, 5 elements from list1, 10 elements from list2
        for i in range(len(gray_list[5:]) // 10):
            sublist1 = reagent_matrix_info[i * 5:i * 5 + 5]
            sublist2 = gray_list[5:][i * 10:i * 10 + 10]
            result.extend(sublist1 + sublist2)

        reagent_matrix_info = ",".join(result)
        reagent_time = test_time[0]
        reagent_time_detail = test_time[1]
        reagent_code = code_num
        reagent_matrix = matrix

        # structuring patient insert info
        info_json = dict(
            patient_name=patient_name,
            patient_id=patient_id,
            patient_age=patient_age,
            patient_gender=patient_gender
        )

        # structuring reagent insert info
        data_json = dict(
            patient_id=patient_id,
            reagent_time=reagent_time,
            reagent_code=reagent_code,
            doctor=doctor,
            depart=depart,
            reagent_matrix=reagent_matrix,
            reagent_time_detail=reagent_time_detail,
            reagent_matrix_info=reagent_matrix_info,
            patient_name=patient_name,
            patient_age=patient_age,
            patient_gender=patient_gender,
            points=point_str,
            reagent_photo=time_now
        )

        # insert to sqlite database
        insertdb.insertMySql(info_json, data_json)
        # get reagent id to select photo
        reagent_id = insertdb.searchId(time_now)
        data_json = insertdb.changePhoto(reagent_id)
        info_msg = 201
        self.update_json.emit(dict(info=info_msg, data=data_json))
        return

    def readPixtableNum(self):
        reagent_matrix_info = []
        for i in range(self.row_exetable):
            row_list = []
            for j in range(self.column_exetable):
                index = self.ui.tableView.model().index(i + 1, j)  # 获取单元格的 QModelIndex 对象
                data = "" if index.data() == None else index.data()
                row_list.append(data)
                # combo_box = self.ui.tableView.indexWidget(index)  # 获取该单元格中的 QComboBox 对象
                # current_text = combo_box.currentText()  # 获取 QComboBox 当前选中的文本
                # row_list.append(str(current_text))
            reagent_matrix_info.append(row_list)
        result = []
        for i in range(0, self.row_exetable, 2):
            result.append([a + b for a, b in zip(reagent_matrix_info[i], reagent_matrix_info[i + 1])])
        return result

    def setReagentCb(self):
        # MySQL语句
        sql = 'SELECT * FROM matrix_table'
        conn = sqlite3.connect(SQL_PATH)
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            # 有异常，回滚事务
            print(e)
            conn.rollback()
        self.reagent_type = []
        self.reagent_matrix = []
        self.reagent_matrix_info = []
        for x in cur.fetchall():
            self.reagent_type.append(x[1])
            self.reagent_matrix.append(x[2])
            self.reagent_matrix_info.append(x[3])
        cur.close()
        conn.close()

    @Slot()
    def on_btnReturn_clicked(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            page_msg = 'HomePage'
            self.next_page.emit(page_msg)
        elif self.ui.stackedWidget.currentIndex() == 1:
            self.resetBtn()
            self.ui.stackedWidget.setCurrentIndex(0)
        elif self.ui.stackedWidget.currentIndex() == 2:
            self.resetBtn()
            self.ui.stackedWidget.setCurrentIndex(0)
        elif self.ui.stackedWidget.currentIndex() == 3:
            self.resetBtn()
            self.ui.stackedWidget.setCurrentIndex(0)

    @Slot()
    def on_btnConfirm_clicked(self):
        if self.ui.modeBox_1.currentIndex() == -1 or self.ui.nameLine.text() == "" or self.ui.ageLine.text() == "" \
                or self.ui.departCb.text() == "" or self.ui.docCb.text() == "":
            # m_title = ""
            # m_info = "请填写完信息！"
            # # infoMessage(m_info, m_title, 280)
            # self.showInfo(m_info)
            info = "请填写完信息！"
            self.showInfoDialog(info)
            return
        # self.setTableView()
        self.row_exetable = 8
        self.column_exetable = 5
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.btnExe.show()
        self.ui.btnConfirm.hide()
        self.setAllergenTableView()

    @Slot()
    def on_btnExe_clicked(self):
        info = "图片生成中。。。"
        dialog = ProcessDialog()
        dialog.setInfo(info)
        dialog.setParent(self)
        dialog.hideBtn()
        dialog.show()
        # self.testinfo.show()
        mypicthread = MyPicThread()
        mypicthread.update_json.connect(self.takePicture)
        mypicthread.finished.connect(dialog.closeDialog)
        mypicthread.setType(self.ui.modeBox_1.currentText())
        try:
            mypicthread.start()
        except Exception as e:
            dialog.closeDialog()
        print("test start!")