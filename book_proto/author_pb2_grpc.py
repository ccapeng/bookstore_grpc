# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from book_proto import author_pb2 as author__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AuthorControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
            '/author.AuthorController/List',
            request_serializer=author__pb2.AuthorListRequest.SerializeToString,
            response_deserializer=author__pb2.Author.FromString,
        )
        self.Create = channel.unary_unary(
            '/author.AuthorController/Create',
            request_serializer=author__pb2.Author.SerializeToString,
            response_deserializer=author__pb2.Author.FromString,
        )
        self.Retrieve = channel.unary_unary(
            '/author.AuthorController/Retrieve',
            request_serializer=author__pb2.AuthorRetrieveRequest.SerializeToString,
            response_deserializer=author__pb2.Author.FromString,
        )
        self.Update = channel.unary_unary(
            '/author.AuthorController/Update',
            request_serializer=author__pb2.Author.SerializeToString,
            response_deserializer=author__pb2.Author.FromString,
        )
        self.Destroy = channel.unary_unary(
            '/author.AuthorController/Destroy',
            request_serializer=author__pb2.Author.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class AuthorControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthorControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'List': grpc.unary_stream_rpc_method_handler(
            servicer.List,
            request_deserializer=author__pb2.AuthorListRequest.FromString,
            response_serializer=author__pb2.Author.SerializeToString,
        ),
        'Create': grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=author__pb2.Author.FromString,
            response_serializer=author__pb2.Author.SerializeToString,
        ),
        'Retrieve': grpc.unary_unary_rpc_method_handler(
            servicer.Retrieve,
            request_deserializer=author__pb2.AuthorRetrieveRequest.FromString,
            response_serializer=author__pb2.Author.SerializeToString,
        ),
        'Update': grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=author__pb2.Author.FromString,
            response_serializer=author__pb2.Author.SerializeToString,
        ),
        'Destroy': grpc.unary_unary_rpc_method_handler(
            servicer.Destroy,
            request_deserializer=author__pb2.Author.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'author.AuthorController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class AuthorController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
        return grpc.experimental.unary_stream(request, target, '/author.AuthorController/List',
                                              author__pb2.AuthorListRequest.SerializeToString,
                                              author__pb2.Author.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
               target,
               options=(),
               channel_credentials=None,
               call_credentials=None,
               insecure=False,
               compression=None,
               wait_for_ready=None,
               timeout=None,
               metadata=None):
        return grpc.experimental.unary_unary(request, target, '/author.AuthorController/Create',
                                             author__pb2.Author.SerializeToString,
                                             author__pb2.Author.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
        return grpc.experimental.unary_unary(request, target, '/author.AuthorController/Retrieve',
                                             author__pb2.AuthorRetrieveRequest.SerializeToString,
                                             author__pb2.Author.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
               target,
               options=(),
               channel_credentials=None,
               call_credentials=None,
               insecure=False,
               compression=None,
               wait_for_ready=None,
               timeout=None,
               metadata=None):
        return grpc.experimental.unary_unary(request, target, '/author.AuthorController/Update',
                                             author__pb2.Author.SerializeToString,
                                             author__pb2.Author.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        return grpc.experimental.unary_unary(request, target, '/author.AuthorController/Destroy',
                                             author__pb2.Author.SerializeToString,
                                             google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
