from flask import Flask, request, jsonify
from src.users.adapters.output.dto_validation_json_schema import ValidateDtoListJsonSchema
# from src.users.adapters.output.dto_validation_pydantic import ValidateDtoPydantic
from src.users.ports.input.user_service_port import UserServicePort
from src.users.adapters.output.user_repository_postgres import UserRepositoryPostgres
from src.users.adapters.output.user_repository_sqlite import UserRepositorySqlite
from src.users.ports.output.validate_dto_list_port import ValidateDtoListPort
from src.users.useCases.user_service import UserService
from src.users.ports.output.user_repository_port import UserRepositoryPort
from dataBase.ports.database_port import Database_Port
from dataBase.adapters.sqlite_db import SqliteDb
from dataBase.adapters.postgres_db import PostgresDb
from src.users.adapters.input.user_controller import UserController
from dataBase.adapters.schema import tables_schema
# create the application object

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

print("app name: ")
database = PostgresDb()
database.createTables(tables_schema)

# To create an instance of UserController and access its blueprint:
dto_validation: ValidateDtoListPort = ValidateDtoListJsonSchema()
user_repo: UserRepositoryPort = UserRepositoryPostgres(database)
user_service: UserServicePort = UserService(user_repo, dto_validation)
user_controller = UserController(user_service)

app.register_blueprint(user_controller.controller, url_prefix="/users")
    
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
