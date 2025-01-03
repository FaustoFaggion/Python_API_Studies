from dataclasses import asdict
import json
import sqlite3
import werkzeug
from flask import Blueprint, request, jsonify, make_response
from src.users.domain.dto.input_dto import InputUserDto, UserIdDto, InputUserBatchDto, DeleteUserBatchDto
from src.users.domain.dto.output_dto import OutputUserDto
from src.users.useCases.user_service import UserService
from src.users.ports.input.user_service_port import UserServicePort
from src.users.ports.output.user_repository_port import UserRepositoryPort
from dataBase.ports.database_port import Database_Port
from dataBase.adapters.sqlite_db import SqliteDb

class UserController:

    def __init__(self, user_service: UserServicePort):
        self.user_service = user_service
        self.controller = Blueprint("user_controller", __name__, static_folder="static", template_folder="template")
        self.register_routes()

    def register_routes(self):
        self.controller.route('/create', methods=['POST'])(self.create)
        self.controller.route('/update', methods=['PUT'])(self.update)
        self.controller.route('/delete', methods=['DELETE'])(self.delete)
        self.controller.route('/find_one/<email>', methods=['GET'])(self.find_one)
        self.controller.route('/find_all', methods=['GET'])(self.find_all)

    def create(self):
        print("USER CONTROLLER")
        try:
            # GET JSON DATA FROM REQUEST
            json_data = request.get_json()

            # SEND JSON DATA AS DTO TO SERVICE MODULE
            dto: InputUserBatchDto = InputUserBatchDto(json_data)
            output_dto_list: list[OutputUserDto] = self.user_service.create(dto)
            
            # TRANSFORM OutputUserDto LIST INTO JSON TO RESPOND
            response: list = []
            for user in output_dto_list:
                response.append(asdict(user))
            return json.dumps(response)
            
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
            # dto: InputUserDto = InputUserDto(json_data)
            dto: InputUserBatchDto = InputUserBatchDto(json_data)
            output_dto_list: list[OutputUserDto] = self.user_service.update(dto)
            
            # TRANSFORM OutputUserDto LIST INTO JSON TO RESPOND
            response: list = []
            for user in output_dto_list:
                response.append(asdict(user))
            return json.dumps(response)
            
        except TypeError as e:
            return make_response(jsonify({"error a": str(e)}), 415)  # Retorna 500 Internal Server Error para outros erros
        except sqlite3.IntegrityError as e:
            return make_response(jsonify({ "error b": str(e)}), 400)
        except werkzeug.exceptions.BadRequest as e:
            return make_response(jsonify({"error c": str(e)}), 400) # erro  request.get_json()
        except Exception as e:
            return make_response(jsonify({ "error d": str(e)}), 500)

        return response

    def delete(self):
        print("USER CONTROLLER delete")
        try:
            # json_data = {'email': email}
            # print(json_data)
            # dto: UserIdDto = UserIdDto(json_data)
            json_data = request.get_json()
            print(json_data)
            dto: DeleteUserBatchDto = DeleteUserBatchDto(json_data)
            self.user_service.delete(dto)
        
            response = "User deleted", 204        
        
        except TypeError as e:
            return make_response(jsonify({"error a": str(e)}), 415)  # Retorna 500 Internal Server Error para outros erros
        except sqlite3.IntegrityError as e:
            return make_response(jsonify({ "error b": str(e)}), 400)
        except werkzeug.exceptions.BadRequest as e:
            return make_response(jsonify({"error c": str(e)}), 400) # erro  request.get_json()
        except Exception as e:
            return make_response(jsonify({ "error d": str(e)}), 500)

        return response
    
    def find_one(self, email):
        print("USER CONTROLLER find_one")
        try:
            json_data = {'email': email}
            print(json_data)
            dto: UserIdDto = UserIdDto(json_data)
            user = self.user_service.find_one(dto)
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
        print("FIND ALL REPOSITORY")
        try:
            return self.user_service.find_all()
        except TypeError as e:
            return make_response(jsonify({"error a": str(e)}), 415)  # Retorna 500 Internal Server Error para outros erros
        except sqlite3.IntegrityError as e:
            return make_response(jsonify({ "error b": str(e)}), 400)
        except werkzeug.exceptions.BadRequest as e:
            return make_response(jsonify({"error c": str(e)}), 400) # erro  request.get_json()
        except Exception as e:
            return make_response(jsonify({ "error d": str(e)}), 500)
        return response