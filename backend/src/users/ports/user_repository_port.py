from abc import ABC, abstractmethod
from typing import Any
from src.users.dto.input_dto import InputUserDto, UserIdDto
from src.users.domain.user_entity import UserEntity


class UserRepositoryPort(ABC):
    
    # @abstractmethod
    # def ___init___() -> None:
    #     pass
        
    @abstractmethod
    def create(dto: InputUserDto):
        ...
    
    @abstractmethod
    def update(dto: InputUserDto):
        ...
    
    @abstractmethod
    def delete(dto: UserIdDto):
        ...
    
    @abstractmethod
    def find_one(dto: UserIdDto):
        ...
        
    @abstractmethod
    def find_all():
        ...
   