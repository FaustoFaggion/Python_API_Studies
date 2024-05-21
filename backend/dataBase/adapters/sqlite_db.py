import sqlite3
from dataBase.ports.database_port import Database_Port

class SqliteDb(Database_Port):
    
    def __init__(self):
        pass
    
    def db_connection(self):
        conn = None
        try:
            conn = sqlite3.connect("dataBase.sqlite")
        except sqlite3.error as e:
            print(e)
        return conn
    
    def createTables(self):
        conn = self.db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        table_exists = cursor.fetchone()

        if not table_exists:
            sql_query = """CREATE TABLE IF NT EXISTS users (
                email       text        PRIMARY KEY,
                name        text        NOT NULL,
                age         number      NOT NULL,
                password    text        NOT NULL
            )"""
            cursor.execute(sql_query)
            print("Tabela 'users' criada com sucesso.")