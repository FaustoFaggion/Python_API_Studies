from flask import Flask, request, jsonify
from dataBase.sqlite_db import SqliteDb
from src.users.user_controller import controller_blueprint

# create the application object
app = Flask(__name__)

SqliteDb.createTables()

app.register_blueprint(controller_blueprint, url_prefix="/users")
    
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
