from flask import request, jsonify
import json
import sqlite3
from dataBase.sqlite_db import SqliteDb
from src.users.ports.user_repository_port import UserRepositoryPort
from src.users.dto.input_dto import InputUserDto, UserIdDto
from src.users.domain.user_entity import UserEntity, user_factory

class UserRepository(UserRepositoryPort):

    def __init__(self) -> None:
        pass

    def create(self, dto: InputUserDto):
        print("USER REPOSITORY")
        conn = SqliteDb.db_connection()
        
        sql = """INSERT INTO users (email, name, age, password) VALUES(?, ?, ?, ?)"""
        cursor = conn.execute(sql, (dto.email, dto.name, dto.age, dto.password))
        conn.commit()
    
        cursor = conn.execute("SELECT * FROM users WHERE email = ?", (dto.email,))
        new_user = cursor.fetchone()
        response = user_factory(new_user)

        conn.close
        
        return response
        
    def update(self, dto: InputUserDto):
        print("USER REPOSITORY Update")
        print(dto.email)
        print(dto.age)
        conn = SqliteDb.db_connection()
        
        sql = """UPDATE users SET name=?, age=?, password=? Where email=?"""
        cursor = conn.execute(sql, (dto.name, dto.age, dto.password, dto.email))
        conn.commit()
    
        cursor = conn.execute("SELECT * FROM users WHERE email = ?", (dto.email,))
        user = cursor.fetchone()
        response = user_factory(user)

        conn.close
        
        return response
    
    def delete(self, email):
        conn = SqliteDb.db_connection()
        
        sql = """DELETE FROM users WHERE email=?"""
        conn.execute(sql, (email,))
        conn.commit()
         
        return "User deleted"

    def find_one(self, dto: UserIdDto):
        conn = SqliteDb.db_connection()
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
        conn = SqliteDb.db_connection()
        cursor = conn.execute("SELECT * FROM users")
        users = [
            dict(email=row[0], name=row[1], age=row[2], password=row[3])
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users)