# from flask import jsonify
# import jsonschema
# from jsonschema import validate
# from src.users.domain.dto.input_dto import InputUserDto
# from src.users.ports.output.validate_dto_port import ValidateDtoPort

# class ValidateDto(ValidateDtoPort):
#     INPUT_USER_SCHEMA = {
#         "type": "object",
#         "properties": {
#             "email": {"type": "string"},
#             "name": {"type": "string"},
#             "age": {"type": "integer"},
#             "password": {"type": "string"}
#         },
#         "required": ["email", "name", "age", "password"],
#         "additionalProperties": False
#     }

#     USER_ID_SCHEMA = {
#         "type": "object",
#         "properties": {
#             "email": {"type": "string"},
#         },
#         "required": ["email"],
#         "additionalProperties": False
#     }

#     def validate_dto(self, json_data, dto_type: str):
#             if not json_data:
#                 return jsonify({ "error": "Invalid JSON data"})    
#             if  dto_type == "InputUserDto":
#                 validate(instance=json_data, schema=self.INPUT_USER_SCHEMA)
#             if  dto_type == "UserIdDto":
#                 validate(instance=json_data, schema=self.USER_ID_SCHEMA)

#             return None