from flask import request, jsonify
from src.users.adapters.dto_validation import *
from src.users.ports.user_repository_port import UserRepositoryPort
from src.users.ports.user_service_port import UserServicePort
from src.users.domain.user_entity import UserEntity
from src.users.dto.input_dto import InputUserDto
from src.users.dto.output_dto import *

class UserService(UserServicePort):
    
    def __init__(self, user_repo: UserRepositoryPort):
        self.user_repo = user_repo
        
    def create(self, json_data: str):
        print("USER SERVICE")
        validate_dto(json_data, "InputUserDto")     
        dto: InputUserDto = InputUserDto(json_data)
        user: UserEntity = self.user_repo.create(dto)

        response: OutputUserDto = output_dto_factory(user)
        return response
    
    def update(self, json_data: str):
        print("USER SERVICE Update")
        validate_dto(json_data, "InputUserDto")     
        dto: InputUserDto = InputUserDto(json_data)
        user: UserEntity = self.user_repo.update(dto)

        response: OutputUserDto = output_dto_factory(user)
        return response
    
    def delete(self, email):
        return self.user_repo.delete(email)

    def find_one(self, email):
        user = self.user_repo.findOne(email)
        return user
    
    def find_all(self):
        user = self.user_repo.find_all()
        return user