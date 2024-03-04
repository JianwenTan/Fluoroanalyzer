import os
import cv2 as cv
import random
from PySide2.QtSql import QSqlDatabase, QSqlQuery
try:
    from view.gui.test import *
    from controller.PicController import MyPicThread
    from third_party.keyboard.keyboard import KeyBoard
    from view.AbstractPage import AbstractPage, ProcessDialog
    import util.frozen as frozen
    import util.dirs as dirs
    import middleware.database as insertdb
except ModuleNotFoundError:
    from qt0223.view.gui.test import *
    from qt0223.controller.PicController import MyPicThread
    from qt0223.third_party.keyboard.keyboard import KeyBoard
    from qt0223.view.AbstractPage import AbstractPage, ProcessDialog
    import qt0223.util.frozen as frozen
    import qt0223.util.dirs as dirs
    import qt0223.middleware.database as insertdb

allergen = [' ', '柳树', '普通豚草', '艾蒿', '屋尘螨']
SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'


class TestPage(Ui_Form, AbstractPage):
    """
    @detail 初始化加载界面信息，同时创建记录异常的信息
    @detail 构造函数
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self) -> None:
        """
        设置界面相关信息
        Returns:
            None
        """
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

        self.mypicthread = MyPicThread()
        self.mypicthread.finished.connect(self.takePicture)

        self.setFocusWidget()
        self.installEvent()
        self.setAllergenCb()
        self.setReagentCb()
        self.mytest()
        self.setBtnIcon()
        self.ui.tableView.horizontalHeader().close()
        self.ui.tableView.verticalHeader().close()
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def setBtnIcon(self) -> None:
        """
        设置按钮图标
        Returns:
            None
        """
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

    def mytest(self) -> None:
        """
        测试信息
        Returns:
            None
        """
        name_list = ["佚名", "00", "检验", "佚名"]
        self.ui.nameLine.setText(name_list[0])
        self.ui.docCb.setText(name_list[3])
        self.ui.ageLine.setText(name_list[1])
        self.ui.departCb.setText(name_list[2])

    def installEvent(self) -> None:
        """
        安装事件监听
        Returns:
            None
        """
        for item in self.focuswidget:
            item.installEventFilter(self)

    def setFocusWidget(self) -> None:
        """
        设置组件点击焦点
        Returns:
            None
        """
        self.focuswidget = [self.ui.nameLine, self.ui.paraLine, self.ui.ageLine, self.ui.departCb, self.ui.docCb]
        for item in self.focuswidget:
            item.setFocusPolicy(Qt.ClickFocus)

    def eventFilter(self, obj, event) -> bool:
        """
        槽函数
        事件过滤
        Args:
            obj: 发生事件的组件
            event: 发生的事件

        Returns:
            None
        """
        if obj in self.focuswidget:
            if event.type() == QEvent.Type.FocusIn:
                # print(obj.setText("hello"))
                self.setKeyBoard(obj)
                return True
            else:
                return False
        else:
            return False

    def setKeyBoard(self, obj) -> None:
        """
        槽函数
        设置可以键盘弹出的组件
        Args:
            obj: 键盘弹出的组件

        Returns:
            None
        """
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

    def getKeyBoardText(self, msg) -> None:
        """
        槽函数
        获取键盘的文本信息
        Args:
            msg: 信号，键盘文本信息

        Returns:
            None
        """
        self.focusWidget().setText(msg)
        self.focusWidget().clearFocus()

    def resetBtn(self) -> None:
        """
        重置按钮信息，当发生页面跳转时触发
        Returns:
            None
        """
        self.ui.btnSwitch.hide()
        self.ui.btnExe.hide()
        self.ui.btnPrint.hide()
        self.ui.btnDownload.hide()
        self.ui.btnConfirm.show()
        self.ui.btnReturn.setGeometry(410, 10, 380, 80)

    def setAllergenTableView(self) -> None:
        """
        设置表格过敏原
        Returns:
            None
        """
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

    def setAllergenCb(self) -> None:
        """
        添加检测组合
        Returns:
            None
        """
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

    def setTableView(self) -> None:
        """
        设置表格内容，主要是过敏原信息
        表格为旧表格，弃用，但不能删除代码
        Returns:
            None
        """
        # 设置行列
        # 需要改进
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

    def takePicture(self, msg) -> None:
        """
        实现图片提取功能，获取得到的img和pixel信息
        Args:
            msg: 信号，测试完后发出的时间信息

        Returns:
            None
        """
        cur_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        # time_now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        pic_path = QDateTime.currentDateTime().toString('yyyy-MM-dd')
        time_now = msg
        name_pic = time_now
        try:
            judge_flag, gray_aver, nature_aver, gray_aver_str, nature_aver_str = self.mypicthread.getGrayAver()
            if judge_flag != 1:
                m_title = ""
                m_info = "本次检测结果无效，建议重新进行检测"
                # infoMessage(m_info, m_title, 180)
                # self.update_info.emit(m_info)
                self.update_info.emit(dict(info=m_info, code=201))
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
            m_title = ""
            m_info = "系统错误！"
            # infoMessage(m_info, m_title, 300)
            self.update_info.emit(m_info)
            return

        img_final = cv.imread(frozen.app_path() + r'/pic_code/img/img_out/img_final.jpeg')
        img_origin = cv.imread(frozen.app_path() + r'/pic_code/img/img_out/img_0ori.jpeg')
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

        # self.testinfo.closeWin()
        page_msg = 'DataPage'
        # page_msg = 'newDataPage'
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
        # reagent_matrix_info = self.global_allergen
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
                         nature_aver_str=nature_aver_str,point_str=point_str)
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

    def setReagentCb(self) -> None:
        """
        读取数据库，获取试剂卡规格的信息
        弃用, 不能删除
        Returns:
            None
        """
        # MySQL语句
        sql = 'SELECT * FROM matrix_table'
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(SQL_PATH)
        db.open()
        try:
            q = QSqlQuery()
            q.exec_(sql)
        except Exception as e:
            print(e)
            # 有异常，回滚事务
        self.reagent_type = []
        self.reagent_matrix = []
        self.reagent_matrix_info = []
        while q.next():
            self.reagent_type.append(q.value(1))
            self.reagent_matrix.append(q.value(2))
            self.reagent_matrix_info.append(q.value(3))
        db.close()

    @Slot()
    def on_btnReturn_clicked(self) -> None:
        """
        槽函数
        返回按钮操作
        Returns:
            None
        """
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
    def on_btnConfirm_clicked(self) -> None:
        """
        槽函数
        确认按钮操作
        Returns:
            None
        """
        if self.ui.modeBox_1.currentIndex() == -1 or self.ui.nameLine.text() == "" or self.ui.ageLine.text() == "" \
                or self.ui.departCb.text() == "" or self.ui.docCb.text() == "":
            # m_title = ""
            # m_info = "请填写完信息！"
            # # infoMessage(m_info, m_title, 280)
            # self.showInfo(m_info)
            info = "请填写完信息！"
            self.showInfoDialog(info)
            return
        self.setTableView()
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.btnExe.show()
        self.ui.btnConfirm.hide()
        self.setAllergenTableView()

    @Slot()
    def on_btnExe_clicked(self) -> None:
        """
        槽函数
        检测按钮操作
        Returns:
            None
        """
        info = "图片生成中。。。"
        dialog = ProcessDialog()
        dialog.setInfo(info)
        dialog.setParent(self)
        dialog.hideBtn()
        dialog.show()
        # self.testinfo.show()
        self.mypicthread.setType(self.ui.modeBox_1.currentText())
        self.mypicthread.finished.connect(dialog.closeDialog)
        try:
            self.mypicthread.start()
        except Exception as e:
            dialog.closeDialog()
        print("test start!")