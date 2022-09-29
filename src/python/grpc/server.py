# this module is used to create a server for the gRPC service
#
# this module has the following classes:
#     UsersService: this class is used to create a server for the gRPC service it inherits from gen.users_pb2_grpc.UsersServicer
#
# this module has the following functions:
#     main: this function is used to start the server

from concurrent import futures

import os
import sys

# add the gen directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'gen'))

import gen.users_pb2_grpc as service
import gen.users_pb2 as message

import grpc

from obj import User

class UsersService(service.UsersServicer):
    """
    this class is used to create a server for the gRPC service

    it inherits from gen.users_pb2_grpc.UsersServicer
    """

    def __init__(self):
        """
        this method is used to initialize the UsersService class
        """

        self.users = []

    def CreateUser(self, request, context):
        """
        this method is used to add a user to the database

        :param request: a protobuf CreateUserRequest object
        :param context: a grpc.ServicerContext object
        :return: a protobuf CreateUserResponse object
        """
            
        user = User.from_protobuf(request.user)

        self.users.append(user)
        user.id = len(self.users) - 1

        response = message.CreateUserResponse(user=user.to_protobuf())

        return response

    def GetUser(self, request, context):
        """
        this method is used to get a user from the database

        :param request: a protobuf GetUserRequest object
        :param context: a grpc.ServicerContext object
        :return: a protobuf GetUserResponse object
        """
    
        user = self.users[request.id]

        response = message.GetUserResponse(user=user.to_protobuf())

        return response

def main():
    """
    this function is used to start the server
    """

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service.add_UsersServicer_to_server(UsersService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    main()