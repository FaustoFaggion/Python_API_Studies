from flask import Flask, request, jsonify
from src.users.user_controller import controller
from dataBase.sqlite_db import SqliteDb

# create the application object
app = Flask(__name__)

SqliteDb.createTables()

app.register_blueprint(controller, url_prefix="/users")
    
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
