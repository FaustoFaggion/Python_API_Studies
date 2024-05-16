import sqlite3

# Criar a conexão com o banco de dados
conn = sqlite3.connect("dataBase.sqlite")
cursor = conn.cursor()

# Verificar se a tabela já existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
table_exists = cursor.fetchone()

# Se a tabela não existir, crie-a
if not table_exists:
    sql_query = """ CREATE TABLE users (
        email       text        PRIMARY KEY,
        name        text        NOT NULL,
        age         number      NOT NULL,
        password    text        NOT NULL
    )"""
    cursor.execute(sql_query)
    print("Tabela 'users' criada com sucesso.")

# Fechar a conexão
# conn.close()

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("dataBase.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn