
class CylinderIdDto:
    id:      int
        
    def __init__(self, json_data):
        self.id = json_data["id"]
        print("dto json data: ", json_data)
        print("dto id: ", self.id)

        additional_properties = set(json_data.keys()) - {"id"}
        if additional_properties:
            raise TypeError("json has additional properties")