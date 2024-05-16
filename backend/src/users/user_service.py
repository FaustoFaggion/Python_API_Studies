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
    
    def delete():
        return UserRepository.delete()

    def findOne():
        user = UserRepository.findOne()
        return user
    
    def findAll():
        user = list(UserRepository.findAll())
        return user