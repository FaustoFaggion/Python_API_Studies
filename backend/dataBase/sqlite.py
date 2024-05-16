import sqlite3

conn = sqlite3.connect("dataBase.sqlite")

# CURSOR OBJECT USED TO EXECUTE SQL STATMENTS
cursor = conn.cursor() 

sql_query = """ CREATE TABLE user (
    email   text        PRIMARY KEY,
    name    text        NOT NULL,
    age     number      NOT NULL
)"""

cursor.execute(sql_query)