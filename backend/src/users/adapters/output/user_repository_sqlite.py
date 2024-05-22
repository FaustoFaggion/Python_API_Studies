from typing import List
from flask import request, jsonify
import json
import sqlite3
from src.users.ports.output.user_repository_port import UserRepositoryPort
from src.users.domain.dto.input_dto import InputUserDto, UserIdDto
from src.users.domain.entities.user_entity import UserEntity, user_factory
from dataBase.adapters.sqlite_db import SqliteDb
from dataBase.ports.database_port import Database_Port

class UserRepositorySqlite(UserRepositoryPort):

    def __init__(self, database: Database_Port) -> None:
        self.database = database

    def create(self, dto: InputUserDto):
        print("USER REPOSITORY")
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        # sql = """INSERT INTO users (email, name, age, password) VALUES(?, ?, ?, ?)"""
        sql = """INSERT INTO users (email, name, age, password) VALUES(?, ?, ?, ?)"""
        cursor.execute(sql, (dto.email, dto.name, dto.age, dto.password))
        conn.commit()
    
        cursor.execute("SELECT * FROM users WHERE email = ?", (dto.email,))
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
         
        sql = """UPDATE users SET name=?, age=?, password=? Where email=?"""
        cursor.execute(sql, (dto.name, dto.age, dto.password, dto.email))
        conn.commit()
    
        cursor.execute("SELECT * FROM users WHERE email = ?", (dto.email,))
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
         
        sql = """DELETE FROM users WHERE email=?"""
        cursor.execute(sql, (dto.email,))
        conn.commit()
         
        if cursor.rowcount == 0:
            raise sqlite3.IntegrityError("User not found")

    def find_one(self, dto: UserIdDto):
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        sql = """SELECT * FROM users WHERE email=?"""
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
        users: List[UserEntity] = [
            user_factory(row)
            for row in cursor.fetchall()
        ]
        
        return users