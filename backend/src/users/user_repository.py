from dataBase.sqlite_db import SqliteDb
from flask import request, jsonify
import json

class UserRepository():

    def __init__(self):
        pass

    def create():
        conn = SqliteDb.db_connection()
        
        print(request.form.get("email"))
        new_email = request.form.get("email")
        new_name = request.form.get("name")
        new_age = request.form.get("age")
        new_password = request.form.get("password")
        
        sql = """INSERT INTO users (email, name, age, password) VALUES(?, ?, ?, ?)"""
        cursor = conn.execute(sql, (new_email, new_name, new_age, new_password))
        conn.commit()
        
        return "User created {cursor.lastthrowid}"

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