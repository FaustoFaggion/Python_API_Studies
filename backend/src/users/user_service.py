from flask import request, jsonify
from src.users.adapters.dto_validation import *
from src.users.ports.user_repository_port import UserRepositoryPort
from src.users.ports.user_service_port import UserServicePort
from src.users.domain.user_entity import UserEntity
from src.users.dto.input_dto import InputUserDto, UserIdDto
from src.users.dto.output_dto import *

class UserService(UserServicePort):
    
    def __init__(self, user_repo: UserRepositoryPort):
        self.user_repo = user_repo
        
    def create(self, json_data: str):
        print("USER SERVICE")
        validate_dto(json_data, "InputUserDto")     
        dto: InputUserDto = InputUserDto(json_data)
        user: UserEntity = self.user_repo.create(dto)
        print("eNTITY: ")
        print(user)
        response: OutputUserDto = output_dto_factory(user)
        return response
    
    def update(self, json_data: str):
        print("USER SERVICE Update")
        validate_dto(json_data, "InputUserDto")     
        dto: InputUserDto = InputUserDto(json_data)
        user: UserEntity = self.user_repo.update(dto)

        response: OutputUserDto = output_dto_factory(user)
        return response
    
    def delete(self, json_data):
        print("USER SERVICE Find_one")
        print(json_data)
        validate_dto(json_data, "UserIdDto")     
        dto: UserIdDto = UserIdDto(json_data)
        print(dto)
        self.user_repo.delete(dto)

    def find_one(self, json_data):
        print("USER SERVICE Find_one")
        print(json_data)
        validate_dto(json_data, "UserIdDto")     
        dto: UserIdDto = UserIdDto(json_data)
        print(dto)
        user: UserEntity = self.user_repo.find_one(dto)
        response: OutputUserDto = output_dto_factory(user)
        
        return response
    
    def find_all(self):
        user = self.user_repo.find_all()
        return user