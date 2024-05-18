from flask import Blueprint, request
from src.users.user_service import UserService
from src.users.user_repository import UserRepository
from src.users.dto.input_dto import CreateUserDto


# Initialize repository and service
user_repository = UserRepository()
user_service = UserService(user_repository)

controller = Blueprint("user_controller", __name__, static_folder="static", template_folder="template")


@controller.route('/create', methods= ['POST'])
def create():
    return user_service.create()

@controller.route('/update', methods= ['POST'])
def update():
    return user_service.update()

@controller.route('/delete/<email>', methods= ['DELETE'])
def delete(email):
    print(email)
    return user_service.delete(email)

@controller.route('/findOne/<email>', methods= ['GET'])
def findOne(email):
    return user_service.findOne(email)

@controller.route('/findAll', methods= ['GET'])
def findAll():
    return user_service.findAll()