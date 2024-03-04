"""
@Description：历史记录界面显示
@Author：mysondrink@163.com
@Time：2024/1/11 10:39
"""
import os
import shutil
import datetime
import sys
import math
from PySide2.QtSql import QSqlQuery, QSqlDatabase
try:
    from third_party.keyboard.keyboard import KeyBoard
    # from func.testinfo import MyTestInfo
    from view.gui.history import *
    from util import dirs
    # from func.infoPage import infoMessage
    import util.frozen as frozen
    from util.report import MyReport
    # from inf.print import Em5822_Print
    from view.AbstractPage import AbstractPage
except ModuleNotFoundError:
    from qt0223.third_party.keyboard.keyboard import KeyBoard
    # from func.testinfo import MyTestInfo
    from qt0223.view.gui.history import *
    from qt0223.util import dirs
    # from func.infoPage import infoMessage
    import qt0223.util.frozen as frozen
    from qt0223.util.report import MyReport
    # from inf.print import Em5822_Print
    from qt0223.view.AbstractPage import AbstractPage

page_dict = {'page': 0, 'page_2': 1, 'page_3': 2, 'page_4': 3}
header_list = ["试剂卡编号", "采样时间",  "病人编号" , "病人姓名"]
SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'


class HistoryPage(Ui_Form, AbstractPage):
    next_page = Signal(str)
    update_json = Signal(dict)
    update_log = Signal(str)

    """
    @detail 初始化加载界面信息，同时创建记录异常的信息
    @detail 构造函数
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    """
    @detail 设置界面相关信息
    """
    def InitUI(self):
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.dateBox.setCalendarPopup(True)
        self.ui.dateBox.setDateTime(QDateTime.currentDateTime())
        # self.ui.historyTable.horizontalHeader().close()
        self.ui.historyTable.verticalHeader().close()

        self.setFocusWidget()
        self.installEvent()

        self.setBtnIcon()

        self.resetBtn_3()
        self.ui.btnDownload.hide()
        self.ui.btnPrint.hide()
        self.ui.btnReport.hide()
        self.setAllergenCb()
        # self.setReagentCb()
        # self.setTableWidget()

    """
    @detail 安装事件监听
    """
    def installEvent(self):
        for item in self.focuswidget:
            item.installEventFilter(self)

    """
    @detail 设置组件点击焦点
    """
    def setFocusWidget(self):
        self.focuswidget = [self.ui.lineEdit, self.ui.lineEdit_2]
        for item in self.focuswidget:
            item.setFocusPolicy(Qt.ClickFocus)

    """
    @detail 事件过滤
    @detail 槽函数
    @param obj: 发生事件的组件
    @param event: 发生的事件
    """
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

    """
    @detail 设置可以键盘弹出的组件
    @detail 槽函数
    @param obj: 键盘弹出的组件
    """
    def setKeyBoard(self, obj):
        self.keyboardtext = KeyBoard()
        self.keyboardtext.text_msg.connect(self.getKeyBoardText)
        obj_name = obj.objectName()
        obj_text = obj.text()
        self.keyboardtext.textInput.setText(obj_text)
        if obj_name == "lineEdit":
            self.keyboardtext.nameLabel.setText("送检医生")
        elif obj_name == "lineEdit_2":
            self.keyboardtext.nameLabel.setText("科室")
        self.keyboardtext.showWindow()

    """
    @detail 获取键盘的文本信息
    @detail 槽函数
    @param msg: 信号，键盘文本信息
    """
    def getKeyBoardText(self, msg):
        self.focusWidget().setText(msg)
        self.focusWidget().clearFocus()

    """
    @detail 设置按钮图标
    """
    def setBtnIcon(self):
        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnConfirm.setIconSize(QSize(32, 32))
        self.ui.btnConfirm.setIcon(QIcon(confirm_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

        pre_icon_path = frozen.app_path() + r"/res/icon/pre.png"
        self.ui.btnPre.setIconSize(QSize(32, 32))
        self.ui.btnPre.setIcon(QIcon(pre_icon_path))

        next_icon_path = frozen.app_path() + r"/res/icon/next.png"
        self.ui.btnNext.setIconSize(QSize(32, 32))
        self.ui.btnNext.setIcon(QIcon(next_icon_path))

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnReport.setIconSize(QSize(32, 32))
        self.ui.btnReport.setIcon(QIcon(confirm_icon_path))

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnDetail.setIconSize(QSize(32, 32))
        self.ui.btnDetail.setIcon(QIcon(confirm_icon_path))

        exe_icon_path = frozen.app_path() + r"/res/icon/compute.png"
        self.ui.btnDownload.setIconSize(QSize(32, 32))
        self.ui.btnDownload.setIcon(QIcon(exe_icon_path))

        exe_icon_path = frozen.app_path() + r"/res/icon/exe.png"
        self.ui.btnPrint.setIconSize(QSize(32, 32))
        self.ui.btnPrint.setIcon(QIcon(exe_icon_path))

    """
    @detail 重置按钮
    @detail 弃用
    """
    def resetBtn(self):
        self.ui.btnReport.setText('报告单')
        self.ui.btnReport.hide()
        self.ui.btnDownload.hide()
        self.ui.btnPrint.hide()
        self.ui.stackedWidget.setCurrentIndex(1)

    """
    @detail 查询列表页面跳转
    """
    def resetBtn_2(self):
        self.ui.btnNext.show()
        self.ui.btnPre.show()
        self.ui.btnDetail.show()
        self.ui.btnReturn.setGeometry(601, 10, 187, 80)

    """
    @detail 查询页面跳转
    """
    def resetBtn_3(self):
        self.ui.btnNext.hide()
        self.ui.btnPre.hide()
        self.ui.btnDetail.hide()

    """
    @detail 设置页面跳转信息
    @param cur_page: 当前页面页数
    """
    def setHistoryTable(self, cur_page):
        if cur_page == 1:
            self.current_page += 1
        elif cur_page == 2:
            if self.current_page == 0:
                # m_title = "错误"
                # m_title = ""
                # m_info = "已经是第一页!"
                # infoMessage(m_info, m_title)
                info = "已经是第一页!"
                self.update_info.emit(info)
                return
            self.current_page -= 1
        elif cur_page == 3:
            if self.current_page == self.total_page - 1:
                # m_title = "错误"
                # m_title = ""
                # m_info = "已经是最后一页!"
                # infoMessage(m_info, m_title)
                info = "已经是最后一页!"
                self.update_info.emit(info)
                return
            self.current_page += 1
        min_page = self.current_page * self.page_size
        self.min_size = self.row_histable - min_page if self.page_size > self.row_histable - min_page else self.page_size
        max_page = self.min_size + self.current_page * self.page_size

        column_histable = len(header_list)
        self.select_table_model = QStandardItemModel(self.page_size, column_histable)

        for i in range(column_histable):
            self.select_table_model.setHeaderData(i, Qt.Horizontal, header_list[i])

        header_view = self.ui.historyTable.horizontalHeader()
        header_view.setStyleSheet("font: 20pt;background-color:#05abc2;")
        ver_view = self.ui.historyTable.verticalHeader()
        ver_view.setStyleSheet("font: 20pt;background-color:#05abc2;")

        self.ui.historyTable.setModel(self.select_table_model)
        self.ui.historyTable.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置表格不可编辑
        self.ui.historyTable.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中

        self.ui.historyTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.historyTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 插入表格
        # 需要改进
        for i in range(min_page, max_page):
            for j in range(column_histable):
                if j == 1:
                    item = QStandardItem(self.time_list[i][10:])
                elif j == 2:
                    item = QStandardItem(self.patient_id_list[i])
                elif j == 3:
                    # item = QStandardItem(self.patient_name_list[i])
                    item = QStandardItem(self.name_list[i])
                else:
                    item = QStandardItem(self.reagent_id_list[i])
                item.setTextAlignment(Qt.AlignCenter)
                self.select_table_model.setItem(i - self.current_page * self.page_size, j, item)
                # self.select_table_model.setItem(i, j, item)
        for i in range(self.min_size, self.page_size):
            for j in range(column_histable):
                item = QStandardItem()
                item.setTextAlignment(Qt.AlignCenter)
                self.select_table_model.setItem(i, j, item)

        # self.ui.historyTable.currentChanged(self.changePhoto) # 选中时改变图片
        # self.ui.historyTable.selectionModel().currentChanged.connect(self.changePhoto)
        # self.ui.btnDetail.clicked.connect(self.changePhoto)

    """
    @detail 根据时间和规格查询数据库数据
    @param time: 查询测试时间
    @param item_type: 查询试剂卡规格
    """
    def selectMysql(self, time, item_type, doctor, depart):
        search_mode = 1
        global header_list
        if doctor != '':
            search_mode = 2
            sql = "SELECT * FROM reagent_copy1 WHERE reagent_type = '%s' AND reagent_time = '%s' AND doctor = '%s';"
        elif depart != '':
            search_mode = 3
            sql = "SELECT * FROM reagent_copy1 WHERE reagent_type = '%s' AND reagent_time = '%s' AND doctor = '%s' AND depart = '%s';"
        else:
            # MySQL语句
            sql = "SELECT * FROM reagent_copy1 WHERE reagent_type = '%s' AND reagent_time = '%s';"
            search_mode = 1
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(SQL_PATH)
        db.open()
        try:
            if search_mode == 1:
                # 执行SQL语句
                q = QSqlQuery()
                q.exec_(sql % (item_type, time))
            elif search_mode == 2:
                # 执行SQL语句
                q = QSqlQuery()
                q.exec_(sql % (item_type, time, doctor))
            elif search_mode == 3:
                # 执行SQL语句
                q = QSqlQuery()
                q.exec_(sql % (item_type, time, doctor, depart))
            # print(q.executedQuery())
        except Exception as e:
            print(e)

        # 设置历史数据图表
        self.time_list = []
        self.patient_id_list = []
        self.reagent_id_list = []
        self.patient_name_list = []
        self.reagent_info = []
        self.name_list = []

        """
        按照数据库数据排序，对数据进行处理
        第四行和第十行为采样时间
        第二行为病人号码
        第五行为试剂卡编号
        """
        sum = 0
        while q.next():
            self.time_list.append(q.value(3) + " " + q.value(9))
            # print(x[9])
            self.patient_id_list.append(str(q.value(1)))
            self.reagent_id_list.append(str(q.value(4)))
            self.reagent_info.append(q.value(10))
            self.name_list.append(q.value(11))
            sum = sum + 1

        self.row_histable = sum
        self.column_histable = len(header_list)
        self.page_size = 5  # 每组最大
        self.total_page = math.ceil(self.row_histable / self.page_size)
        self.current_page = -1

        sql = "SELECT * FROM patient_copy1;"
        try:
            # 执行SQL语句
            q.exec_(sql)
        except Exception as e:
            print(e)

        self.patien_info_list = []
        temp = []
        while q.next():
            for i in range(20):
                temp.append(q.value(i))
            self.patien_info_list.append(temp)
            temp = []

        for i in self.patient_id_list:
            for j in self.patien_info_list:
                if int(i) == j[3]:
                    self.patient_name_list.append(j[0])

        self.setHistoryTable(1)
        db.close()

    """
    @detail 历史数据图片展示，选中是改变图片
    @param current_row: 选中的行
    """
    def changePhoto(self, current_row):
        # self.statusBar().showMessage('选中第{}行'.format(current.row() + 1))

        num = current_row + self.page_size * self.current_page
        pic_num = self.reagent_id_list[num]

        # MySQL语句
        sql = "SELECT reagent_photo, reagent_type FROM reagent_copy1 WHERE reagent_id = %s"
        sql_2 = "SELECT * FROM reagent_copy1 WHERE reagent_id = %s"
        sql_3 = "SELECT * FROM reagent_copy1 WHERE patient_id = %s"

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(SQL_PATH)
        db.open()
        try:
            # 执行SQL语句
            q = QSqlQuery()
            q.exec_(sql_2 % (pic_num))
            while q.next():
                item_type = q.value(0)
                patient_id = q.value(1)
                pic_name = q.value(2)
                pic_path = q.value(3)
                code_num = q.value(5)
                doctor = q.value(6)
                depart = q.value(7)
                reagent_matrix = q.value(8)
                row_exetable = reagent_matrix[0]
                column_exetable = reagent_matrix[2]
                cur_time = []
                cur_time.append(pic_path)
                cur_time.append(q.value(9))
                reagent_matrix_info = q.value(10)
                patient_name = q.value(11)
                patient_age = q.value(12)
                patient_gender = q.value(13)
                age = q.value(12)
                gender = q.value(13)
                name = q.value(11)
                points = q.value(14)
                name_pic = pic_name
                point_str = q.value(14)
                gray_aver_str = q.value(15)
                nature_aver_str = q.value(16)
                data_json = dict(patient_id=patient_id, patient_name=patient_name,
                                 patient_age=patient_age, patient_gender=patient_gender,
                                 item_type=item_type, pic_name=pic_name,
                                 time=cur_time, doctor=doctor,
                                 depart=depart, age=age,
                                 gender=gender, name=name,
                                 matrix=reagent_matrix, code_num=code_num,
                                 pic_path=pic_path, name_pic=name_pic,
                                 row_exetable=row_exetable, column_exetable=column_exetable,
                                 reagent_matrix_info=reagent_matrix_info,point_str=point_str,
                                 gray_aver_str=gray_aver_str,nature_aver_str=nature_aver_str)
                info_msg = 202
                self.update_json.emit(dict(info=info_msg, data=data_json))
        except Exception as e:
            print(e)

        # 释放内存
        db.close()

    def setAllergenCb(self):
        # 指定要读取的路径
        path = frozen.app_path() + r"/res/allergen/"
        # path = r"/res/allergen/"
        # 获取指定路径下的所有文件名
        filenames = os.listdir(path)
        self.ui.modeBox_3.clear()
        # 输出所有文件名
        for filename in filenames:
            # self.ui.modeBox_3.clear()
            self.ui.modeBox_3.addItem(filename)
            self.ui.modeBox_3.setCurrentIndex(-1)

    """
    @detail 确认按钮操作
    @detail 槽函数
    """
    @Slot()
    def on_btnConfirm_clicked(self):
        if self.ui.modeBox_3.currentIndex() == -1:
            # m_title = ""
            # m_info = "未选择试剂卡规格！"
            # infoMessage(m_info, m_title, 300)
            info = "未选择试剂卡规格！"
            self.update_info.emit(info)
        else:
            self.resetBtn_2()
            self.ui.btnConfirm.hide()
            self.ui.stackedWidget.setCurrentIndex(1)

            time = "%s-%s-%s" % (
                self.ui.dateBox.date().year(), self.ui.dateBox.date().month(), self.ui.dateBox.date().day())
            time = self.ui.dateBox.date().toString("yyyy-MM-dd")
            # time = self.ui.dateBox.currentText()
            item_type = self.ui.modeBox_3.currentText()
            doctor = self.ui.lineEdit.text()
            depart = self.ui.lineEdit_2.text()
            self.selectMysql(time, item_type, doctor, depart)

    """
    @detail 上一页按钮操作
    @detail 槽函数
    """
    @Slot()
    def on_btnPre_clicked(self):
        self.setHistoryTable(2)

    """
    @detail 下一页按钮操作
    @detail 槽函数
    """
    @Slot()
    def on_btnNext_clicked(self):
        self.setHistoryTable(3)

    """
    @detail 详情按钮操作
    @detail 槽函数
    """
    @Slot()
    def on_btnDetail_clicked(self):
        if self.ui.historyTable.currentIndex().row() == -1:
            # m_title = "错误"
            # m_title = ""
            # m_info = "未选择试剂卡！"
            # infoMessage(m_info, m_title, 300)
            info = "未选择试剂卡！"
            self.update_info.emit(info)
            return
        else:
            # 点击空白不显示
            current_row = self.ui.historyTable.currentIndex().row()
            if current_row >= self.min_size:
                return
            else:
                # self.testinfo = MyTestInfo()
                # self.testinfo.setWindowModality(Qt.ApplicationModal)
                # self.testinfo.show()
                self.next_page.emit('DataPage')
                self.changePhoto(current_row)
                return
            self.resetBtn_3()
            # self.ui.btnReturn.setGeometry(539, 10, 254, 80)
            self.ui.btnReturn.setGeometry(601, 10, 187, 80)
            self.ui.btnReport.show()
            self.ui.btnDownload.show()
            self.ui.btnPrint.show()
            self.ui.stackedWidget.setCurrentIndex(2)

    """
    @detail 返回按钮操作
    @detail 槽函数
    """
    @Slot()
    def on_btnReturn_clicked(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            page_msg = 'HomePage'
            self.next_page.emit(page_msg)
        elif self.ui.stackedWidget.currentIndex() == 1:
            self.resetBtn_3()
            self.ui.btnReturn.setGeometry(410, 10, 380, 80)
            self.ui.btnConfirm.show()
            self.ui.stackedWidget.setCurrentIndex(0)
        elif self.ui.stackedWidget.currentIndex() == 2:
            self.resetBtn()
            self.resetBtn_2()
        elif self.ui.stackedWidget.currentIndex() == 3:
            self.resetBtn()
            self.resetBtn_2()