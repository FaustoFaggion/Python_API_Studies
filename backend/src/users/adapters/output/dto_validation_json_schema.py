import json
from flask import jsonify
import jsonschema
from jsonschema import validate
from src.users.domain.dto.input_dto import InputUserDto, InputUserBatchDto, UserIdDto
from src.users.ports.output.validate_dto_list_port import ValidateDtoListPort

class ValidateDtoListJsonSchema(ValidateDtoListPort):
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

    def validate_dto(self, dto_list):
        print("VALIDATE DTO")
        if not dto_list:
            return jsonify({ "error": "Invalid JSON data"})
        
        if isinstance(dto_list, InputUserBatchDto):
            for dto in dto_list.users:
                user_dict = dto.__dict__   
                print(user_dict)
                try:
                    validate(instance=user_dict, schema=self.INPUT_USER_SCHEMA)
                    print("Validation successful.")
                except jsonschema.exceptions.ValidationError as e:
                    return jsonify({"error": f"Validation failed: {e.message}"}), 400
        # elif isinstance(dto_list, UserIdDto):
        #     validate(instance=user_dict, schema=self.USER_ID_SCHEMA)

        return None