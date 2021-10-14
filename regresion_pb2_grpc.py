# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import onnx_pb2 as onnx__pb2
import regresion_pb2 as regresion__pb2
import solvers_dataset_pb2 as solvers__dataset__pb2


class RegresionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamLogs = channel.unary_stream(
                '/Regresion/StreamLogs',
                request_serializer=regresion__pb2.Empty.SerializeToString,
                response_deserializer=regresion__pb2.File.FromString,
                )
        self.MakeRegresion = channel.unary_unary(
                '/Regresion/MakeRegresion',
                request_serializer=solvers__dataset__pb2.DataSet.SerializeToString,
                response_deserializer=onnx__pb2.ONNX.FromString,
                )


class RegresionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamLogs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MakeRegresion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegresionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamLogs': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamLogs,
                    request_deserializer=regresion__pb2.Empty.FromString,
                    response_serializer=regresion__pb2.File.SerializeToString,
            ),
            'MakeRegresion': grpc.unary_unary_rpc_method_handler(
                    servicer.MakeRegresion,
                    request_deserializer=solvers__dataset__pb2.DataSet.FromString,
                    response_serializer=onnx__pb2.ONNX.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Regresion', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Regresion(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Regresion/StreamLogs',
            regresion__pb2.Empty.SerializeToString,
            regresion__pb2.File.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MakeRegresion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Regresion/MakeRegresion',
            solvers__dataset__pb2.DataSet.SerializeToString,
            onnx__pb2.ONNX.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
