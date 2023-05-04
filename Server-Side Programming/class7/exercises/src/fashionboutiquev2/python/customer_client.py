from __future__ import print_function
import logging
import random

import grpc
from pb2 import customer_pb2, customer_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = customer_pb2_grpc.CustomerListStub(channel)
        print("SOMETHING HERE")


if __name__ == '__main__':
    logging.basicConfig()
    run()
