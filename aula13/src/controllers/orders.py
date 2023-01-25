from src.models.api import CreateOrderAPIModel
from src.clients import database

def create_order(create_order_api_model: CreateOrderAPIModel):
    assert create_order_api_model

    valid_username = database.get_username(username=create_order_api_model.username)
    valid_menu_item_name = database.get_menu_item(menu_item_name=create_order_api_model.menu_item_name)

    assert valid_username
    assert valid_menu_item_name

    database.create_order(username=valid_username, menu_item_name=valid_menu_item_name)
    
