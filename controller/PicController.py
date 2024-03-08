"""
@Description：图像算法控制类
@Author：mysondrink@163.com
@Time：2024/1/15 17:16
"""
import time
import grpc
try:
    import util.frozen as frozen
    from controller.AbstractThread import AbstractThread
    from pic_code.img_main import img_main
    from api.imgprocess.v1 import imgprocess_pb2_grpc, imgprocess_pb2
    from api.helloworld.v1 import helloworld_pb2, helloworld_pb2_grpc
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.controller.AbstractThread import AbstractThread
    from qt0223.pic_code.img_main import img_main
    from qt0223.api.imgprocess.v1 import imgprocess_pb2_grpc, imgprocess_pb2
    from qt0223.api.helloworld.v1 import helloworld_pb2, helloworld_pb2_grpc


TIME_TO_SLEEP = 2
TRYLOCK_TIME = -1
FAILED_CODE = 404
SUCCEED_CODE = 202


class MyPicThread(AbstractThread):
    def __init__(self):
        """
        初始化线程
        构造函数
        """
        super().__init__()
        self.judge_flag = True

    def run(self):
        """
        线程运行函数
        进行图片的获取和图片pixel的获取
        Returns:
            None
        """
        item_type = "检测组合" + self.item_type
        try:
            print("Will try to imgprocess...")
            with grpc.insecure_channel("localhost:50051") as channel:
                stub = imgprocess_pb2_grpc.ImgProcesserStub(channel)
                response: imgprocess_pb2_grpc.ImgProcesserStub = stub.ImgProcess(
                    imgprocess_pb2.ImgProcessRequest(name=f"{item_type}"),
                    timeout=30
                )
                time.sleep(TIME_TO_SLEEP)
                if response.code != 202:
                    raise Exception
            self.update_json.emit(
                dict(
                    timenow=response.message,
                    flag=True,
                )
            )
        except Exception as e:
            self.update_json.emit(
                dict(
                    timenow=response.message,
                    flag=False,
                )
            )
            self.sendException()

    def setType(self, item_type):
        """
        设置需要检测的试剂卡型号
        Args:
            item_type: 试剂卡型号

        Returns:
            None
        """
        self.item_type = item_type
