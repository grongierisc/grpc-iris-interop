from dataclasses import dataclass

from grongier.pex import Message

from obj import User

@dataclass
# > The `CreateUserResponse` class is a message that contains an `id` field of type `int`
class CreateUserRequest(Message):

    user:User = None

@dataclass
# > The `CreateUserResponse` class is a message that contains an `id` field of type `int`
class CreateUserResponse(Message):

    user:User=None


@dataclass
# > The `GetUserResponse` class is a `Message` class that has a `person` attribute of type `User`
class GetUserResponse(Message):
    user:User = None

@dataclass
# > A request to get a person by id
class GetUserRequest(Message):
    id:int = None
