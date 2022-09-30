# this module is used to create a client for the gRPC service
# this module has the following classes:
#     UsersClient: this class is used to create a client for the gRPC service it inherits from users_pb2_grpc.UsersStub
# this module has the following functions:
#     main: this function is used to start the client

from concurrent import futures

from datetime import date

import os
import sys

import users_pb2_grpc as service
import users_pb2 as message

import grpc

from obj import User

class UsersClient:
    """
    this class is an helper class for the gRPC client
    it overrides the methods of the UsersStub class
    to make use of the User class
    this class has the following methods:
        create_user: this method is used to create a user
                     this method converts the request to a User protobuf object
                     this method calls the original method
        get_user: this method is used to get a user
                  this method calls the original method
        __init__: create a new stub from the channel
    """
    channel = None
    stub = None

    def __init__(self, channel):
        """
        create a new stub from the channel
        """
        self.channel = channel
        self.stub = service.UsersStub(channel)

    def create_user(self, user: User):
        """
        this method is used to create a user
        :param user: a User object
        :return: a User object
        """
        request = message.CreateUserRequest(user=user.to_protobuf())
        response = self.stub.CreateUser(request)

        return User.from_protobuf(response.user)

    def get_user(self, id: int):
        """
        this method is used to get a user
        :param id: the id of the user
        :return: a User object
        """
        request = message.GetUserRequest(id=id)
        response = self.stub.GetUser(request)
        return User.from_protobuf(response.user)

def main():
    """
    this function is used to start the client
    """

    with grpc.insecure_channel('localhost:50051') as channel:
        client = UsersClient(channel)

        user = User(
            name='John Doe',
            dob=date.fromisoformat('2000-01-01'),
            company='Acme',
            phone='555-555-5555',
            title='CEO'
        )

        user = client.create_user(user)
        print(user)

        user = client.get_user(user.id)
        print(user)

if __name__ == '__main__':
    main()
