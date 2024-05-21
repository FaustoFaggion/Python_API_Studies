from flask import request, jsonify
import json
import sqlite3
from src.users.ports.user_repository_port import UserRepositoryPort
from src.users.dto.input_dto import InputUserDto, UserIdDto
from src.users.domain.user_entity import UserEntity, user_factory
from dataBase.adapters.sqlite_db import SqliteDb
from dataBase.ports.database_port import Database_Port

class UserRepository(UserRepositoryPort):

    def __init__(self, database: Database_Port) -> None:
        self.database = database

    def create(self, dto: InputUserDto):
        print("USER REPOSITORY")
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        # sql = """INSERT INTO users (email, name, age, password) VALUES(?, ?, ?, ?)"""
        sql = """INSERT INTO users (email, name, age, password) VALUES(%s, %s, %s, %s)"""
        cursor.execute(sql, (dto.email, dto.name, dto.age, dto.password))
        conn.commit()
    
        cursor.execute("SELECT * FROM users WHERE email = %s", (dto.email,))
        new_user = cursor.fetchone()
        response = user_factory(new_user)

        conn.close
        
        return response
        
    def update(self, dto: InputUserDto):
        print("USER REPOSITORY Update")
        print(dto.email)
        print(dto.age)
        conn = self.database.db_connection()
        cursor = conn.cursor()
         
        sql = """UPDATE users SET name=%s, age=%s, password=%s Where email=%s"""
        cursor.execute(sql, (dto.name, dto.age, dto.password, dto.email))
        conn.commit()
    
        cursor.execute("SELECT * FROM users WHERE email = %s", (dto.email,))
        user = cursor.fetchone()
        
        if user is None:
            conn.close()
            return None  
    
        response = user_factory(user)

        conn.close
        
        return response
    
    def delete(self, dto):
        conn = self.database.db_connection()
        cursor = conn.cursor()
         
        sql = """DELETE FROM users WHERE email=%s"""
        cursor.execute(sql, (dto.email,))
        conn.commit()
         
        if cursor.rowcount == 0:
            raise sqlite3.IntegrityError("User not found")

    def find_one(self, dto: UserIdDto):
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        sql = """SELECT * FROM users WHERE email=%s"""
        cursor.execute(sql, (dto.email,))
        user = cursor.fetchone()
        print(user)
        response: UserEntity = user_factory(user)
        print(response)

        conn.close
        
        return response
        
    def find_all(self):
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users")
        users = [
            dict(email=row[0], name=row[1], age=row[2], password=row[3])
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users)