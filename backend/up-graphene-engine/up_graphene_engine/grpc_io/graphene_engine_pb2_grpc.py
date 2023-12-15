# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import up_graphene_engine.grpc_io.graphene_engine_pb2 as graphene__engine__pb2


class GrapheneEngineStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.producePlanAnytime = channel.unary_unary(
                '/GrapheneEngine/producePlanAnytime',
                request_serializer=graphene__engine__pb2.Empty.SerializeToString,
                response_deserializer=graphene__engine__pb2.PlanRequest.FromString,
                )
        self.consumePlanAnytime = channel.stream_unary(
                '/GrapheneEngine/consumePlanAnytime',
                request_serializer=graphene__engine__pb2.PlanGenerationResult.SerializeToString,
                response_deserializer=graphene__engine__pb2.Empty.FromString,
                )
        self.producePlanOneShot = channel.unary_unary(
                '/GrapheneEngine/producePlanOneShot',
                request_serializer=graphene__engine__pb2.Empty.SerializeToString,
                response_deserializer=graphene__engine__pb2.PlanRequest.FromString,
                )
        self.consumePlanOneShot = channel.unary_unary(
                '/GrapheneEngine/consumePlanOneShot',
                request_serializer=graphene__engine__pb2.PlanGenerationResult.SerializeToString,
                response_deserializer=graphene__engine__pb2.Empty.FromString,
                )
        self.produceValidatePlan = channel.unary_unary(
                '/GrapheneEngine/produceValidatePlan',
                request_serializer=graphene__engine__pb2.Empty.SerializeToString,
                response_deserializer=graphene__engine__pb2.ValidationRequest.FromString,
                )
        self.consumeValidatePlan = channel.unary_unary(
                '/GrapheneEngine/consumeValidatePlan',
                request_serializer=graphene__engine__pb2.ValidationResult.SerializeToString,
                response_deserializer=graphene__engine__pb2.Empty.FromString,
                )
        self.produceCompile = channel.unary_unary(
                '/GrapheneEngine/produceCompile',
                request_serializer=graphene__engine__pb2.Empty.SerializeToString,
                response_deserializer=graphene__engine__pb2.Problem.FromString,
                )
        self.consumeCompile = channel.unary_unary(
                '/GrapheneEngine/consumeCompile',
                request_serializer=graphene__engine__pb2.CompilerResult.SerializeToString,
                response_deserializer=graphene__engine__pb2.Empty.FromString,
                )


class GrapheneEngineServicer(object):
    """Missing associated documentation comment in .proto file."""

    def producePlanAnytime(self, request, context):
        """An anytime plan request to the engine.
        The engine replies with a stream of N `Answer` messages where:
        - the first (N-1) message are of type `IntermediateReport`
        - the last message is of type `FinalReport`
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def consumePlanAnytime(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def producePlanOneShot(self, request, context):
        """A oneshot plan request to the engine.
        The engine replies with the PlanGenerationResult
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def consumePlanOneShot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def produceValidatePlan(self, request, context):
        """A validation request to the engine.
        The engine replies with the ValidationResult
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def consumeValidatePlan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def produceCompile(self, request, context):
        """A compiler request to the engine.
        The engine replies with the CompilerResult
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def consumeCompile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GrapheneEngineServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'producePlanAnytime': grpc.unary_unary_rpc_method_handler(
                    servicer.producePlanAnytime,
                    request_deserializer=graphene__engine__pb2.Empty.FromString,
                    response_serializer=graphene__engine__pb2.PlanRequest.SerializeToString,
            ),
            'consumePlanAnytime': grpc.stream_unary_rpc_method_handler(
                    servicer.consumePlanAnytime,
                    request_deserializer=graphene__engine__pb2.PlanGenerationResult.FromString,
                    response_serializer=graphene__engine__pb2.Empty.SerializeToString,
            ),
            'producePlanOneShot': grpc.unary_unary_rpc_method_handler(
                    servicer.producePlanOneShot,
                    request_deserializer=graphene__engine__pb2.Empty.FromString,
                    response_serializer=graphene__engine__pb2.PlanRequest.SerializeToString,
            ),
            'consumePlanOneShot': grpc.unary_unary_rpc_method_handler(
                    servicer.consumePlanOneShot,
                    request_deserializer=graphene__engine__pb2.PlanGenerationResult.FromString,
                    response_serializer=graphene__engine__pb2.Empty.SerializeToString,
            ),
            'produceValidatePlan': grpc.unary_unary_rpc_method_handler(
                    servicer.produceValidatePlan,
                    request_deserializer=graphene__engine__pb2.Empty.FromString,
                    response_serializer=graphene__engine__pb2.ValidationRequest.SerializeToString,
            ),
            'consumeValidatePlan': grpc.unary_unary_rpc_method_handler(
                    servicer.consumeValidatePlan,
                    request_deserializer=graphene__engine__pb2.ValidationResult.FromString,
                    response_serializer=graphene__engine__pb2.Empty.SerializeToString,
            ),
            'produceCompile': grpc.unary_unary_rpc_method_handler(
                    servicer.produceCompile,
                    request_deserializer=graphene__engine__pb2.Empty.FromString,
                    response_serializer=graphene__engine__pb2.Problem.SerializeToString,
            ),
            'consumeCompile': grpc.unary_unary_rpc_method_handler(
                    servicer.consumeCompile,
                    request_deserializer=graphene__engine__pb2.CompilerResult.FromString,
                    response_serializer=graphene__engine__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GrapheneEngine', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GrapheneEngine(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def producePlanAnytime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrapheneEngine/producePlanAnytime',
            graphene__engine__pb2.Empty.SerializeToString,
            graphene__engine__pb2.PlanRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def consumePlanAnytime(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/GrapheneEngine/consumePlanAnytime',
            graphene__engine__pb2.PlanGenerationResult.SerializeToString,
            graphene__engine__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def producePlanOneShot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrapheneEngine/producePlanOneShot',
            graphene__engine__pb2.Empty.SerializeToString,
            graphene__engine__pb2.PlanRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def consumePlanOneShot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrapheneEngine/consumePlanOneShot',
            graphene__engine__pb2.PlanGenerationResult.SerializeToString,
            graphene__engine__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def produceValidatePlan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrapheneEngine/produceValidatePlan',
            graphene__engine__pb2.Empty.SerializeToString,
            graphene__engine__pb2.ValidationRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def consumeValidatePlan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrapheneEngine/consumeValidatePlan',
            graphene__engine__pb2.ValidationResult.SerializeToString,
            graphene__engine__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def produceCompile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrapheneEngine/produceCompile',
            graphene__engine__pb2.Empty.SerializeToString,
            graphene__engine__pb2.Problem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def consumeCompile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrapheneEngine/consumeCompile',
            graphene__engine__pb2.CompilerResult.SerializeToString,
            graphene__engine__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
