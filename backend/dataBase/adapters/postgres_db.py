import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask
from dataBase.ports.database_port import Database_Port

load_dotenv()

class PostgresDb(Database_Port):
    
    def __init__(self):
       pass
    
    def db_connection(self, ):
        conn = None
        try:
            # url = os.getenv("DATA_URL")
            conn = psycopg2.connect(
                dbname="mydb",
                user="myuser",
                password="mypassword",
                host="127.0.0.1", # to run local 127.0.0.1, to run into container postgres
                port="5432",
            )
            print("Connection established successfully:", conn)
        except psycopg2.Error as e:
            print(e)
        except Exception as e:
            print("An error occurred:", e)
        return conn
    
    def createTables(self, tables_schema):
        print("CREATE TABLES...")
        conn = self.db_connection()
        if conn is None:
            print("No connection to the database.")
            return
        try:
            cursor = conn.cursor()


            for table in tables_schema:
                schema = tables_schema[table]
                sql_query = f"CREATE TABLE IF NOT EXISTS {table} {schema}"
                cursor.execute(sql_query)
                print("Tabela 'users' criada com sucesso.")
                conn.commit()

        except psycopg2.Error as e:
            print(f"Error executing SQL: {e}")
            if conn:
                conn.rollback()  # Rollback in case of error
        finally:
            if conn:
                cursor.close()
                conn.close()
