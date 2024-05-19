from flask import Flask, request, jsonify
from src.users.ports.user_service_port import UserServicePort
from src.users.user_service import UserService
from src.users.ports.user_repository_port import UserRepositoryPort
from src.users.user_repository import UserRepository
from dataBase.ports.database_port import Database_Port
from dataBase.adapters.sqlite_db import SqliteDb
from src.users.user_controller import UserController

# create the application object
app = Flask(__name__)

database = SqliteDb()
database.createTables()

# To create an instance of UserController and access its blueprint:
database: Database_Port = SqliteDb()
user_repo: UserRepositoryPort = UserRepository(database)
user_service: UserServicePort = UserService(user_repo)
user_controller = UserController(user_service)

app.register_blueprint(user_controller.controller, url_prefix="/users")
    
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
