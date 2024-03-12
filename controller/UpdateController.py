import time
import grpc
try:
    from api.update.v1 import update_pb2, update_pb2_grpc
    import util.frozen as frozen
    from controller.AbstractThread import AbstractThread
except ModuleNotFoundError:
    from qt0922.api.update.v1 import update_pb2, update_pb2_grpc
    import qt0922.util.frozen as frozen
    from qt0922.controller.AbstractThread import AbstractThread

TIME_TO_SLEEP = 2
TRYLOCK_TIME = -1
FAILED_CODE = 404
SUCCEED_CODE = 202

MY_ZIP = frozen.app_path() + r'/update.zip'
MY_DIR = frozen.app_path()


class MyUpdateThread(AbstractThread):
    def __init__(self):
        super().__init__()

    def run(self):
        try:
            # client of update server
            print("Will try to update ...")
            # request connect to update server
            with grpc.insecure_channel("localhost:50051") as channel:
                stub = update_pb2_grpc.UpdaterStub(channel)
                response: update_pb2_grpc.UpdaterStub = stub.UpdateSoftware(
                    update_pb2.UpdateRequest(name="updatecontroller"),
                    timeout=10
                )
                time.sleep(TIME_TO_SLEEP)
                if response.code == 202:
                    info_msg = "更新成功！"
                    code_msg = SUCCEED_CODE
                    status_msg = self.currentThread()
                    self.update_json.emit(
                        dict(
                            info=info_msg,
                            code=code_msg,
                            status=status_msg
                        )
                    )
                else:
                    raise Exception
        except Exception as e:
            self.sendException()
            info_msg = "更新失败！"
            code_msg = FAILED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            # if os.path.exists(MY_ZIP):
            #     os.remove(MY_ZIP)
        finally:
            self.log_thread.deleteLater()
            # if os.path.exists(MY_ZIP):
            #     os.remove(MY_ZIP)
