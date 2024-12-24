import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask
from dataBase.ports.database_port import Database_Port
from dataBase.adapters.schema import DatabaseSchema
from dataBase.adapters.seed_database import query_values

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
                host="127.0.0.1", # to run local 127.0.0.1, to run into container postgres
                port="5432",
            )
            print("Connection established successfully:", conn)
        except psycopg2.Error as e:
            print(e)
        except Exception as e:
            print("An error occurred:", e)
        return conn
    
    def createTables(self, database_schema: DatabaseSchema):
        print("CREATE TABLES...")
        conn = self.db_connection()
        if conn is None:
            print("No connection to the database.")
            return
        try:
            cursor = conn.cursor()

            for table in database_schema.tables_schema:
                for key, value in table.items():
                    table_name = key
                    table_columns = value
                    cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE")
                    conn.commit()
                    sql_query = f"CREATE TABLE IF NOT EXISTS {table_name} {table_columns}"
                    cursor.execute(sql_query)
                    print(f"Tabela {table_name} criada com sucesso.")
                    conn.commit()

        except psycopg2.Error as e:
            print(f"Error executing SQL: {e}")
            if conn:
                conn.rollback()  # Rollback in case of error
        finally:
            if conn:
                cursor.close()
                conn.close()

    def seed_database(self, database_schema: DatabaseSchema):
        print("SEED TABLES...")
        
        conn = self.db_connection()
        if conn is None:
            print("No connection to the database.")
            return
        try:
            cursor = conn.cursor()

            for table in database_schema.tables_schema:
                print("table: ", table)
                for key, value in table.items():
                    table_name = key
                    table_columns = database_schema.table_columns[key]
                    #PARSE QUERY VALUES
                    executemany_values = []
                    for query_dict in query_values:
                        print('------')
                        for key, value in query_dict.items():
                            print("table_name: ", table_name)
                            print("key: ", key)
                            if table_name == key:
                                executemany_values = value
                                print("executemany: ", executemany_values)

                                if executemany_values:
                                    placeholders = ', '.join(['%s'] * len(executemany_values[0]))
                                    sql_query = f"INSERT INTO {table_name} {table_columns} VALUES({placeholders})"
                                    print("sql_query: ", sql_query)

                                    #EXECUTE QUERY
                                    cursor.executemany(sql_query, executemany_values)
                                    print(f"Tabela {table_name} criada com sucesso.")
                                    conn.commit()
                                    break

        except psycopg2.Error as e:
            print(f"Error executing SQL: {e}")
            if conn:
                conn.rollback()  # Rollback in case of error
        finally:
            if conn:
                cursor.close()
                conn.close()
