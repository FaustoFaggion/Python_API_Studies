
from abc import ABC


class ValidateDto(ABC):
    
    def validate_dto(json_data, dto_type):
        ...