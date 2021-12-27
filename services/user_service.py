from typing import Optional

from model.User import User


def user_count():
    return 3


def create_account(name: str, email:str, password:str)->User:
    return User(name, email, "todopasswordhash")


def login_user(email:str, password:str)->Optional[User]:
    if password == 'todopasswordhash':
        return User('test_user', email, "todopasswordhash")
    return None
