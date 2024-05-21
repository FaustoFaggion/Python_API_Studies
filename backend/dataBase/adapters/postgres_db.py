import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask
from dataBase.ports.database_port import Database_Port

load_dotenv()

class PostgresDb(Database_Port):
    
    def __init__(self):
       pass
    
    def db_connection(self):
        conn = None
        try:
            # url = os.getenv("DATA_URL")
            conn = psycopg2.connect(
                dbname="mydb",
                user="myuser",
                password="mypassword",
                host="127.0.0.1",
                port="5432",
            )
            print("Connection established successfully:", conn)
        except psycopg2.Error as e:
            print(e)
        return conn
    
    def createTables(self):
        print("CREATE TABLES...")
        conn = self.db_connection()
        if conn is None:
            print("No connection to the database.")
            return
        try:
            cursor = conn.cursor()
        
            cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' And table_name = 'users';""")
            table_exists = cursor.fetchone()

            if not table_exists:
                sql_query = """CREATE TABLE users (
                    email       TEXT        PRIMARY KEY,
                    name        TEXT        NOT NULL,
                    age         INTEGER     NOT NULL,
                    password    TEXT        NOT NULL
                );"""
                cursor.execute(sql_query)
                print("Tabela 'users' criada com sucesso.")
                conn.commit()
            else:
                print("Tabela 'users' já existe.")
        except psycopg2.Error as e:
            print(f"Error executing SQL: {e}")
            if conn:
                conn.rollback()  # Rollback in case of error
        finally:
            if conn:
                cursor.close()
                conn.close()
