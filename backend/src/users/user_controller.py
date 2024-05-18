from flask import Blueprint, request, jsonify
from src.users.user_service import UserService
from src.users.user_repository import UserRepository
from src.users.ports.user_service_port import UserServicePort

class UserController:

    def __init__(self):
        self.user_repository = UserRepository()
        self.user_service = UserService(self.user_repository)
        self.controller = Blueprint("user_controller", __name__, static_folder="static", template_folder="template")
        self.register_routes()

    def register_routes(self):
        self.controller.route('/create', methods=['POST'])(self.create)
        self.controller.route('/update', methods=['PUT'])(self.update)
        self.controller.route('/delete/<email>', methods=['DELETE'])(self.delete)
        self.controller.route('/find_one/<email>', methods=['GET'])(self.find_one)
        self.controller.route('/find_all', methods=['GET'])(self.find_all)

    def create(self):
        return self.user_service.create()

    def update(self):
        return self.user_service.update()

    def delete(self, email):
        return self.user_service.delete(email)

    def find_one(self, email):
        return self.user_service.find_one(email)

    def find_all(self):
        return self.user_service.find_all()

# To create an instance of UserController and access its blueprint:
user_controller = UserController()
controller_blueprint = user_controller.controller





# from flask import Blueprint, request
# from src.users.user_service import UserService
# from src.users.user_repository import UserRepository
# from src.users.dto.input_dto import CreateUserDto


# # Initialize repository and service
# user_repository = UserRepository()
# user_service = UserService(user_repository)

# controller = Blueprint("user_controller", __name__, static_folder="static", template_folder="template")


# @controller.route('/create', methods= ['POST'])
# def create():
#     return user_service.create()

# @controller.route('/update', methods= ['POST'])
# def update():
#     return user_service.update()

# @controller.route('/delete/<email>', methods= ['DELETE'])
# def delete(email):
#     print(email)
#     return user_service.delete(email)

# @controller.route('/findOne/<email>', methods= ['GET'])
# def findOne(email):
#     return user_service.findOne(email)

# @controller.route('/findAll', methods= ['GET'])
# def findAll():
#     return user_service.findAll()