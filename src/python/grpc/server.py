# this module is used to create a server for the gRPC service
#
# this module has the following classes:
#     UsersService: this class is used to create a server for the gRPC service it inherits from users_pb2_grpc.UsersServicer
#
# this module has the following functions:
#     main: this function is used to start the server

from concurrent import futures

from grongier.pex import Director

import users_pb2_grpc as service
import users_pb2 as message

import grpc

from obj import User

from msg import (CreateUserRequest, GetUserRequest)

class UsersService(service.UsersServicer):
    """
    this class is used to create a server for the gRPC service

    it inherits from users_pb2_grpc.UsersServicer
    """

    def CreateUser(self, request, context):
        """
        this method is used to add a user to the database

        :param request: a protobuf CreateUserRequest object
        :param context: a grpc.ServicerContext object
        :return: a protobuf CreateUserResponse object
        """
            
        user = User.from_protobuf(request.user)
        msg = CreateUserRequest(user=user)

        service = Director.create_python_business_service("Python.gRPCService")
        iris_response = service.on_process_input(msg)

        response = message.CreateUserResponse(user=iris_response.user.to_protobuf())

        return response

    def GetUser(self, request, context):
        """
        this method is used to get a user from the database

        :param request: a protobuf GetUserRequest object
        :param context: a grpc.ServicerContext object
        :return: a protobuf GetUserResponse object
        """
    
        msg = GetUserRequest(id=request.id)

        service = Director.create_python_business_service("Python.gRPCService")
        iris_response = service.on_process_input(msg)

        response = message.GetUserResponse(user=iris_response.user.to_protobuf())

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