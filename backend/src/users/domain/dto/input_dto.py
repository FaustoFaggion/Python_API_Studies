import json
from dataclasses import dataclass

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

        additional_properties = set(json_data.keys()) - {"email", "name", "age", "password"}
        if additional_properties:
            raise TypeError("json has additional properties")

    def to_tuple(self):
        return (self.email, self.name, self.age, self.password)

class InputUserBatchDto:

    def __init__(self, json_data_list):
        self.users: list[InputUserDto] = []

        for json_data in json_data_list:
            self.users.append(InputUserDto(json_data))

class DeleteUserBatchDto:

    def __init__(self, json_data_list):


        self.users: list[tuple[str, str,int,str]]
        
        self.users = []
        for user in json_data_list:
            self.users.append((user["email"]))


class UserIdDto:
    email:      str
        
    def __init__(self, json_data):
        self.email = json_data["email"]

        additional_properties = set(json_data.keys()) - {"email"}
        if additional_properties:
            raise TypeError("json has additional properties")