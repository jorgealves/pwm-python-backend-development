from pydantic import BaseSettings


class Settings(BaseSettings):

    database_connection: str = "mysql://root:admin@db/el_chapo_food_db"
