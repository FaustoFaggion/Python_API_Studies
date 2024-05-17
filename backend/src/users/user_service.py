from flask import request, jsonify
from src.users.user_repository import UserRepository
from src.users.dto.input_dto import CreateUserDto

class UserService():
    
    def __init__(self):
        pass

    def validate_created_user_json():
        json_data = request.get_json()
        
        if type(json_data["email"]) != str:
            return "Exception"
        
    def create():
        UserService.validate_created_user_json()
        user = UserRepository.create()
        
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