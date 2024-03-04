"""
@Description：图像算法控制类
@Author：mysondrink@163.com
@Time：2024/1/15 17:16
"""
from PySide2.QtCore import QThread, Signal, QDateTime
import datetime
try:
    import util.frozen as frozen
    from controller.AbstractThread import AbstractThread
    from pic_code.img_main import img_main
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.controller.AbstractThread import AbstractThread
    from qt0223.pic_code.img_main import img_main

#   定位点圈定区域，可修改
roi_position = [
    [0, 700], [0, 2500]  # [startY, endY] [StartX, endX]
]


class MyPicThread(AbstractThread):
    # update_fail = Signal()
    # update_success = Signal()
    finished = Signal(str)

    """
    @detail 初始化线程，同时创建记录异常的信息
    @detail 构造函数
    """

    def __init__(self):
        super().__init__()
        self.gray_aver = []
        self.judge_flag = 0
        self.nature_aver = []
        self.gray_aver_str = []
        self.nature_aver_str = []

    """
    @detail 线程运行函数
    @detail 进行图片的获取和图片pixel的获取
    """

    def run(self):
        pic_path = QDateTime.currentDateTime().toString('yyyy-MM-dd')
        time_now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        path_cache = frozen.app_path() + r'/pic_code/img/img_cache/'
        path_save = frozen.app_path() + r'/pic_code/img/img_tem/'
        Main = img_main()
        Camera_Init_flag = Main.imgAcquire(
            path_chache=path_cache,
            path_save=path_save,
            name="%s" % time_now
        )
        if Camera_Init_flag is not True:
            return

        item_type = "检测组合" + self.item_type
        # judge_flag, self.gray_aver, self.nature_aver = self.imgPro.process(
        #     path_read=frozen.app_path() + r'/third_party/img/picture/' + time_now + '.jpeg',
        #     path_write=frozen.app_path() + r'/third_party/img/img_out/', combina=item_type, radius=40)
        judge_flag, self.gray_aver, self.nature_aver = Main.imgProcess(
            read=frozen.app_path() + r'/pic_code/img/img_tem/' + time_now + '.jpeg',
            write=frozen.app_path() + r'/pic_code/img/img_out/',
            combina=item_type,
            radius=40
        )
        # judge_flag, self.gray_aver, self.nature_aver = Main.imgProcess(
        #     read=frozen.app_path() + r'/pic_code/img/img_input/2.jpeg',
        #     write=frozen.app_path() + r'/pic_code/img/img_out/',
        #     combina=item_type,
        #     radius=40
        # )
        w, h = self.nature_aver.shape
        print(w, h)
        self.antibody_test_results = []
        self.antibody_test_points = []
        nature_aver_list = []
        gray_aver_list = []
        for i in range(w):
            for j in range(h):
                nature_aver_list.append(self.nature_aver[i][j])
                gray_aver_list.append(str(self.gray_aver[i][j]))
                # if (i * h + j) % 2 != 0:
                #     self.antibody_test_points.append(self.gray_aver[i + 1][j])
                # else:
                #     self.antibody_test_results.append(self.nature_aver[i][j])
        # print(self.gray_aver)
        # print(self.nature_aver)
        # for k in range(h):
        #     self.gray_aver_str += "," + str(self.gray_aver[w][k])
        # print(self.nature_aver_str)
        # print(self.gray_aver_str)
        self.nature_aver_str = ",".join(nature_aver_list)
        self.gray_aver_str = ",".join(gray_aver_list)
        print("finished!")
        self.finished.emit(time_now)
        self.judge_flag = judge_flag


    """
    @detail 获取图片pixel信息
    """

    def getGrayAver(self):
        return self.judge_flag, self.gray_aver, self.nature_aver, self.gray_aver_str, self.nature_aver_str

    def setType(self, item_type):
        self.item_type = item_type
