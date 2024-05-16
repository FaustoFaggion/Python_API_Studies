from flask import Blueprint
from src.users.user_service import UserService

user_controller = Blueprint("user_controller", __name__, static_folder="static", template_folder="template")


@user_controller.route('/create', methods= ['GET'])
def create():
    return UserService.create()

@user_controller.route('/update', methods= ['POST'])
def update():
    return UserService.update()

@user_controller.route('/delete', methods= ['DELETE'])
def delete():
    return UserService.delete()

@user_controller.route('/findOne', methods= ['GET'])
def findOne():
    return UserService.findOne()

@user_controller.route('/findAll', methods= ['GET'])
def findAll():
    return UserService.findAll()