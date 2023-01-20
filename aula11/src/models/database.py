from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Column, String, Float
from sqlalchemy import create_engine
from src.config import Settings
# Creates connector to the database
engine = create_engine(Settings().database_connection)

BaseDatabaseModel = declarative_base()

# Models Definition


class UserDatabaseModel(BaseDatabaseModel):
    __tablename__ = "users"

    username = Column(String(50), primary_key=True)
    password = Column(String(100))


class MenuItemDatabaseModel(BaseDatabaseModel):
    __tablename__ = "menu_items"

    name = Column(String(50), primary_key=True)
    price = Column(Float)
    description = Column(String(300), nullable=True)


# create all tables in database
BaseDatabaseModel.metadata.create_all(engine)
