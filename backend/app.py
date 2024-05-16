# import the Flask class from the flask module
from flask import Flask
from src.users.user_controller import controller

# create the application object
app = Flask(__name__)

app.register_blueprint(controller, url_prefix="/users")

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
