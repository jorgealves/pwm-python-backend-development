from pydantic import BaseSettings


class Settings(BaseSettings):

    database_connection: str = "mysql://root:admin@db/social_network_db"
    SECRET_KEY = "super_secret_key_for_jwt"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 2
