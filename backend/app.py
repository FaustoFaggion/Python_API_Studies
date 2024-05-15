# import the Flask class from the flask module
from flask import Flask
from src.users.user_controller import user_controller

# create the application object
app = Flask(__name__)

app.register_blueprint(user_controller, url_prefix="")


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
    import backend.src.users.user_controller as user_controller