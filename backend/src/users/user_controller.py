from dataclasses import asdict
import json
import sqlite3

import werkzeug
from flask import Blueprint, request, jsonify, make_response
from src.users.user_service import UserService
from src.users.user_repository import UserRepository
from src.users.ports.user_service_port import UserServicePort
from src.users.ports.user_repository_port import UserRepositoryPort

class UserController:

    def __init__(self, user_service: UserServicePort):
        self.user_service = user_service
        self.controller = Blueprint("user_controller", __name__, static_folder="static", template_folder="template")
        self.register_routes()

    def register_routes(self):
        self.controller.route('/create', methods=['POST'])(self.create)
        self.controller.route('/update', methods=['PUT'])(self.update)
        self.controller.route('/delete/<email>', methods=['DELETE'])(self.delete)
        self.controller.route('/find_one/<email>', methods=['GET'])(self.find_one)
        self.controller.route('/find_all', methods=['GET'])(self.find_all)

    def create(self):
        print("USER CONTROLLER")
        try:
            json_data = request.get_json()
            user = self.user_service.create(json_data)
            dto_dict = asdict(user)
            response = json.dumps(dto_dict)
            
        except TypeError as e:
            return make_response(jsonify({"error a": str(e)}), 415)  # Retorna 500 Internal Server Error para outros erros
        except sqlite3.IntegrityError as e:
            return make_response(jsonify({ "error b": str(e)}), 400)
        except werkzeug.exceptions.BadRequest as e:
            return make_response(jsonify({"error c": str(e)}), 400) # erro  request.get_json()
        except Exception as e:
            return make_response(jsonify({ "error d": str(e)}), 500)
        return response

    def update(self):
        print("USER CONTROLLER Update")
        try:
            json_data = request.get_json()
            print(json_data)
            user = self.user_service.update(json_data)
            dto_dict = asdict(user)
            response = json.dumps(dto_dict)
            
        except TypeError as e:
            return make_response(jsonify({"error a": str(e)}), 415)  # Retorna 500 Internal Server Error para outros erros
        except sqlite3.IntegrityError as e:
            return make_response(jsonify({ "error b": str(e)}), 400)
        except werkzeug.exceptions.BadRequest as e:
            return make_response(jsonify({"error c": str(e)}), 400) # erro  request.get_json()
        except Exception as e:
            return make_response(jsonify({ "error d": str(e)}), 500)

        return response

    def delete(self, email):
        return self.user_service.delete(email)

    def find_one(self, email):
        print("USER CONTROLLER find_one")
        try:
            json_data = {'email': email}
            print(json_data)
            user = self.user_service.find_one(json_data)
            dto_dict = asdict(user)
            response = json.dumps(dto_dict)
            
        except TypeError as e:
            return make_response(jsonify({"error a": str(e)}), 415)  # Retorna 500 Internal Server Error para outros erros
        except sqlite3.IntegrityError as e:
            return make_response(jsonify({ "error b": str(e)}), 400)
        except werkzeug.exceptions.BadRequest as e:
            return make_response(jsonify({"error c": str(e)}), 400) # erro  request.get_json()
        except Exception as e:
            return make_response(jsonify({ "error d": str(e)}), 500)
        return response

    def find_all(self):
        return self.user_service.find_all()

# To create an instance of UserController and access its blueprint:
user_repo: UserRepositoryPort = UserRepository()
user_service: UserServicePort = UserService(user_repo)
user_controller = UserController(user_service)
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