# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
try:
    from api.update.v1 import update_pb2 as update__pb2
except ModuleNotFoundError:
    from qt0223.api.update.v1 import update_pb2 as update__pb2


class UpdaterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateSoftware = channel.unary_unary(
                '/Updater/UpdateSoftware',
                request_serializer=update__pb2.UpdateRequest.SerializeToString,
                response_deserializer=update__pb2.UpdateReply.FromString,
                )


class UpdaterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpdateSoftware(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UpdaterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateSoftware': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSoftware,
                    request_deserializer=update__pb2.UpdateRequest.FromString,
                    response_serializer=update__pb2.UpdateReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Updater', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Updater(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpdateSoftware(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Updater/UpdateSoftware',
            update__pb2.UpdateRequest.SerializeToString,
            update__pb2.UpdateReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)