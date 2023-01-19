from src.models.database import UserDatabaseModel
from src.models.api import UserAPIModel, MenuItemAPIModel
from src.models.database import MenuItemDatabaseModel
from dataclasses import asdict

users_table = dict()
menu_item_table = dict()


def create_new_user(user_api_model: UserAPIModel):
    if user_api_model.username in users_table.keys():
        raise Exception("Username already taken")
    users_table[user_api_model.username] = user_api_model.password


def get_username(username: str) -> UserDatabaseModel:
    database_password = users_table.get(username)
    if not database_password:
        raise Exception("username does not exist")
    return UserDatabaseModel(username=username, password=database_password)


def create_new_menu_item(menu_item_api_model: MenuItemAPIModel):
    if menu_item_api_model.name in menu_item_table.keys():
        raise Exception("Menu Item already exists")
    menu_item_table[menu_item_api_model.name] = MenuItemDatabaseModel(
        **menu_item_api_model.dict()
    )  # MenuItemDatabaseModel(name=menu_item_api_model.name, price=menu_item_api_model.price, description=menu_item_api_model.description)


def get_all_menu_items():
    data = list(menu_item_table.values())
    return [
        MenuItemAPIModel(**asdict(x))
        for x in data
    ]
    # result = []
    # for x in data:
    #     result.append(MenuItemAPIModel(**x.dict()))


def delete_menu_item(menu_item_name: str):
    if menu_item_name not in menu_item_table.keys():
        raise Exception("Menu Item name does not exist")
    menu_item_table.pop(menu_item_name)
    # del menu_item_table[menu_item_name]
