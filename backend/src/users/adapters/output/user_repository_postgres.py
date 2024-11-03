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

class UserRepositoryPostgres(UserRepositoryPort):

    def __init__(self, database: Database_Port) -> None:
        self.database = database

    def sql_syntax(self):
        conn = self.database.db_connection()
        cursor = conn.cursor()

        print("\n\nsql syntax function\n")
        print(SqlSyntax.SELECT_column_FROM_table("users", "email", "age"))
        print(SqlSyntax.SELECT_DISTINCT_column_FROM_table("users", "email", "age"))


    def create(self, dto: InputUserBatchDto):
        print("USER REPOSITORY")
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        sql = """INSERT INTO users (email, name, age, password) VALUES(%s, %s, %s, %s);"""
        if not dto.users:
            raise ValueError("No users to insert")
        
        cursor.executemany(sql, dto.users)
        conn.commit()

        inserted_emails = [user[0] for user in dto.users]
        placeholders = ', '.join(['%s'] * len(inserted_emails))
        
        cursor.execute(f"SELECT * FROM users WHERE email IN ({placeholders})", inserted_emails)

        new_users = cursor.fetchall()
        print("new_Users: ", new_users)
        response: List[UserEntity] = [
            UserEntity(*row)for row in new_users] 
        conn.close
        print("new_Users: ", response)
        return response   
        
    def update(self, dto: DeleteUserBatchDto):
        print("USER REPOSITORY Update")
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        # sql = """UPDATE users SET name=%s, age=%s, password=%s Where email=%s"""
        query = """INSERT INTO users (email, name, age, password) values(%s, %s, %s, %s) ON CONFLICT (email) DO UPDATE SET name=EXCLUDED.name, age=EXCLUDED.age;"""
        
        print("Executing query: ", query)
        print("With parameters: ", dto.users)

        cursor.executemany(query, dto.users)
        conn.commit()
        print("aaaa")
        inserted_emails = [user[0] for user in dto.users]
        placeholders = ', '.join(['%s'] * len(inserted_emails))
        
        cursor.execute(f"SELECT * FROM users WHERE email IN ({placeholders})", inserted_emails)

        updated_users = cursor.fetchall()
        print("updated_users: ", updated_users)
        response: List[UserEntity] = [
            UserEntity(*row)for row in updated_users] 
        conn.close
        print("new_Users: ", response)
        return response   
    
    def delete(self, dto: InputUserBatchDto):
        conn = self.database.db_connection()
        cursor = conn.cursor()
        print("dto.users: ", dto.users)
        
        sql = f"DELETE FROM users WHERE email IN {tuple(dto.users)}"
        cursor.executemany(sql, dto.users)
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
        response: UserEntity = UserEntity(user)
        print(response)

        conn.close
        
        return response
        
    def find_all(self):
        conn = self.database.db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users")
        users: List[UserEntity] = [
            UserEntity(row)for row in cursor.fetchall()] 
        
        return users
