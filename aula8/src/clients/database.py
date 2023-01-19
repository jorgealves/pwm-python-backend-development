from src.models.database import UserDatabaseModel

user = "pwm"
passwd = "2123"


def get_username() -> UserDatabaseModel:
    return UserDatabaseModel(username=user, password=passwd)
