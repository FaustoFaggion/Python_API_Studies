from dataclasses import dataclass
import json
from src.users.domain.entities.user_entity import UserEntity

@dataclass
class OutputUserDto:
    email:      str
    name:       str
    age:        int
    
def output_dto_factory(entity: UserEntity) -> OutputUserDto:
    return OutputUserDto(
        email = entity.email,
        name = entity.name,
        age = entity.age
    )