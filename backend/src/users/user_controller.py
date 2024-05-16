from flask import Blueprint
from src.users.user_service import UserService

user_controller = Blueprint("user_controller", __name__, static_folder="static", template_folder="template")

# use decorators to link the function to a url
@user_controller.route('/create')
def create():
    return UserService.create()

