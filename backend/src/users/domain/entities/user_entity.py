from dataclasses import dataclass

# implementing __init__, __repr__, __eq__ behind the scenes
class UserEntity:
    
    def __init__(self, data):
        self.email=data[0]
        self.name=data[1]
        self.age=data[2]
        self.password=data[3]

    def to_tuple(self):
        return (self.email, self.name, self.age, self.password)
    
    def to_tuple_updatable_params(self):
        return (self.name, self.age, self.password)