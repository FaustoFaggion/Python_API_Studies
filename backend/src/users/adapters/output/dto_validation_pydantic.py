# from flask import jsonify
# import jsonschema
# from jsonschema import validate
# from src.users.domain.dto.input_dto import InputUserDto, UserIdDto
# from src.users.ports.output.validate_dto_port import ValidateDtoPort
# from pydantic import BaseModel, EmailStr, Field, validator, Extra

# class ValidateDtoPydantic(ValidateDtoPort):

#     class InputUserSchema(BaseModel):

#         email: EmailStr
#         name: str
#         age: int = Field(..., gt=0)  # age must be greater than 0
#         password: str

        
#         @validator('name')
#         def name_must_not_be_empty(cls, v):
#             if not v or v.strip() == "":
#                 raise ValueError('name must not be empty')
#             return v

#         @validator('password')
#         def password_strength(cls, v):
#             if len(v) < 8:
#                 raise ValueError('password must be at least 8 characters long')
#             return v
        
#         class Config:
#             extra = Extra.forbid

#     class UserIdSchema(BaseModel):
#         email: EmailStr
        
#         # class Config:
#         #     extra = "forbid"

#     def validate_dto(self, dto):
#             if not dto:
#                 return jsonify({ "error": "Invalid JSON data"})    
#             if isinstance(dto, InputUserDto):
#                 self.InputUserSchema(**dto.__dict__)
#             elif isinstance(dto, UserIdDto):
#                 self.UserIdSchema(**dto.__dict__)

#             return None