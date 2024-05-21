
from abc import ABC, abstractmethod


class Database_Port(ABC):
    
    @abstractmethod
    def db_connection():
        ...
        
    @abstractmethod
    def createTables():
        ...
        
        