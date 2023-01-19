from src.models.api import UserAPIModel
from src.clients import database
from src.models.database import UserDatabaseModel


def validate_user_and_password(user_api_model: UserAPIModel) -> bool:
    user_database_data: UserDatabaseModel = database.get_username()
    return (
        user_database_data.username == user_api_model.username
    ) and (
        user_database_data.password == user_api_model.password
    )
