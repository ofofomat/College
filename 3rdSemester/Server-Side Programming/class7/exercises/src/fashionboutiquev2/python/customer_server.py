from concurrent import futures
import logging
import grpc
from pb2 import customer_pb2, customer_pb2_grpc
import customer_resources


def get_customer(customer_db, index):
    for customer in customer_db:
        if customer.location == index:
            return customer
    return None


def responses(self, type):
    response = customer_pb2.Response
    response.operation = response.Type.Name(type)
    if response.operation == 'ADD':
        response.name = 'Added to the list'
        response.http_status_code = 201
    elif response.operation == 'DELETE':
        response.name = 'Deleted from the list'
        response.http_status_code = 204
    elif response.operation == 'ALTER':
        response.name = 'Altered in the list'
        response.http_status_code = 200
    else:
        response.name = ""
        response.http_status_code = None


class CustomerServicer(customer_pb2_grpc.CustomerListServicer):
    def __init__(self):
        self.db = customer_resources.read_customer_database()

    def GetAllCustomers(self, request, context):
        return self.db

    def GetCustomer(self, request, context):
        customer = get_customer(self.db, request)
        if customer is None:
            return f'This id is not being used.'
        else:
            return customer

    def AddCustomer(self, request, context):
        customers = self.db
        data = request
        customer = customer_pb2.Customer(
            id=customer_pb2.Id.id,
            nome=data['nome'],
            email=data['email']
        )
        customer_pb2.Id.count()
        customers.append(customer)
        return responses(0)

    def DeleteCustomer(self, request, context):
        customers = self.db
        customers.pop(request)
        return responses(1)

    def AlterCustomer(self, request, context):
        return super().AlterCustomer(request, context)
