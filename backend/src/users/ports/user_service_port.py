from abc import ABC, abstractmethod
from typing import Any
from src.users.dto.input_dto import InputUserDto
from src.users.domain.user_entity import UserEntity


class UserServicePort(ABC):
    # @abstractmethod
    # def ___init___() -> None:
    #     ...
        
    @abstractmethod
    def create():
        ...
    
    @abstractmethod
    def update():
        ...
    
    @abstractmethod
    def delete(email):
        ...
    
    @abstractmethod
    def find_one(email):
        ...
        
    @abstractmethod
    def find_all():
        ...
 