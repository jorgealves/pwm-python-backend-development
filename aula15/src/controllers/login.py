from src.models.api import ApiToken
from src.models.database import UserDB
from src.utils.security import get_password_hash, create_access_token


def authenticate_user(username: str, password: str) -> ApiToken:
    user: UserDB = database.get(UserDB, lambda x: username ==
                                x.username and get_password_hash(password=password))

    if not user:
        raise ValueError("could not get username")

    access_token: ApiToken = create_access_token(
        data={"username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
