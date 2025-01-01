import json
from flask import Blueprint, request, jsonify, make_response
from dataBase.ports.database_port import Database_Port
from src.domain.dto.cylinder.input_dto import CylinderIdDto
from src.useCases.cylinder_service import CylinderService

class CylinderController:

    def __init__(self, cylinder_service: CylinderService):
        self.cylinder_service = cylinder_service
        self.controller = Blueprint("cylinder_controller", __name__, static_folder="static", template_folder="template")
        self.register_routes()
        
    def register_routes(self):
        self.controller.route('/find_one/<id>', methods=['GET'])(self.find_one)

    def find_one(self, id):
        print("CYLINDER CONTROLLER find_one")
        json_data = {'id': id}
        print(json_data)
        dto: CylinderIdDto = CylinderIdDto(json_data)
        print("dto: ", dto)
        cylinder = self.cylinder_service.find_one(dto)
        print("cylinder: ", cylinder)

        return json.dumps(cylinder.to_dict())

        