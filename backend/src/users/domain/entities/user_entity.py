
from dataclasses import dataclass


@dataclass
class UserEntity:
    email:      str
    name:       str
    age:        int
    password:   str
    
def user_factory(data: tuple) -> UserEntity:
    return UserEntity(
        email=data[0],
        name=data[1],
        age=data[2],
        password=data[3]
    )