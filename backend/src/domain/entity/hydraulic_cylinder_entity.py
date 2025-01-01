

class HydraulicCylinderEntity:
    
    def __init__(self, data):
        self.id: int = data[0]
        self.power: int = 0
        self.efficiency_mec: int = data[1]
        self.efficiency_hid: int = data[2]
        self.bore_diam = data[4]
        self.bore_area = 0
        self.extend_force = 0
        self.extend_veloc = 0
        self.extend_volume = 0
        self.extend_time = 0
        self.rod_diam = data[3]
        self.rod_area = 0
        self.retract_force = 0
        self.retract_veloc = 0
        self.retract_volume = 0
        self.retract_time = 0
        self.ratio_area = 0
        self.flow_output_rod = 0
        self.flow_output_bore = 0
        self.type = data[4]

    def __str__(self):
        return(f"cylinder_id: {self.id}\n"
              f"bore_diam: {self.bore_diam}\n"
              f"rod_diam: {self.rod_diam}\n"
              f"mec_efficiency: {self.efficiency_mec}\n"
              f"hidr_eficiency: {self.efficiency_hid}\n"
              f"type: {self.type}\n")