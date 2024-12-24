from src.domain.entity.hydraulic_system_unit_entity import HydraulicSystemUnitEntity


class EquipamentEntity:

    application: str
    use_condition: str
    
    def __init__(self):
        self.power: int
        self.hidraulic_systems: list[HydraulicSystemUnitEntity]