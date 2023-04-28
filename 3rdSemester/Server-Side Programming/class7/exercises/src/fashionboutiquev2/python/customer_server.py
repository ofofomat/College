from concurrent import futures
import logging
import grpc
import customer_pb2_grpc as customer_pb2_grpc
import customer_pb2 as customer_pb2
from customer_pb2_grpc import CustomerListServicer


def get_customer(self, customers, index):
    for customer in customers:
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


def alter_customer(self, customer, index):
    id = customer['id']
    novo_nome = input("Qual o novo nome? ")
    novo_email = input("Qual o novo email? ")
    novo_customer = customer_pb2.Customer(
        id=id,
        nome=novo_nome,
        email=novo_email
    )
    self.customers.insert(index, novo_customer)


class CustomerServicer(customer_pb2_grpc.CustomerListServicer):
    def __init__(self, customers=[]):
        self.customers = customers

    def GetAllCustomers(self, request, context):
        return self.customers

    def GetCustomer(self, request, context):
        customer = get_customer(self.customers, request)
        if customer is None:
            return customer_pb2.Customer(
                id=None,
                nome="",
                email=""
            )
        else:
            return customer

    def AddCustomer(self, request, context):
        customers = self.customers
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
        customers = self.customers
        customer = get_customer(customers, request)
        if customer is None:
            return responses(99)
        else:
            customers.remove(customer)
            return responses(1)

    def AlterCustomer(self, request, context):
        customers = self.customers
        customer = get_customer(customers, request)
        if customer is None:
            return responses(99)
        else:
            alter_customer(customer, request)
            return responses(2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    customer_pb2_grpc.add_CustomerListServicer_to_server(
        CustomerListServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server has been started!" +
          "\nWaiting new calls")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
