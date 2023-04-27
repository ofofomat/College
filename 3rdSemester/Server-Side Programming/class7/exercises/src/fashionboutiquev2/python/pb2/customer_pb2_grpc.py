# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import customer_pb2 as customer__pb2


class CustomerListStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllCustomers = channel.unary_unary(
                '/customer.CustomerList/GetAllCustomers',
                request_serializer=customer__pb2.Request.SerializeToString,
                response_deserializer=customer__pb2.ListOfCustomer.FromString,
                )
        self.GetCustomer = channel.unary_unary(
                '/customer.CustomerList/GetCustomer',
                request_serializer=customer__pb2.Id.SerializeToString,
                response_deserializer=customer__pb2.Customer.FromString,
                )
        self.AddCustomer = channel.unary_unary(
                '/customer.CustomerList/AddCustomer',
                request_serializer=customer__pb2.Customer.SerializeToString,
                response_deserializer=customer__pb2.Response.FromString,
                )
        self.DeleteCustomer = channel.unary_unary(
                '/customer.CustomerList/DeleteCustomer',
                request_serializer=customer__pb2.Id.SerializeToString,
                response_deserializer=customer__pb2.Response.FromString,
                )
        self.AlterCustomer = channel.unary_unary(
                '/customer.CustomerList/AlterCustomer',
                request_serializer=customer__pb2.Id.SerializeToString,
                response_deserializer=customer__pb2.Response.FromString,
                )


class CustomerListServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllCustomers(self, request, context):
        """Get all customers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomer(self, request, context):
        """Get a customer from the list by the id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCustomer(self, request, context):
        """Add a customer to the list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCustomer(self, request, context):
        """Delete a customer from the list by the id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AlterCustomer(self, request, context):
        """Alter a customer from the list by the id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CustomerListServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllCustomers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllCustomers,
                    request_deserializer=customer__pb2.Request.FromString,
                    response_serializer=customer__pb2.ListOfCustomer.SerializeToString,
            ),
            'GetCustomer': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCustomer,
                    request_deserializer=customer__pb2.Id.FromString,
                    response_serializer=customer__pb2.Customer.SerializeToString,
            ),
            'AddCustomer': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCustomer,
                    request_deserializer=customer__pb2.Customer.FromString,
                    response_serializer=customer__pb2.Response.SerializeToString,
            ),
            'DeleteCustomer': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCustomer,
                    request_deserializer=customer__pb2.Id.FromString,
                    response_serializer=customer__pb2.Response.SerializeToString,
            ),
            'AlterCustomer': grpc.unary_unary_rpc_method_handler(
                    servicer.AlterCustomer,
                    request_deserializer=customer__pb2.Id.FromString,
                    response_serializer=customer__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'customer.CustomerList', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CustomerList(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllCustomers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerList/GetAllCustomers',
            customer__pb2.Request.SerializeToString,
            customer__pb2.ListOfCustomer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCustomer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerList/GetCustomer',
            customer__pb2.Id.SerializeToString,
            customer__pb2.Customer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCustomer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerList/AddCustomer',
            customer__pb2.Customer.SerializeToString,
            customer__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCustomer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerList/DeleteCustomer',
            customer__pb2.Id.SerializeToString,
            customer__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AlterCustomer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/customer.CustomerList/AlterCustomer',
            customer__pb2.Id.SerializeToString,
            customer__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
