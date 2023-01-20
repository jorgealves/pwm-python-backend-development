from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Column, String, Float
from sqlalchemy import create_engine
# Creates connector to the database
engine = create_engine("sqlite://")

BaseDatabaseModel = declarative_base()

# Models Definition


class UserDatabaseModel(BaseDatabaseModel):
    __tablename__ = "users"

    username = Column(String, primary_key=True)
    password = Column(String)


class MenuItemDatabaseModel(BaseDatabaseModel):
    __tablename__ = "menu_items"

    name = Column(String, primary_key=True)
    price = Column(Float)
    description = Column(String, nullable=True)


# create all tables in database
BaseDatabaseModel.metadata.create_all(engine)
