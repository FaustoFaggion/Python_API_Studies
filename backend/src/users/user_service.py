from src.users.user_repository import UserRepository

class UserService():
    
    def __init__(self):
        pass

    def create():
        user = UserRepository.create()
        return user
    
    def update():
        user = UserRepository.update()
        return user
    
    def delete(email):
        return UserRepository.delete(email)

    def findOne(email):
        user = UserRepository.findOne(email)
        return user
    
    def findAll():
        user = UserRepository.findAll()
        return user