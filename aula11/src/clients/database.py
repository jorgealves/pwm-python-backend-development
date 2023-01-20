from src.models.database import UserDatabaseModel
from src.models.api import UserAPIModel, MenuItemAPIModel
from src.models.database import MenuItemDatabaseModel, engine
from dataclasses import asdict
from sqlalchemy.orm import Session
from sqlalchemy import select, delete


def create_new_user(user_api_model: UserAPIModel):
    with Session(engine) as session:
        new_user = UserDatabaseModel(**user_api_model.dict())
        session.add(new_user)
        session.commit()


def get_username(username: str) -> UserDatabaseModel:
    with Session(engine) as session:
        query = select(UserDatabaseModel).where(
            UserDatabaseModel.username == username)
        result = session.scalars(query).one()
    if not result:
        raise Exception("username does not exist")
    return result


def create_new_menu_item(menu_item_api_model: MenuItemAPIModel):
    with Session(engine) as db:
        new_item = MenuItemDatabaseModel(**menu_item_api_model.dict())
        db.add(new_item)
        db.commit()


def get_all_menu_items():
    with Session(engine) as db:
        query = select(MenuItemDatabaseModel)
        result = db.scalars(query).all()
    return list(result)


def delete_menu_item(menu_item_name: str):
    with Session(engine) as db:
        statement = delete(MenuItemDatabaseModel).where(
            MenuItemDatabaseModel.name == menu_item_name)
        db.execute(statement)
