# 1. interoperability-embedded-python

proto script :

```
python3 -m grpc_tools.protoc \
        --proto_path=./misc/proto/users/ \
        --python_out=src/python/grpc/ \
        --grpc_python_out=src/python/grpc/ \
        ./misc/proto/users/users.proto
```

TODO : DOC

Proof of Concept gRCP with iris interop

docker-compose up

POST http://localhost:8080/users HTTP/1.1
Content-Type: application/json

{
    "company": "tesdfst",
    "dob": "0001-01-01",
    "name": "fsd",
    "phone": "fdsffdsf",
    "title": "sfd"
}

GET http://localhost:8080/users/1
