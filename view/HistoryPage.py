import os
import shutil
import datetime
import sys
import math
import sqlite3
try:
    from third_party.keyboard.keyboard import KeyBoard
    from view.gui.history import *
    from util import dirs
    import util.frozen as frozen
    from util.report import MyReport
    from view.AbstractPage import AbstractPage
    import middleware.database as insertdb
except ModuleNotFoundError:
    from qt0922.third_party.keyboard.keyboard import KeyBoard
    from qt0922.view.gui.history import *
    from qt0922.util import dirs
    import qt0922.util.frozen as frozen
    from qt0922.util.report import MyReport
    from qt0922.view.AbstractPage import AbstractPage
    import qt0922.middleware.database as insertdb

page_dict = {'page': 0, 'page_2': 1, 'page_3': 2, 'page_4': 3}
header_list = ["试剂卡编号", "采样时间",  "病人编号" , "病人姓名"]
SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'


class HistoryPage(Ui_Form, AbstractPage):
    next_page = Signal(str)
    update_json = Signal(dict)
    update_log = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()
        self.page_size = 5

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

    def installEvent(self):
        for item in self.focuswidget:
            item.installEventFilter(self)

    def setFocusWidget(self):
        self.focuswidget = [self.ui.lineEdit, self.ui.lineEdit_2]
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
        if obj_name == "lineEdit":
            self.keyboardtext.nameLabel.setText("送检医生")
        elif obj_name == "lineEdit_2":
            self.keyboardtext.nameLabel.setText("科室")
        self.keyboardtext.showWindow()

    def getKeyBoardText(self, msg):
        self.focusWidget().setText(msg)
        self.focusWidget().clearFocus()

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

    def resetBtn(self):
        self.ui.btnReport.setText('报告单')
        self.ui.btnReport.hide()
        self.ui.btnDownload.hide()
        self.ui.btnPrint.hide()
        self.ui.stackedWidget.setCurrentIndex(1)

    def resetBtn_2(self):
        self.ui.btnNext.show()
        self.ui.btnPre.show()
        self.ui.btnDetail.show()
        self.ui.btnReturn.setGeometry(601, 10, 187, 80)

    def resetBtn_3(self):
        self.ui.btnNext.hide()
        self.ui.btnPre.hide()
        self.ui.btnDetail.hide()

    def setHistoryTable(self):
        if self.page_num < 1:
            self.page_num = 1
            info = "已经是第一页!"
            self.update_info.emit(info)
            return
        elif self.page_num > self.total_page:
            self.page_num = self.total_page
            info = "已经是最后一页!"
            self.update_info.emit(info)
            return

        # get select reagent info
        self.sql_syntax[-1] = (self.page_num - 1) * self.page_size
        patient_id_list, time_list, reagent_id_list, name_list = insertdb.getSQLiteInfo(*self.sql_syntax)

        # set history table to display
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
        for i in range(len(time_list)):
            for j in range(len(header_list)):
                if j == 1:
                    item = QStandardItem(time_list[i][10:])
                elif j == 2:
                    item = QStandardItem(patient_id_list[i])
                elif j == 3:
                    # item = QStandardItem(self.patient_name_list[i])
                    item = QStandardItem(name_list[i])
                else:
                    item = QStandardItem(reagent_id_list[i])
                item.setTextAlignment(Qt.AlignCenter)
                self.select_table_model.setItem(i, j, item)
                # self.select_table_model.setItem(i, j, item)

        # self.ui.historyTable.currentChanged(self.changePhoto) # 选中时改变图片
        # self.ui.historyTable.selectionModel().currentChanged.connect(self.changePhoto)
        # self.ui.btnDetail.clicked.connect(self.changePhoto)

    def getTotalPage(self, time, item_type, doctor, depart):
        offset = 0
        if doctor != '':
            sql = """
            SELECT * FROM reagent_copy1 WHERE reagent_type LIKE '%' || ? AND reagent_time = ? AND doctor = ?;
            """
            sql_2 = """
            SELECT * FROM reagent_copy1 WHERE reagent_type LIKE '%' || ? AND reagent_time = ? AND doctor = ? LIMIT 5 OFFSET ?;
            """
            self.sql_total = [sql, item_type, time, doctor]
            self.sql_syntax = [sql_2, item_type, time, doctor, offset]
        elif depart != '':
            sql = """
            SELECT * FROM reagent_copy1 WHERE reagent_type LIKE '%' || ? AND reagent_time = ? AND doctor = ? AND depart = ?;
            """
            sql_2 = """
            SELECT * FROM reagent_copy1 WHERE reagent_type LIKE '%' || ? AND reagent_time = ? AND doctor = ? AND depart = ? LIMIT 5 OFFSET ?;
            """
            self.sql_total = [sql, item_type, time, doctor, depart]
            self.sql_syntax = [sql_2, item_type, time, doctor, depart, offset]
        else:
            # MySQL语句
            sql = """
            SELECT * FROM reagent_copy1 WHERE reagent_type LIKE '%' || ? AND reagent_time = ?;
            """
            sql_2 = """
            SELECT * FROM reagent_copy1 WHERE reagent_type LIKE '%' || ? AND reagent_time = ? LIMIT 5 OFFSET ?;
            """
            self.sql_total = [sql, item_type, time]
            self.sql_syntax = [sql_2, item_type, time, offset]
        # SELECT * FROM users LIMIT 10 OFFSET 20;
        return  math.ceil(insertdb.totalPage(*self.sql_total) / self.page_size)

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
            self.page_num = 1
            time = "%s-%s-%s" % (
                self.ui.dateBox.date().year(), self.ui.dateBox.date().month(), self.ui.dateBox.date().day())
            time = self.ui.dateBox.date().toString("yyyy-MM-dd")
            # time = self.ui.dateBox.currentText()
            item_type = self.ui.modeBox_3.currentText()
            doctor = self.ui.lineEdit.text()
            depart = self.ui.lineEdit_2.text()
            self.total_page = self.getTotalPage(time, item_type, doctor, depart)
            self.setHistoryTable()

    @Slot()
    def on_btnPre_clicked(self):

        self.page_num = self.page_num - 1
        self.setHistoryTable()

    @Slot()
    def on_btnNext_clicked(self):

        self.page_num = self.page_num + 1
        self.setHistoryTable()

    @Slot()
    def on_btnDetail_clicked(self):
 
        current_row = self.ui.historyTable.currentIndex().row()
        item = self.select_table_model.item(current_row, 0)
        if item is None:
            return
        reagent_id = item.text()
        page_msg = 'DataPage'
        self.next_page.emit(page_msg)
        # self.changePhoto(reagent_id)
        data_json = insertdb.changePhoto(reagent_id)
        info_msg = 202
        self.update_json.emit(dict(info=info_msg, data=data_json))

    @Slot()
    def on_btnReturn_clicked(self):

        if self.ui.stackedWidget.currentIndex() == 0:
            page_msg = 'HomePage'
            self.next_page.emit(page_msg)
        elif self.ui.stackedWidget.currentIndex() == 1:
            self.ui.historyTable.setModel(None)
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