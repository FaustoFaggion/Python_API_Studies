from typing import List
from flask import request, jsonify
from src.users.ports.output.user_repository_port import UserRepositoryPort
from src.users.ports.input.user_service_port import UserServicePort
from src.users.domain.entities.user_entity import UserEntity
from src.users.domain.dto.input_dto import InputUserDto, UserIdDto
from src.users.domain.dto.output_dto import *
from src.users.ports.output.validate_dto_port import ValidateDtoPort

class UserService(UserServicePort):
    
    def __init__(self, user_repo: UserRepositoryPort, dto_validation: ValidateDtoPort):
        self.user_repo = user_repo
        self.dto_validation = dto_validation
        
    def create(self, dto: InputUserDto):
        print("USER SERVICE")
        self.dto_validation.validate_dto(dto)     
        user: UserEntity = self.user_repo.create(dto)
        response: OutputUserDto = OutputUserDto(user)
        return response
    
    def update(self, dto: InputUserDto):
        print("USER SERVICE Update")
        self.dto_validation.validate_dto(dto)     
        user: UserEntity = self.user_repo.update(dto)

        response: OutputUserDto = OutputUserDto(user)
        return response
    
    def delete(self, dto: UserIdDto):
        print("USER SERVICE Find_one")
        self.dto_validation.validate_dto(dto)     
        self.user_repo.delete(dto)

    def find_one(self, dto: UserIdDto):
        print("USER SERVICE Find_one")
        self.dto_validation.validate_dto(dto)     
        user: UserEntity = self.user_repo.find_one(dto)
        response: OutputUserDto = OutputUserDto(user)
        
        return response
    
    def find_all(self):
        users: List[OutputUserDto] = self.user_repo.find_all()
        
        response: List[OutputUserDto] = []
        for user in users:
            response.append(OutputUserDto(user))
        
        return {"users": response}
    