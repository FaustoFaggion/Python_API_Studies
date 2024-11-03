from typing import List
from flask import request, jsonify
from src.users.ports.output.user_repository_port import UserRepositoryPort
from src.users.ports.input.user_service_port import UserServicePort
from src.users.domain.entities.user_entity import UserEntity
from src.users.domain.dto.input_dto import InputUserDto, UserIdDto, InputUserBatchDto, DeleteUserBatchDto
from src.users.domain.dto.output_dto import *
from src.users.ports.output.validate_dto_port import ValidateDtoPort
from dataclasses import asdict
class UserService(UserServicePort):
    
    def __init__(self, user_repo: UserRepositoryPort, dto_validation: ValidateDtoPort):
        self.user_repo = user_repo
        self.dto_validation = dto_validation
        
    def create(self, dto: InputUserBatchDto):
        print("USER SERVICE")
        # self.dto_validation.validate_dto(dto)     
        user_entities: list[UserEntity] = self.user_repo.create(dto)

        dto_list: List[OutputUserDto] = []
        for entity in user_entities:
            dto_list.append(OutputUserDto(asdict(entity)))
        
        response: list = []
        for user in dto_list:
           response.append(asdict(user))

        return json.dumps(response) 

        

    def update(self, dto: InputUserDto):
        print("USER SERVICE Update")
        # self.dto_validation.validate_dto(dto)     
        user_entities: list[UserEntity] = self.user_repo.update(dto)
        
        dto_list: List[OutputUserDto] = []
        for entity in user_entities:
            dto_list.append(OutputUserDto(asdict(entity)))
        
        response: list = []
        for user in dto_list:
           response.append(asdict(user))

        return json.dumps(response)
    
    def delete(self, dto: DeleteUserBatchDto):
        print("USER SERVICE Find_one")
        # self.dto_validation.validate_dto(dto)     
        self.user_repo.delete(dto)

    def find_one(self, dto: UserIdDto):
        print("USER SERVICE Find_one")
        self.dto_validation.validate_dto(dto)     
        user: UserEntity = self.user_repo.find_one(dto)
        response: OutputUserDto = OutputUserDto(user)
        
        return response
    
    def find_all(self):
        users: List[UserEntity] = self.user_repo.find_all()
        
        print("User SErvice users: ", users)
        response: List[OutputUserDto] = []
        for user in users:
            response.append(OutputUserDto(user))
        
        return {"users": response}
    