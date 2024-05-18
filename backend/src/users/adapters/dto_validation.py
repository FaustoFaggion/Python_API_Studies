from flask import jsonify
import jsonschema
from jsonschema import validate
from src.users.dto.input_dto import InputUserDto

INPUT_USER_SCHEMA = {
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

USER_ID_SCHEMA = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
    },
    "required": ["email"],
    "additionalProperties": False
}

def validate_dto(json_data, dto_type: str):
        if not json_data:
            return jsonify({ "error": "Invalid JSON data"})    
        if  dto_type == "InputUserDto":
            validate(instance=json_data, schema=INPUT_USER_SCHEMA)
        if  dto_type == "UserIdDto":
            validate(instance=json_data, schema=USER_ID_SCHEMA)
        
        return None