from flask import Blueprint, request, jsonify, make_response
from dataBase.ports.database_port import Database_Port
import json

class CylinderController:

    def __init__(self, database: Database_Port):
        self.controller = Blueprint("cylinder_controller", __name__, static_folder="static", template_folder="template")
        self.register_routes()
        self.database = database

    def register_routes(self):
        self.controller.route('/find_one/<id>', methods=['GET'])(self.find_one)

    def find_one(self, id):
        print("CYLINDER CONTROLLER find_one")

        json_data = {'id': id}
        print(json_data)
        # dto: UserIdDto = UserIdDto(json_data)
        # user = self.user_service.find_one(dto)
        # dto_dict = asdict(user)
        # response = json.dumps(dto_dict)

        # CREATE DATABASE CONNECTION
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        # DEFINE SQL QUERY
        sql = f"SELECT * FROM cylinder WHERE id={id}"
        
        # EXECUTE QUERY TO DATABASE
        cursor.execute(sql)
        cylinder = cursor.fetchone()

        # CLOSE CONNECTION AND CURSOR
        cursor.close()
        conn.close()

        response = json.dumps(cylinder)

        return response