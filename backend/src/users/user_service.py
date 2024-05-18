from flask import request, jsonify
# from src.users.user_repository import UserRepository
from src.users.dto.input_dto import CreateUserDto
from src.users.ports.user_repository_port import UserRepositoryPort
from src.users.adapters.dto_validation import *

class UserService():
    
    def __init__(self, user_repo: UserRepositoryPort):
        self.user_repo = user_repo
        
    def create(self):
        json_data = request.get_json()
        json_error = validate_dto(json_data, CREATE_USER_SCHEMA)        
        if json_error:
            return jsonify({"error": json_error})
        
        dto: CreateUserDto = CreateUserDto(json_data)
        user = self.user_repo.create(dto)
        
        return user
    
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