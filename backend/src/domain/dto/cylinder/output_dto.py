from src.domain.entity.hydraulic_cylinder_entity import HydraulicCylinderEntity

class OutputCylinderDto:
    
    def __init__(self, entity: HydraulicCylinderEntity):
        self.id: int =          getattr(entity, "id")
        self. bore_diam: int =  getattr(entity,"bore_diam")
        self.rod_diam: int =    getattr(entity,"rod_diam")
        self.type: str =        getattr(entity, "type")

    def __str__(self):
        return(
            f"id: {self.id}\n"
            f"bore_diam: {self.bore_diam}\n"
            f"rod_diam: {self.rod_diam}\n"
            f"type: {self.type}"
        )
    
    def to_dict(self):
        return(
            {
                "id": self.id,
                "bore_diam": self.bore_diam,
                "rod_diam": self.rod_diam,
                "type": self.type

            }
        )