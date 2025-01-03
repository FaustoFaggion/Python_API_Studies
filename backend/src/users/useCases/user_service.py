from typing import List
from flask import request, jsonify
from src.users.ports.output.user_repository_port import UserRepositoryPort
from src.users.ports.input.user_service_port import UserServicePort
from src.users.domain.entities.user_entity import UserEntity
from src.users.domain.dto.input_dto import InputUserBatchDto, InputUserDto, UserIdDto, InputUserBatchDto, DeleteUserBatchDto
from src.users.domain.dto.output_dto import *
from src.users.ports.output.validate_dto_list_port import ValidateDtoListPort
from dataclasses import asdict, astuple

class UserService(UserServicePort):
    
    def __init__(self, user_repo: UserRepositoryPort, dto_validation: ValidateDtoListPort):
        self.user_repo = user_repo
        self.dto_validation = dto_validation
        
    def create(self, dto_list: InputUserBatchDto):
        print("USER SERVICE")
        # VALIDATE IF RECEIVED DATA IS ACORDING ENTITY
        self.dto_validation.validate_dto(dto_list)     
        
        # INSTANCIATE ENTITIES FROM DTO TO SAVE INTO DATABASE
        users_tuple_list: list[tuple] = []
        for dto in dto_list.users:
            users_tuple_list.append(dto.to_tuple())
            
        users_entity_list: list[UserEntity] = []
        for user_tuple in users_tuple_list:
            print("entity: ", users_entity_list)
            users_entity_list.append(UserEntity(user_tuple))
            
        # SEND Entity TO SAVE INTO DATABASE
        user_entities: list[UserEntity] = self.user_repo.create(users_entity_list)

        # GET OUTPUT DATA FROM USER ENTITY
        response: List[OutputUserDto] = []
        for entity in user_entities:
            response.append(OutputUserDto(entity.__dict__))
        
        for item in response:
            print("item: ", item)
        return response      

    def update(self, dto_list: InputUserBatchDto):
        print("USER SERVICE Update")
        # self.dto_validation.validate_dto(dto)

         # INSTANCIATE ENTITIES FROM DTO TO SAVE INTO DATABASE
        users_tuple_list: list[tuple] = []
        for dto in dto_list.users:
            users_tuple_list.append(dto.to_tuple())
        print("users_tuple_list: ", users_tuple_list)

        users_entity_list: list[UserEntity] = []
        for user_tuple in users_tuple_list:
            print("entity: ", users_entity_list)
            users_entity_list.append(UserEntity(user_tuple))

        # SEND Entity TO SAVE INTO DATABASE     
        user_entities: list[UserEntity] = self.user_repo.update(users_entity_list)
        
        # GET OUTPUT DATA FROM USER ENTITY
        response: List[OutputUserDto] = []
        for entity in user_entities:
            response.append(OutputUserDto(entity.__dict__))

        return response
    
    def delete(self, dto: DeleteUserBatchDto):
        print("USER SERVICE DELETE")
        # self.dto_validation.validate_dto(dto)     
        self.user_repo.delete(dto)

    def find_one(self, dto: UserIdDto):
        print("USER SERVICE Find_one")
        # self.dto_validation.validate_dto(dto)     
        entity: UserEntity = self.user_repo.find_one(dto)

        # GET OUTPUT DATA FROM USER ENTITY
        response: OutputUserDto = OutputUserDto(entity.__dict__)
        
        return response
    
    def find_all(self):
        user_entities: List[UserEntity] = self.user_repo.find_all()
        
        # GET OUTPUT DATA FROM USER ENTITY
        response: List[OutputUserDto] = []
        for entity in user_entities:
            response.append(OutputUserDto(entity.__dict__))
        
        return response
    