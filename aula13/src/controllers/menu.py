from src.models.api import MenuItemAPIModel
from src.clients import database


def create_new_menu_item(menu_item_api_model: MenuItemAPIModel):
    database.create_new_menu_item(menu_item_api_model)


def get_all():
    return database.get_all_menu_items()

def delete_menu_item(menu_item_name:str):
    database.delete_menu_item(menu_item_name=menu_item_name)
