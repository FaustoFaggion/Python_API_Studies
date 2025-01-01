from src.domain.dto.cylinder.input_dto import CylinderIdDto
from src.domain.dto.cylinder.output_dto import OutputCylinderDto
from src.domain.entity.hydraulic_cylinder_entity import HydraulicCylinderEntity 
from src.adapters.output.cylinder_repository import CylinderRepository

class CylinderService:

    def __init__(self, cylinder_repository: CylinderRepository):
        self.cylinder_repository = cylinder_repository

    def find_one(self, dto: CylinderIdDto):
        print("CYLINDER SERVICE Find_one")
        # self.dto_validation.validate_dto(dto)

        entity: HydraulicCylinderEntity = self.cylinder_repository.find_one(dto)
        print('RETURN ENTITY: \n', entity)
        
        # GET OUTPUT DATA FROM USER ENTITY
        response: OutputCylinderDto = OutputCylinderDto(entity)
        print(f"response: {response}")
        return response
