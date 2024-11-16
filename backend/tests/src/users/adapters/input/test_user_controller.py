import pytest
import app

# from src.users.adapters.input.user_controller import UserController

# class TestUserController:

#     #RUNS BEFORRE EACH TEST METHOD
#     def setup_method(self, method):
#         self.users_list = [
#             {
#                 "email":"vc@email.com",
#                 "name":"nmddd",
#                 "age": 30,
#                 "password":"12345678"
#             },
#             {
#                 "email":"eu@email.com",
#                 "name":"nmddd",
#                 "age": 30,
#                 "password":"12345678"
#             }
#         ]

#     def teardown_method(self, method):
#         print("Tear down {method}")

#     def test_create(self, )

def test_app(app):
    assert app.name == 'app'