from flask import Blueprint, request
from src.users.user_service import UserService

controller = Blueprint("user_controller", __name__, static_folder="static", template_folder="template")


@controller.route('/create', methods= ['POST'])
def create():
    return UserService.create()

@controller.route('/update', methods= ['POST'])
def update():
    return UserService.update()

@controller.route('/delete', methods= ['DELETE'])
def delete():
    return UserService.delete()

@controller.route('/findOne', methods= ['GET'])
def findOne():
    return UserService.findOne()

@controller.route('/findAll', methods= ['GET'])
def findAll():
    return UserService.findAll()