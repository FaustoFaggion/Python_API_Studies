from flask import request, jsonify
from src.users.user_repository import UserRepository
from src.users.dto.input_dto import CreateUserDto
from src.users.adapters.dto_validation import *

class UserService():
    
    def __init__(self):
        pass
        
    def create():
        json_data = request.get_json()
        json_error = validate_dto(json_data, CREATE_USER_SCHEMA)        
        if json_error:
            return jsonify({"error": json_error})
        
        dto: CreateUserDto = CreateUserDto(json_data)
        user = UserRepository.create(dto)
        
        return user
    
    def update():
        user = UserRepository.update()
        return user
    
    def delete(email):
        return UserRepository.delete(email)

    def findOne(email):
        user = UserRepository.findOne(email)
        return user
    
    def findAll():
        user = UserRepository.findAll()
        return user