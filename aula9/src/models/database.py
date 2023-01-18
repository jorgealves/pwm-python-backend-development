from dataclasses import dataclass


@dataclass()
class UserDatabaseModel:
    username: str
    password: str
