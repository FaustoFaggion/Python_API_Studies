import json

class InputUserDto:
    email:      str
    name:       str
    age:        int
    password:   str
    
    def __init__(self, json_data):
       
        self.email = json_data["email"]
        self.name = json_data["name"]
        self.age = json_data["age"]
        self.password = json_data["password"]
        
class UserIdDto:
    email:      str
        
    def __init__(self, json_data):
       
        self.email = json_data["email"]
