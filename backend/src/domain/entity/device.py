from src.domain.entity.hydraulic_cylinder_entity import CylinderEntity
from src.domain.entity.hydraulic_motor_entity import MotorEntity

class DeviceEntity:

    def __init__(self):
        self.power: int
        self.cylinders: CylinderEntity 
        self.motors: MotorEntity