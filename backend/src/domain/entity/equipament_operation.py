from src.domain.entity.device import DeviceEntity

class EquipamentOperation:

    def __init__(self):
        self.power: int
        self.devices: list[DeviceEntity]