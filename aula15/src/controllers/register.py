
from src.models import api, database
from src.clients import database as db_client


def create_user(user: api.UserAPI):
    user_db = database.UserDB(**user.dict())
    db_client.insert(user_db)
