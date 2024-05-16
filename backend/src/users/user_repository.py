from dataBase import sqlite_db
from flask import request, jsonify
import json

class UserRepository():

    def __init__(self):
        pass

    def create():
        conn2 = sqlite_db.db_connection()
        cursor = conn2.cursor()
        
        print(request.form.get("email"))
        new_email = request.form.get("email")
        new_name = request.form.get("name")
        new_age = request.form.get("age")
        new_password = request.form.get("password")
        
        sql = """INSERT INTO users (email, name, age, password) VALUES(?, ?, ?, ?)"""
        cursor = conn2.execute(sql, (new_email, new_name, new_age, new_password))
        conn2.commit()
        
        return "User created {cursor.lastthrowid}"

    def update():
        user = "User updated into repository"
        return user
    
    def delete():
        user = "User deleted"
        return user

    def findOne():
        user = "User found"
        return user
        
        
        
    def findAll():
        cursor = conn.execute("SELECT * FROM users")
        users = [
            dict(id=row[0], email=row[1], name=row[2], age=row[3], password=row[4])
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users)