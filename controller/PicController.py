import time
import grpc
try:
    import util.frozen as frozen
    from controller.AbstractThread import AbstractThread
    from api.imgprocess.v1 import imgprocess_pb2_grpc, imgprocess_pb2
    from api.helloworld.v1 import helloworld_pb2, helloworld_pb2_grpc
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen
    from qt0922.controller.AbstractThread import AbstractThread
    from qt0922.api.imgprocess.v1 import imgprocess_pb2_grpc, imgprocess_pb2
    from qt0922.api.helloworld.v1 import helloworld_pb2, helloworld_pb2_grpc


TIME_TO_SLEEP = 2
TRYLOCK_TIME = -1
FAILED_CODE = 404
SUCCEED_CODE = 202


class MyPicThread(AbstractThread):
    def __init__(self):
        super().__init__()
        self.judge_flag = True

    def run(self):
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
        self.item_type = item_type
