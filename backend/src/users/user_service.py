from flask import request, jsonify
from src.users.user_repository import UserRepository
from src.users.dto.input_dto import CreateUserDto

class UserService():
    
    def __init__(self):
        pass

    def validate_dto():
        json_data = request.get_json()
        try:
            if not json_data:
                return jsonify({ "error": "Invalid JSON data"})    
            dto: CreateUserDto = CreateUserDto(json_data)
        except KeyError as err:
            return jsonify({"error": str(err)}), 400
        
        return dto
        
    def create():
        json_data = request.get_json()
        try:
            if not json_data:
                return jsonify({ "error": "Invalid JSON data"})    
            dto: CreateUserDto = CreateUserDto(json_data)
        except KeyError as err:
            return jsonify({"error": str(err)}), 400
        
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