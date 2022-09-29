# this class is a dataclass that represents a user
# this class is used to store user information
# this class is used to serialize and deserialize user information to protobuf

import gen.users_pb2 as users

from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    """
    this class represents a user

    this class have the following attributes:
        id: int
        name: str
        dob: date
        company: str
        phone: str
        title: str
    """
    
    id: int = 0
    name: str = ''
    dob: date = date.fromisoformat('0001-01-01')
    company: str = ''
    phone: str = ''
    title: str = ''

    def to_protobuf(self) -> users.User:
        """
        this method converts a User object to a protobuf User object

        :return: a protobuf User object
        """

        return users.User(
            id=self.id, 
            name=self.name, 
            company=self.company,
            dob=self.dob.isoformat(), 
            phone=self.phone, 
            title=self.title
        )

    @staticmethod
    def from_protobuf(user: users.User) -> 'User':
        """
        this method converts a protobuf User object to a User object

        :param user: a protobuf User object
        :return: a User object
        """

        return User(
            id=user.id,
            name=user.name,
            dob=date.fromisoformat(user.dob),
            company=user.company,
            phone=user.phone,
            title=user.title
        )

