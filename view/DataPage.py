import os
import re
import cv2 as cv
import datetime
import numpy as np
try:
    from view.gui.info import *
    import util.frozen as frozen
    from util import dirs
    from util.report import MyReport
    from view.AbstractPage import AbstractPage, ProcessDialog
    from controller.USBController import CheckUSBThread
    import middleware.database as insertdb
except ModuleNotFoundError:
    from qt0223.view.gui.info import *
    import qt0223.util.frozen as frozen
    from qt0223.util import dirs
    from qt0223.util.report import MyReport
    from qt0223.view.AbstractPage import AbstractPage, ProcessDialog
    from qt0223.controller.USBController import CheckUSBThread
    import qt0223.middleware.database as insertdb



class DataPage(Ui_Form, AbstractPage):
    def __init__(self):
        """
        继承父类构造函数
        初始化数据展示界面，同时创建记录异常的信息
        """
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
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(3)  # 取消图片显示
        self.ui.btnPic.hide()
        self.setBtnIcon()
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.photoLabel.setText("")
        self.ui.picLabel.setText("")

    def closeEvent(self, event) -> None:
        """
        窗口关闭事件
        Args:
            event: 响应事件，窗口关闭

        Returns:
            None
        """
        self.setParent(None)
        event.accept()  # 表示同意了，结束吧

    def setBtnIcon(self) -> None:
        """
        设置按钮图标
        Returns:
            None
        """
        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnData.setIconSize(QSize(32, 32))
        self.ui.btnData.setIcon(QIcon(confirm_icon_path))

        switch_icon_path = frozen.app_path() + r"/res/icon/switch.png"
        self.ui.btnPic.setIconSize(QSize(32, 32))
        self.ui.btnPic.setIcon(QIcon(switch_icon_path))

        exe_icon_path = frozen.app_path() + r"/res/icon/exe.png"
        self.ui.btnPrint.setIconSize(QSize(32, 32))
        self.ui.btnPrint.setIcon(QIcon(exe_icon_path))

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnReport.setIconSize(QSize(32, 32))
        self.ui.btnReport.setIcon(QIcon(confirm_icon_path))

        exe_icon_path = frozen.app_path() + r"/res/icon/compute.png"
        self.ui.btnDownload.setIconSize(QSize(32, 32))
        self.ui.btnDownload.setIcon(QIcon(exe_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

    # this is a data get slot
    def getData(self, msg) -> None:
        """
        获取信息
        信息来自TestPage和HistoryPage页面，信息包括图片信息和数据库信息
        Args:
            msg: 信号，发送来的信息

        Returns:
            None
        """
        # print(msg['info'])
        # self.writeFile(msg['data'])
        print("datapage id: ", id(self))
        flag = 0
        pic_para = 1
        self.info = msg['info']
        self.data = msg['data']
        self.row_exetable = int(self.data['row_exetable'])
        self.column_exetable = int(self.data['column_exetable'])

        # print("row,column:", self.row_exetable, self.column_exetable)
        name_pic = self.data['name_pic']
        cur_time = self.data['time']
        pic_path = self.data['pic_path']
        self.test_time = cur_time[0] + ' ' + cur_time[1]
        reagent_matrix_info = self.data['reagent_matrix_info']
        self.pix_table_model = QStandardItemModel(
            self.row_exetable + int(self.row_exetable / 2), self.column_exetable
        )
        self.pix_table_model_copy = QStandardItemModel(
            self.row_exetable + int(self.row_exetable / 2) + 2,
            self.column_exetable
        )
        self.ui.tableView.setModel(self.pix_table_model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().close()
        self.ui.tableView.verticalHeader().close()
        # self.ui.tableView.setGridStyle(Qt.NoPen)

        self.ui.tableView_2.setModel(self.pix_table_model_copy)
        self.ui.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView_2.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView_2.horizontalHeader().close()
        self.ui.tableView_2.verticalHeader().close()
        self.ui.tableView_2.setGridStyle(Qt.NoPen)

        self.ui.rightLabel.setText(self.test_time)
        self.ui.leftLabel.setText(self.test_time)

        self.pic_para = 1
        if self.info == 201:
            self.point_list = self.data['point_str']
            gray_row = self.data['gray_row']
            gray_column = self.data['gray_column']
            gray_aver = self.data['gray_aver'][1:]
            for i in range(self.row_exetable + int(self.row_exetable / 2)):
                if i % 3 != 0:
                    for j in range(self.column_exetable):
                        if i - flag < gray_row and j < gray_column:
                            # item = QStandardItem(str(gray_aver[i - flag][j]))
                            # pix_num = int(gray_aver[i - flag][j])
                            pix_num = int(float(gray_aver[i - flag][j]) * self.pic_para)
                            # pix_num = random.randint(15428, 16428)
                            item = QStandardItem(str(pix_num))
                        else:
                            item = QStandardItem(str(0))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.pix_table_model.setItem(i, j, item)
                else:
                    # num = i % 3
                    for j in range(0, self.column_exetable):
                        if j < gray_column:
                            # item = QStandardItem(reagent_matrix_info[num][j])
                            item = QStandardItem(reagent_matrix_info[flag][j])
                        else:
                            item = QStandardItem(str(0))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.pix_table_model.setItem(i, j, item)
                    flag += 1

            self.insertMysql(name_pic, cur_time)  # 图片数据信息存入数据库
        elif self.info == 202:
            self.allergy_info = reagent_matrix_info
            point_str = self.data['point_str']
            self.showDataView(point_str + ',' + reagent_matrix_info)

        self.setTableWidget(self.data['item_type'], self.allergy_info, self.data['nature_aver_str'])

    def insertMysql(self, name_pic, cur_time) -> None:
        """
        需要修改
        连接数据库，写入图片信息
        Args:
            name_pic: 保存图片的图片名
            cur_time: 测试事件

        Returns:
            None
        """
        reagent_matrix_info = str(self.readPixtable())
        point_str = self.data['point_str']
        self.showDataView(point_str + "," + reagent_matrix_info)
        self.allergy_info = reagent_matrix_info
        patient_id = self.data['patient_id']

        patient_name = self.data['patient_name']
        patient_age = self.data['patient_age']
        patient_gender = self.data['patient_gender']
        item_type = self.data['item_type']
        pic_name = name_pic
        doctor = self.data['doctor']
        depart = self.data['depart']
        age = self.data['age']
        name = self.data['name']
        matrix = self.data['matrix']
        code_num = self.data['code_num']
        points = self.data['point_str']
        gray_aver = self.data['gray_aver_str']
        nature_aver = self.data['nature_aver_str']
        try:
            data_1 = [
                    patient_name,
                    patient_id,
                    patient_age,
                    patient_gender
                ]
            data_2 = [
                    item_type, patient_id, pic_name, cur_time[0],
                    code_num, doctor, depart, matrix, cur_time[1],
                    reagent_matrix_info, name, age, patient_gender,
                    points, gray_aver, nature_aver
                ]
            # 提交事务
            insertdb.insertMySql(data_1, data_2)
        except Exception as e:
            print(e)

    def setTableWidget(self, item_type, reagent_info, nature_aver_str):
        v = QVBoxLayout()
        text = MyReport().gethtml(item_type, reagent_info, nature_aver_str)
        self.myreport = QTextEdit()
        # 姓名，性别，样本号，条码号，样本类型，测试时间，【结果】，打印时间
        # cur_time[0] + ' ' + cur_time[1]
        str_list = [self.data['patient_name'], self.data['patient_gender'], self.data['patient_id'],
                    self.data['code_num'], self.data['item_type'],
                    self.data['time'][0] + ' ' + self.data['time'][1],
                    text[1], '']
        self.myreport.setHtml(text[0] % tuple(str_list))

        v.addWidget(self.myreport)
        self.ui.tableWidget.setLayout(v)

    def readPixtable(self) -> str:
        """
        读取表格内容，同时以str形式保存到数据库
        Returns:
            str
        """
        reagent_matrix_info = []
        for i in range(self.row_exetable + int(self.row_exetable / 2)):
            for j in range(self.column_exetable):
                index = self.pix_table_model.index(i, j)
                data = self.pix_table_model.data(index)
                reagent_matrix_info.append(str(data))
        return ",".join(reagent_matrix_info)

    def getUSBInfo(self, msg) -> None:
        """
        U盘提示信息
        Args:
            msg: U盘信息

        Returns:
            None
        """
        if msg == 202:
            self.usbthread.deleteLater()
            # m_title = ""
            # m_info = "下载完成！"
            # infoMessage(m_info, m_title, 300)
            info = "下载完成！"
            self.showInfoDialog(info)
        elif msg == 404:
            self.usbthread.deleteLater()
            # m_title = ""
            # m_info = "U盘未插入或无法访问！"
            # infoMessage(m_info, m_title)
            info = "U盘未插入或无法访问！"
            self.showInfoDialog(info)
        elif msg == 405:
            self.usbthread.deleteLater()
            # m_title = ""
            # m_info = "图片读取失败或未找到图片！"
            # infoMessage(m_info, m_title)
            info = "图片读取失败或未找到图片！"
            self.showInfoDialog(info)

    """
    @detail 读取下传文件
    @detail 测试代码
    """

    def writeFile(self, msg):
        # file_path = os.path.join(r'/', "example.txt")
        with open("./example.txt", "w") as f:
            f.write(str(msg))

    """
    @detail 数据展示
    """

    def showDataView(self, data):
        title_list = ["定位点", "", "", "", "定位点"]
        data_copy = re.split(r",", data)
        data_copy = title_list + data_copy
        row = self.pix_table_model_copy.rowCount()
        column = self.pix_table_model_copy.columnCount()
        for i in range(row):
            for j in range(column):
                pix_num = data_copy[i * column + j]
                item = QStandardItem(str(pix_num))
                item.setTextAlignment(Qt.AlignCenter)
                self.pix_table_model_copy.setItem(i, j, item)
        return

    """
    @detail 打印按钮操作
    @detail 槽函数
    """

    @Slot()
    def on_btnPrint_clicked(self):
        info = "打印中。。。"
        dialog = ProcessDialog()
        dialog.setInfo(info)
        dialog.setParent(self)
        dialog.hideBtn()
        dialog.show()
        print("print")
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        test_time = self.test_time
        Data_Base = [self.data['patient_name'], self.data['patient_gender'], self.data['patient_id'],
                    self.data['code_num'], '检测组合' + self.data['item_type'], test_time, time_now]
        gray_aver_str = self.data['gray_aver_str'].split(",")
        nature_aver_str = self.data['nature_aver_str'].split(",")
        array_gray_aver = np.array(gray_aver_str)
        array_nature_aver = np.array(nature_aver_str)
        matrix_gray_aver = array_gray_aver.reshape(9, 5)
        matrix_nature_aver = array_nature_aver.reshape(9, 5)
        Data_Nature = matrix_nature_aver
        Data_Light = matrix_gray_aver
        return
        # myEm5822_Print = Em5822_Print()
        # myEm5822_Print.em5822_print(Data_Base, Data_Nature, Data_Light)
        # m_title = ""
        # m_info = "输出表格成功!"
        # infoMessage(m_info, m_title, 300)
        Main = img_main()
        if Main.natPrint(Data_Base, Data_Nature, Data_Light):
            dialog.closeDialog()
            info = "输出表格成功!"
            self.update_info.emit(info)
        else:
            dialog.closeDialog()
            info = "输出表格失败!"
            self.update_info.emit(info)

    """
    @detail 下载按钮操作
    @detail 槽函数
    """

    @Slot()
    def on_btnDownload_clicked(self):
        print("Download")
        name = self.data['name_pic']
        path = self.data['pic_path']
        data = self.data
        self.usbthread = CheckUSBThread(name, path, data, self.data['point_str'] + ',' + self.allergy_info)
        self.usbthread.update_json.connect(self.getUSBInfo)
        # 创建定时器
        self.download_timer = QTimer()
        self.download_timer.timeout.connect(self.usbthread.start)
        self.download_timer.timeout.connect(self.download_timer.stop)
        # 设置定时器延迟时间，单位为毫秒
        # 延迟2秒跳转
        delay_time = 2000
        self.download_timer.start(delay_time)
        m_title = ""
        m_info = "下载中..."
        # infoMessage(m_info, m_title, 300)
        info = "下载中..."
        self.showInfoDialog(info)

    """
    @detail 数据按钮操作
    @detail 槽函数
    """

    @Slot()
    def on_btnData_clicked(self):
        # self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.stackedWidget.setCurrentIndex(3)

    """
    @detail 图片按钮操作
    @detail 槽函数
    """

    @Slot()
    def on_btnPic_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    """
    @detail 报告单按钮操作
    @detail 槽函数
    """

    @Slot()
    def on_btnReport_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    """
    @detail 返回按钮操作
    @detail 槽函数
    """

    @Slot()
    def on_btnReturn_clicked(self):
        if self.info == 201:
            page_msg = 'TestPage'
            self.next_page.emit(page_msg)
        elif self.info == 202:
            page_msg = 'history'
            self.next_page.emit(page_msg)