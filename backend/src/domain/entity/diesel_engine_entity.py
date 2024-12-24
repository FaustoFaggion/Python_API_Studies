from src.domain.interface.engine_interface import IEngine


class DieselEngine(IEngine):

    def __init__(self):
        self.power:  int
        self.efficiency_mec: int

    def power(self) -> int:
        pass
    