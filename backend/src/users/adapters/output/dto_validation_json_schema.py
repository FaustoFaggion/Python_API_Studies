import json
from flask import jsonify
import jsonschema
from jsonschema import validate
from src.users.domain.dto.input_dto import InputUserDto, UserIdDto
from src.users.ports.output.validate_dto_port import ValidateDtoPort

class ValidateDtoJsonSchema(ValidateDtoPort):
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

    def validate_dto(self, dto):
        if not dto:
            return jsonify({ "error": "Invalid JSON data"})
           
        user_dict = dto.__dict__   
        print(user_dict)
        if isinstance(dto, InputUserDto):
            validate(instance=user_dict, schema=self.INPUT_USER_SCHEMA)
            print("Validation successful.")
        if isinstance(dto, UserIdDto):
            validate(instance=user_dict, schema=self.USER_ID_SCHEMA)

        return None