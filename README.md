# grpc-iris-interop

The aim of this proof of concept is to show how the gRPC protocl can be implemented with the IRIS ineroperabilty module.

## architecture

<img width="1128" alt="image" src="https://user-images.githubusercontent.com/47849411/193216843-b34a1aad-4b3b-4d01-8ca3-c0bbbc01cdca.png">

On this schema, we can see that the gRPC Service is hosted by IRIS.

This service must invoke the IRIS interoperability module. For that it transforms the protobuf messages to IRIS messages.

The gRPC client is host by a Flask server for demo purpose, the gRPC client can also be invoke by the python script.

## definition of each file

### users.proto

```proto
syntax = "proto3";
package users;

service Users {
  rpc CreateUser (users.CreateUserRequest) returns (users.CreateUserResponse);
  rpc GetUser (users.GetUserRequest) returns (users.GetUserResponse);
}

message User {
  uint32 id = 1;
  string name = 2;
  string dob = 3;
  string company = 4;
  string phone = 5;
  string title = 6;

}

message CreateUserRequest {
  User user = 1;
}

message CreateUserResponse {
  User user = 1;
}

message GetUserRequest {
  uint32 id = 1;
}

message GetUserResponse {
  User user = 1;
}
```

This file is in ./misc/proto/users

This file holds the definition of the gRPC implementation, it’s kinda the swagger spec.

To create the implementation classes you have to invoke this command :

```sh
python3 -m grpc_tools.protoc \
        --proto_path=./misc/proto/users/ \
        --python_out=src/python/grpc/ \
        --grpc_python_out=src/python/grpc/ \
        ./misc/proto/users/users.proto
```

This command generate two files :

* users_pb2.py that hold the definition of the protobuf objects User and messages GetUser and CreateUser
* users_pb2_grpc.py that hold a Client and Service


### obj.py

This module is in ./src/python/grpc/

This module has on class User.

This class is a dataclass that represents a user.

This class is used to store user information.

This class is used to serialize and deserialize user information to protobuf.

This class is used in the IRIS messages.

### server.py

This module is in ./src/python/grpc/

This module is used to create a server for the gRPC service.

This module has the following classes:
* UsersService: this class is used to create a server for the gRPC service it inherits from users_pb2_grpc.UsersServicer

This module has the following functions:
* main: this function is used to start the server

UsersService has the following functions:
* CreateUser: 
  * This function is used to retrive an Business Service instance with the IRIS Director module.
  * It makes use of User classe to deserialize the protobuf message and convert it in User dataclass.
* GetUser: 
  * This function is used to retrive an Business Service instance with the IRIS Director module. 
  * It makes use of User classe to deserialize the protobuf message and convert it in User dataclass.

### client.py

This module is in ./src/python/grpc/

This module is used to create a client for the gRPC service.

This module has the following classes:
* UsersClient: this class is used to create a client for the gRPC service on init it create a users_pb2_grpc.UsersStub with a channel parameter

This module has the following functions:
* main: this function is used to start the client outside of the Flask application

The UsersClient class has the following methods:
* create_user: 
  * this method is used to create a user
  * this method converts the request to a User protobuf object
  * this method calls the original method
* get_user: 
  * this method is used to get a user
  * this method calls the original method
* `__init__`: create a new stub from the channel

### app.py

This module is in ./src/python/grpc/

This module is the flask app to server the gRCP client

This module has the following classes:
* app: 
  * this class is used to create the flask app
    * it has the following methods:
      * create_user: 
        * this method is used to create a user
        * it returns a json object
        * it converts the request payload to a User object
        * it calls the gRPC client to create the user
      * get_user: 
        * this method is used to get a user
        * it returns a json object
        * it calls the gRPC client to get the user by id

This module has the following functions:
* main: this function is used to start the flask app


## Run this project

```sh
docker-compose up
```

Play with it :

```http
POST http://localhost:8080/users HTTP/1.1
Content-Type: application/json

{
    "company": "tesdfst",
    "dob": "0001-01-01",
    "name": "fsd",
    "phone": "fdsffdsf",
    "title": "sfd"
}
```

```http
GET http://localhost:8080/users/1 HTTP/1.1
```