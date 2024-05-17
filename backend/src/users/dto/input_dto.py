import json

class CreateUserDto:
    email:      str
    name:       str
    age:        int
    password:   str
    
    def __init__(self, json_data):
        data = json.loads(json_data)
        self.email = data["email"]
        self.name = data["name"]
        self.age = data["age"]
        self.password = data["password"]