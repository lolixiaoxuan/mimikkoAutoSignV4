# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import auth_pb2 as proto_dot_auth__pb2


class AuthStub(object):
    """https://api4.mimikko.cn/com.mimikko.app.api.idp.view.Auth/Login

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/com.mimikko.app.api.idp.view.Auth/Login',
                request_serializer=proto_dot_auth__pb2.LoginRequest.SerializeToString,
                response_deserializer=proto_dot_auth__pb2.response.FromString,
                )


class AuthServicer(object):
    """https://api4.mimikko.cn/com.mimikko.app.api.idp.view.Auth/Login

    """

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=proto_dot_auth__pb2.LoginRequest.FromString,
                    response_serializer=proto_dot_auth__pb2.response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.mimikko.app.api.idp.view.Auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Auth(object):
    """https://api4.mimikko.cn/com.mimikko.app.api.idp.view.Auth/Login

    """

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mimikko.app.api.idp.view.Auth/Login',
            proto_dot_auth__pb2.LoginRequest.SerializeToString,
            proto_dot_auth__pb2.response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
