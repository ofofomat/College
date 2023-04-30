from __future__ import print_function
import logging
import grpc
import customer_pb2
import customer_pb2_grpc


def call_get_all_customers(stub):
    customers = stub.GetAllCustomers(0)
    print(customers)


def call_get_a_customer(stub):
    index = input("What's the index of the customer? ")
    customer = stub.GetCustomer(index)
    print(customer)


def call_add_a_customer(stub):
    nome = input("Customer's name: ")
    email = input("Customer's email: ")
    data = [nome, email]
    stub.AddCustomer(data)


def call_delete_a_customer(stub):
    index = input("What's the index of the customer? ")
    stub.DeleteCustomer(index)


def call_alter_a_customer(stub):
    index = input("What's the customer's index? ")
    stub.AlterCustomer(index)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = customer_pb2_grpc.CustomerListStub(channel)
        # print("---------- AddCustomer1 ----------")
        # call_add_a_customer(stub)
        # SHOULD ADD ONE CUSTOMER
        # print("---------- AddCustomer2 ----------")
        # call_add_a_customer(stub)
        # # should add another customer
        # print("---------- AddCustomer3 ----------")
        # call_add_a_customer(stub)
        # # should add the last customer
        # print("---------- DeleteCustomer ----------")
        # call_delete_a_customer(stub)
        # # should delete the second customer
        # print("---------- AlterCustomer ----------")
        # call_alter_a_customer(stub)
        # # should alter the first customer
        # print("---------- GetCustomer ----------")
        # call_get_a_customer(stub)
        # # should return customer 1
        # print("---------- GetCustomer ----------")
        # call_get_a_customer(stub)
        # # should return customer 2
        # # and it should be equal to the last customer added
        # print("---------- GetAllCustomers ----------")
        # call_get_all_customers(stub)
        # should have 2 customers


if __name__ == '__main__':
    logging.basicConfig()
    run()
