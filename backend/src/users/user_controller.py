from flask import Blueprint, request
from src.users.user_service import UserService
from src.users.dto.input_dto import CreateUserDto

controller = Blueprint("user_controller", __name__, static_folder="static", template_folder="template")


@controller.route('/create', methods= ['POST'])
def create():
    return UserService.create()

@controller.route('/update', methods= ['POST'])
def update():
    return UserService.update()

@controller.route('/delete/<email>', methods= ['DELETE'])
def delete(email):
    print(email)
    return UserService.delete(email)

@controller.route('/findOne/<email>', methods= ['GET'])
def findOne(email):
    return UserService.findOne(email)

@controller.route('/findAll', methods= ['GET'])
def findAll():
    return UserService.findAll()