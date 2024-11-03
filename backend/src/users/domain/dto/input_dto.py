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

        additional_properties = set(json_data.keys()) - {"email", "name", "age", "password"}
        if additional_properties:
            raise TypeError("json has additional properties")
        
class InputUserBatchDto:

    def __init__(self, json_data_list):


        self.users: list[tuple[str, str,int,str]]
        
        self.users = []
        for user in json_data_list:
            user = user
            print("user..: ", user)
            self.users.append((user["email"], user["name"], user["age"], user["password"]))

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