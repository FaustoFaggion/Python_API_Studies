from flask import request, jsonify
from src.users.user_repository import UserRepository
from src.users.dto.input_dto import CreateUserDto

import jsonschema
from jsonschema import validate

CREATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "password": {"type": "string"}
    },
    "required": ["email", "name", "age", "password"],
    "additionalProperties": False
}

class UserService():
    
    def __init__(self):
        pass

    def validate_dto(json_data):
        if not json_data:
            return jsonify({ "error": "Invalid JSON data"})    
        validate(instance=json_data, schema=CREATE_USER_SCHEMA)    

        return None
        
    def create():
        json_data = request.get_json()
        
        try:
            if not json_data:
                return jsonify({ "error": "Invalid JSON data"})    

            validate(instance=json_data, schema=CREATE_USER_SCHEMA)    
            dto: CreateUserDto = CreateUserDto(json_data)
        
        except jsonschema.ValidationError as e:
            return jsonify({"error": str(e)}), 400
        
        # dto = UserService.validate_dto(json_data)        
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