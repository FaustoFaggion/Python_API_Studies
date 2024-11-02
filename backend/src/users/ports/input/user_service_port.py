from abc import ABC, abstractmethod
from typing import Any

class UserServicePort(ABC):
        
    @abstractmethod
    def create(json_data: any):
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
 