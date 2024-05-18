from abc import ABC, abstractmethod
from typing import Any
from src.users.dto.input_dto import InputUserDto
from src.users.domain.user_entity import UserEntity
from src.users.ports.user_repository_port import UserRepositoryPort


class UserServicePort(ABC):
        
    @abstractmethod
    def create(json_data: str):
        ...
    
    @abstractmethod
    def update(json_data: str):
        ...
    
    @abstractmethod
    def delete(json_data: str):
        ...
    
    @abstractmethod
    def find_one(json_data: str):
        ...
        
    @abstractmethod
    def find_all():
        ...
 