from src.domain.entity.pump_entity import PumpEntity

class HydraulicSystemEntity:

    def __init__(self, max_pressure):
        self.power: int
        max_pressure: int
        work_pressure: int
        self.max_flow: int
        self.work_flow: int
        self.pump: PumpEntity
        