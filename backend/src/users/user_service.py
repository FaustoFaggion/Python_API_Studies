from flask import request, jsonify
from src.users.adapters.dto_validation import *
from src.users.ports.user_repository_port import UserRepositoryPort
from src.users.domain.user_entity import UserEntity
from src.users.dto.input_dto import CreateUserDto
from src.users.dto.output_dto import *

class UserService():
    
    def __init__(self, user_repo: UserRepositoryPort):
        self.user_repo = user_repo
        
    def create(self, json_data):
        json_error = validate_dto(json_data, CREATE_USER_SCHEMA)        
        if json_error:
            return jsonify({"error": json_error})
            
        dto: CreateUserDto = CreateUserDto(json_data)
        user: UserEntity = self.user_repo.create(dto)
        print(user)
        response1: OutputUserDto = output_dto_factory(user)
        print(response1)
        response3 = jsonify({"res": response1})
        print(response3)
        response = jsonify({"user": user})
        print( response)
        return response1
    
    def update(self):
        user = self.user_repo.update()
        return user
    
    def delete(self, email):
        return self.user_repo.delete(email)

    def findOne(self, email):
        user = self.user_repo.findOne(email)
        return user
    
    def findAll(self):
        user = self.user_repo.findAll()
        return user