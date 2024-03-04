"""
@Description：
@Author：mysondrink@163.com
@Time：2024/2/26 11:13
"""
from concurrent import futures
import logging

import grpc
try:
    from api.helloworld.v1 import helloworld_pb2, helloworld_pb2_grpc
except ModuleNotFoundError:
    from qt0223.api.helloworld.v1 import helloworld_pb2, helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReplyAgain(message=f"Hello again, {request.name}!", code=202)


def serve():
    port = "50051"
    # 实例化server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册逻辑到server中
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    # 启动server
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()