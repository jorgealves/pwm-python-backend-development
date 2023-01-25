from src.models.api import UserAPIModel
from src.clients import database
from src.models.database import UserDatabaseModel
from src.utils.encrypt import encrypt_password
from datetime import datetime, timedelta
from src.config import Settings
from jose import JWTError, jwt


def validate_user_and_password(user_api_model: UserAPIModel) -> bool:
    user_database_data: UserDatabaseModel = database.get_username()
    return (user_database_data.username == user_api_model.username) and (user_database_data.password == user_api_model.password)


def authenticate_user(username: str, password: str):
    user = database.get_username(username)
    if not user:
        raise Exception("Incorrect username or password")
    hashed_password = encrypt_password(password)
    if not hashed_password == user.password:
        raise Exception("Incorrect username or password")
    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=Settings().ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Settings(
    ).SECRET_KEY, algorithm=Settings().ALGORITHM)
    return encoded_jwt


def get_token(form_data):
    user = authenticate_user(username=form_data.username,
                             password=form_data.password)
    token = create_access_token(data=dict(username=user.username))

    return {"access_token": token, "token_type": "bearer"}
