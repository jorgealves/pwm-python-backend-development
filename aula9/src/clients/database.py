from src.models.database import UserDatabaseModel
from src.models.api import UserAPIModel

users_table = dict()


def create_new_user(user_api_model: UserAPIModel):
    if user_api_model.username in users_table.keys():
        raise Exception("Username already taken")
    users_table[user_api_model.username] = user_api_model.password


def get_username(username: str) -> UserDatabaseModel:
    database_password = users_table.get(username)
    if not database_password:
        raise Exception("username does not exist")
    return UserDatabaseModel(username=username, password=database_password)
