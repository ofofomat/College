import json

from pb2 import customer_pb2


def read_customer_database():
    customers_list = []
    with open("customer_db.json") as customer_db_file:
        for item in json.load(customer_db_file):
            customer = customer_pb2.Customer(
                id=customer_pb2.Id.id,
                nome=item['nome'],
                email=item['email']
            )
            customer_pb2.Id.count()
            customers_list.append(customer)
    return customers_list
