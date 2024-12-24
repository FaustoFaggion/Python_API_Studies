from typing import List
from flask import request, jsonify
import json
import sqlite3
from src.users.domain.dto.output_dto import OutputUserDto
from src.users.ports.output.user_repository_port import UserRepositoryPort
from src.users.domain.dto.input_dto import InputUserDto, UserIdDto, InputUserBatchDto, DeleteUserBatchDto
from src.users.domain.entities.user_entity import UserEntity
from dataBase.adapters.sqlite_db import SqliteDb
from dataBase.ports.database_port import Database_Port
from dataBase.adapters.sql_syntax import SqlSyntax
from dataclasses import asdict, astuple

class UserRepositoryPostgres(UserRepositoryPort):

    def __init__(self, database: Database_Port) -> None:
        self.database = database

    def sql_syntax(self):
        conn = self.database.db_connection()
        cursor = conn.cursor()

        print("\n\nsql syntax function\n")
        print(SqlSyntax.SELECT_column_FROM_table("users", "email", "age"))
        print(SqlSyntax.SELECT_DISTINCT_column_FROM_table("users", "email", "age"))


    def create(self, entities_list: list[UserEntity]):
        print("USER REPOSITORY")

        #PREPARE DATA TO EXECUTEMANY FUNCTION
        users_list: list[tuple] = []
        for entity in entities_list:
            users_list.append(entity.to_tuple())

        # CREATE DATABASE CONNECTION
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        # DEFINE SQL QUERY
        sql = """INSERT INTO users (email, name, age, password) VALUES(%s, %s, %s, %s);"""

        # EXECUTE QUERY TO DATABASE
        cursor.executemany(sql, entities_list)

        # SAVE CHANGE PERMANENTLY INTO DATABASE
        conn.commit()

        # GET DATA TO RETURN TO SERVICE MODULE
        inserted_emails = [user[0] for user in users_list]
        placeholders = ', '.join(['%s'] * len(inserted_emails))
        
        # EXECUTE QUERY TO DATABASE
        cursor.execute(f"SELECT * FROM users WHERE email IN ({placeholders})", inserted_emails)
        new_users = cursor.fetchall()
        print("before new_Users: ", new_users)

        # CLOSE CONNECTION AND CURSOR
        cursor.close()
        conn.close()
        
        # CREATE ENTITIES LIST TO RETURN TO SERVICE MODULE
        response: List[UserEntity] = []
        for user in new_users:
            response.append(UserEntity(user)) 
        
        return response   
        
    def update(self, entities_list: list[UserEntity]):
        print("USER REPOSITORY UPDATE")

        #PREPARE DATA TO EXECUTEMANY FUNCTION
        users_list: list[tuple] = []
        for entity in entities_list:
            user_tuple = (entity.name, entity.age, entity.password, entity.email)
            users_list.append(user_tuple)
        
        # CREATE DATABASE CONNECTION
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        # DEFINE SQL QUERY
        query = "UPDATE users SET name = %s, age = %s, password = %s WHERE email = %s"
        
        # EXECUTE QUERY TO DATABASE
        cursor.executemany(query, users_list)
        
        # SAVE CHANGE PERMANENTLY INTO DATABASE
        conn.commit()

        # DEFINE SQL QUERY TO RETURN DATA
        inserted_emails = [user[3] for user in users_list]
        placeholders = ', '.join(['%s'] * len(inserted_emails))
        query = f"SELECT * FROM users WHERE email IN ({placeholders})"

        # EXECUTE QUERY TO DATABASE
        cursor.execute(query, inserted_emails)
        updated_users = cursor.fetchall()
        print("updated_users: ", updated_users)
        
        # CLOSE CONNECTION AND CURSOR
        cursor.close()
        conn.close()

        # CREATE ENTITIES LIST TO RETURN TO SERVICE MODULE
        response: List[UserEntity] = []
        for user in updated_users:
            response.append(UserEntity(user)) 
        
        return response   
    
    def delete(self, dto: InputUserBatchDto):
        print("DELETE REPOSITORY")
        
        #PREPARE DATA TO EXECUTEMANY FUNCTION
        users = tuple(dto.users)
        print("users_email: ", users)

        # CREATE DATABASE CONNECTION
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        # DEFINE SQL QUERY
        sql = f"DELETE FROM users WHERE email IN {users}"

        # EXECUTE QUERY TO DATABASE
        cursor.executemany(sql, users)
        
        # SAVE CHANGE PERMANENTLY INTO DATABASE
        conn.commit()

        # CLOSE CONNECTION AND CURSOR
        cursor.close()
        conn.close()
        
        if cursor.rowcount == 0:
            raise sqlite3.IntegrityError("User not found")
    
        return None

    def find_one(self, dto: UserIdDto):
        print("FIND ONE")
        # CREATE DATABASE CONNECTION
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        # DEFINE SQL QUERY
        sql = """SELECT * FROM users WHERE email=%s"""
        
        # EXECUTE QUERY TO DATABASE
        cursor.execute(sql, (dto.email,))
        user = cursor.fetchone()
        print(user)

        # CLOSE CONNECTION AND CURSOR
        cursor.close()
        conn.close()
        
        # CREATE ENTITY TO RETURN TO SERVICE MODULE
        response: UserEntity = UserEntity(user)

        return response
        
    def find_all(self):

        # CREATE DATABASE CONNECTION
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        # DEFINE SQL QUERY
        query = "SELECT * FROM users"
        
        # EXECUTE QUERY TO DATABASE
        cursor.execute(query)
        entities = cursor.fetchall()

        # CLOSE CONNECTION AND CURSOR
        cursor.close()
        conn.close()

        # CREATE ENTITIES LIST TO RETURN TO SERVICE MODULE
        response: list[UserEntity] = []
        for user_entity in entities:
            response.append(UserEntity(user_entity)) 

        return response
