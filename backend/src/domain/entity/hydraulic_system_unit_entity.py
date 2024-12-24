from src.domain.entity.oil_entity import OilEntity
from src.domain.entity.hydraulic_system_unit_entity import HydraulicSystemUnitEntity
from src.domain.interface.engine_interface import IEngine

class HydraulicSystemUnitEntity:

    oil: OilEntity
    max_pressure: int

    def __init__(self):
        self.power: int
        self.hidraulic_systems: list[HydraulicSystemUnitEntity]
        self.engine: IEngine