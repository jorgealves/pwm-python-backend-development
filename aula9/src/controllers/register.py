from src.clients import database
from src.models.api import UserAPIModel

def create_new_user(user_api_model: UserApiModel):
    database.create_new_user(user_api_model)