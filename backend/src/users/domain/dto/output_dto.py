from dataclasses import dataclass
import json
from src.users.domain.entities.user_entity import UserEntity

@dataclass
class OutputUserDto:
    email:      str
    name:       str
    age:        int
    
    def __init__(self, entity: dict):
        self.email = entity["email"]
        self.name = entity["name"]
        self.age = entity["age"]