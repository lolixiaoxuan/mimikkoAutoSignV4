# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import energy_pb2 as proto_dot_energy__pb2


class EnergyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListEnergySourceModel = channel.unary_unary(
                '/com.mimikko.app.api.general.energy.Energy/ListEnergySourceModel',
                request_serializer=proto_dot_energy__pb2.ListEnergySourceModelRequest.SerializeToString,
                response_deserializer=proto_dot_energy__pb2.response.FromString,
                )
        self.ListEnergySourceRecord = channel.unary_unary(
                '/com.mimikko.app.api.general.energy.Energy/ListEnergySourceRecord',
                request_serializer=proto_dot_energy__pb2.ListEnergySourceRecordRequest.SerializeToString,
                response_deserializer=proto_dot_energy__pb2.response2.FromString,
                )
        self.CreateEnergySourceRecord = channel.unary_unary(
                '/com.mimikko.app.api.general.energy.Energy/CreateEnergySourceRecord',
                request_serializer=proto_dot_energy__pb2.CreateEnergySourceRecordRequest.SerializeToString,
                response_deserializer=proto_dot_energy__pb2.response3.FromString,
                )
        self.ReceiveEnergySourceReward = channel.unary_unary(
                '/com.mimikko.app.api.general.energy.Energy/ReceiveEnergySourceReward',
                request_serializer=proto_dot_energy__pb2.ReceiveEnergySourceRewardRequest.SerializeToString,
                response_deserializer=proto_dot_energy__pb2.response4.FromString,
                )


class EnergyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListEnergySourceModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEnergySourceRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEnergySourceRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveEnergySourceReward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EnergyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListEnergySourceModel': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEnergySourceModel,
                    request_deserializer=proto_dot_energy__pb2.ListEnergySourceModelRequest.FromString,
                    response_serializer=proto_dot_energy__pb2.response.SerializeToString,
            ),
            'ListEnergySourceRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEnergySourceRecord,
                    request_deserializer=proto_dot_energy__pb2.ListEnergySourceRecordRequest.FromString,
                    response_serializer=proto_dot_energy__pb2.response2.SerializeToString,
            ),
            'CreateEnergySourceRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEnergySourceRecord,
                    request_deserializer=proto_dot_energy__pb2.CreateEnergySourceRecordRequest.FromString,
                    response_serializer=proto_dot_energy__pb2.response3.SerializeToString,
            ),
            'ReceiveEnergySourceReward': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveEnergySourceReward,
                    request_deserializer=proto_dot_energy__pb2.ReceiveEnergySourceRewardRequest.FromString,
                    response_serializer=proto_dot_energy__pb2.response4.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.mimikko.app.api.general.energy.Energy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Energy(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListEnergySourceModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mimikko.app.api.general.energy.Energy/ListEnergySourceModel',
            proto_dot_energy__pb2.ListEnergySourceModelRequest.SerializeToString,
            proto_dot_energy__pb2.response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListEnergySourceRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mimikko.app.api.general.energy.Energy/ListEnergySourceRecord',
            proto_dot_energy__pb2.ListEnergySourceRecordRequest.SerializeToString,
            proto_dot_energy__pb2.response2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateEnergySourceRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mimikko.app.api.general.energy.Energy/CreateEnergySourceRecord',
            proto_dot_energy__pb2.CreateEnergySourceRecordRequest.SerializeToString,
            proto_dot_energy__pb2.response3.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveEnergySourceReward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mimikko.app.api.general.energy.Energy/ReceiveEnergySourceReward',
            proto_dot_energy__pb2.ReceiveEnergySourceRewardRequest.SerializeToString,
            proto_dot_energy__pb2.response4.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
