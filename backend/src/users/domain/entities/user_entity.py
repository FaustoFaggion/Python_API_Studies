from dataclasses import dataclass

# implementing __init__, __repr__, __eq__ behind the scenes
@dataclass
class UserEntity:
    email:      str
    name:       str
    age:        int
    password:   str
    
    def __init__(self, *data):
        self.email=data[0]
        self.name=data[1]
        self.age=data[2]
        self.password=data[3]