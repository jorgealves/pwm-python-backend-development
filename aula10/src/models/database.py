from dataclasses import dataclass


@dataclass()
class UserDatabaseModel:
    username: str
    password: str


@dataclass
class MenuItemDatabaseModel:
    name: str
    price: float
    description: str | None
