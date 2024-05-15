from flask import Blueprint

user_controller = Blueprint("user_controller", __name__, static_folder="static", template_folder="template")

# use decorators to link the function to a url
@user_controller.route('/')
def home():
    return "Hello, World!"  # return a string

# @app.route('/welcome')
# def welcome():
#     return render_template('welcome.html')  # render a template
