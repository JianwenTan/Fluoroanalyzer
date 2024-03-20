from concurrent import futures
import logging
import sys
import datetime
sys.path.append("..")

import tempfile
import zipfile
import shutil
import os
import grpc
try:
    from api.helloworld.v1 import helloworld_pb2, helloworld_pb2_grpc
    from api.update.v1 import update_pb2, update_pb2_grpc
    from api.imgprocess.v1 import imgprocess_pb2, imgprocess_pb2_grpc
    from pic_code.img_main import img_main
    import middleware.database as insertdb
    import util.frozen as frozen
except ModuleNotFoundError:
    from qt0922.api.helloworld.v1 import helloworld_pb2, helloworld_pb2_grpc
    from qt0922.api.update.v1 import update_pb2, update_pb2_grpc
    from qt0922.api.imgprocess.v1 import imgprocess_pb2, imgprocess_pb2_grpc
    import qt0922.util.frozen as frozen
    from qt0922.pic_code.img_main import img_main
    import qt0922.middleware.database as insertdb


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        """
        测试代码
        Args:
            request:
            context:

        Returns:

        """
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

    def SayHelloAgain(self, request, context):
        """
        测试代码
        Args:
            request:
            context:

        Returns:

        """
        return helloworld_pb2.HelloReplyAgain(message=f"Hello again, {request.name}!", code=202)


class Updater(update_pb2_grpc.UpdaterServicer):
    def UpdateSoftware(self, request, context):
        """
        进行软件升级
        返回升级后的结果，成功或失败
        Args:
            request: 来自客户端的请求，request定义的格式在protobuf
            context: 上下文内容

        Returns:
            Reply: grpc生成的reply，定义的格式在protobuf
        """
        # print(request.name)
        MY_ZIP = frozen.app_path() + r'/update.zip'
        try:
            # creating a template directory to unzip file
            with tempfile.TemporaryDirectory() as tempdir:
                with zipfile.ZipFile(MY_ZIP, 'r') as zip_ref:
                    zip_ref.extractall(tempdir)
                # copying tempfile to target directory
                flag = shutil.copytree(tempdir, os.path.dirname(os.path.dirname(MY_ZIP)), dirs_exist_ok=True)
                print("flag:", flag)
                msg = "succeed"
                code = 202
                return update_pb2.UpdateReply(message=msg, code=code)
        except Exception as e:
            if os.path.exists(MY_ZIP):
                os.remove(MY_ZIP)
            msg = "failed"
            code = 404
            return update_pb2.UpdateReply(message=msg, code=code)


class ImgProcesser(imgprocess_pb2_grpc.ImgProcesserServicer):
    def ImgProcess(self, request, context):
        """
        根据试剂卡格式type，进行图像处理，同时保存内容到数据库
        返回处理后的结果，成功或失败
        Args:
            request: 来自客户端的请求，request定义的格式在protobuf
            context: 上下文内容

        Returns:
            Reply: grpc生成的reply，定义的格式在protobuf
        """
        # print(request.name)
        pic_path = datetime.datetime.now().strftime("%Y-%m-%d")
        time_now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        path_cache = frozen.app_path() + r'/pic_code/dataset/img_result/img_cache/'
        path_save = frozen.app_path() + r'/pic_code/dataset/img_result/img_tem/'

        try:
            Main = img_main()
            Camera_Init_flag = Main.imgAcquire(
                path_chache=path_cache,
                path_save=path_save,
                name="%s" % time_now
            )
            if Camera_Init_flag is not True:
                raise Exception
            item_type = request.name
            judge_flag, gray_aver, nature_aver = Main.imgProcess(
                read=frozen.app_path() + r'/pic_code/dataset/img_result/img_tem/' + time_now + '.jpeg',
                write=frozen.app_path() + r'/pic_code/dataset/img_result/img_out/',
                combina=item_type,
                radius=40
            )
            if judge_flag is not True:
                raise Exception
            w, h = nature_aver.shape
            # print(w, h)

            # convert list result to str result
            # to insert database
            antibody_test_results = []
            antibody_test_points = []
            nature_aver_list = []
            gray_aver_list = []
            for i in range(w):
                for j in range(h):
                    nature_aver_list.append(nature_aver[i][j])
                    gray_aver_list.append(str(gray_aver[i][j]))
            nature_aver_str = ",".join(nature_aver_list)
            gray_aver_str = ",".join(gray_aver_list)

            # insert database
            data = dict(
                reagent_type=item_type,
                reagent_photo=time_now,
                gray_aver=gray_aver_str,
                nature_aver=nature_aver_str
            )
            insertdb.insertMySql(data)
            msg = "succeed"
            code = 202
            return imgprocess_pb2.ImgProcessReply(message=time_now, code=202)
        except Exception as e:
            msg = "failed"
            code = 404
            return imgprocess_pb2.ImgProcessReply(message=msg, code=code)


def serve():
    port = "50051"

    # instantiation server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # register instance to server
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    update_pb2_grpc.add_UpdaterServicer_to_server(Updater(), server)
    imgprocess_pb2_grpc.add_ImgProcesserServicer_to_server(ImgProcesser(), server)

    # activate server
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()