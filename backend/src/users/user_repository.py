from flask import request, jsonify
import json
import sqlite3
from dataBase.sqlite_db import SqliteDb
from src.users.dto.input_dto import CreateUserDto

class UserRepository():

    def __init__(self):
        pass

    def create(dto):
        conn = SqliteDb.db_connection()
        
        try:
            sql = """INSERT INTO users (email, name, age, password) VALUES(?, ?, ?, ?)"""
            cursor = conn.execute(sql, (dto.email, dto.name, dto.age, dto.password))
            conn.commit()
       
            # Retrieve the newly inserted record
            cursor = conn.execute("SELECT * FROM users WHERE email = ?", (dto.email,))
            new_user = cursor.fetchone()
        
        except sqlite3.IntegrityError as e:
            conn.rollback()
            return jsonify({ "error": str(e)}), 400
        finally:
            conn.close
        
        return jsonify({"user": new_user})
        
    def update():
        user = "User updated into repository"
        return user
    
    def delete(email):
        conn = SqliteDb.db_connection()
        
        sql = """DELETE FROM users WHERE email=?"""
        conn.execute(sql, (email,))
        conn.commit()
         
        return "User deleted"

    def findOne(email):
        conn = SqliteDb.db_connection()
        cursor = conn.cursor()
        
        sql = """SELECT * FROM users WHERE email=?"""
        cursor.execute(sql, (email,))
        
        rows = cursor.fetchall()
        for r in rows:
            user = r
        if user is not None:
            return jsonify(user), 200
        else:
            return "Something Wrong"    
        
    def findAll():
        conn = SqliteDb.db_connection()
        cursor = conn.execute("SELECT * FROM users")
        users = [
            dict(email=row[0], name=row[1], age=row[2], password=row[3])
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users)