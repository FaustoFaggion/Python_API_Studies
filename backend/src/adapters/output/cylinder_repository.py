from flask import Blueprint, request, jsonify, make_response
import json
from dataBase.ports.database_port import Database_Port
from src.domain.entity.hydraulic_cylinder_entity import HydraulicCylinderEntity 

class CylinderRepository:

    def __init__(self, database: Database_Port):
        self.database = database

    def find_one(self, dto):
        cylinder_id = dto.id
        print("CYLINDER REPOSITORY find_one")
        # CREATE DATABASE CONNECTION
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        # DEFINE SQL QUERY
        sql = f"SELECT * FROM cylinder WHERE id= {cylinder_id}"

        # EXECUTE QUERY TO DATABASE
        cursor.execute(sql)
        cylinder = cursor.fetchone()

        # CLOSE CONNECTION AND CURSOR
        cursor.close()
        conn.close()

        # PARSE RESPONSE
        cylinder_entity: HydraulicCylinderEntity = HydraulicCylinderEntity(cylinder)
        return cylinder_entity