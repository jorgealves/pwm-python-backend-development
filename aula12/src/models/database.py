from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import String, Column, String, Float, Integer, ForeignKey
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

    orders = relationship("OrdersDatabaseModel")


class MenuItemDatabaseModel(BaseDatabaseModel):
    __tablename__ = "menu_items"

    name = Column(String(50), primary_key=True)
    price = Column(Float)
    description = Column(String(300), nullable=True)

    bought_on = relationship("OrderDatabaseModel")

class OrderDatabaseModel(BaseDatabaseModel):
    __tablename__="orders"

    id=Column(Integer, primary_key=True)
    username = Column(String(100), ForeignKey("UserDatabaseModel.username"))
    menu_item_name = Column(String(100), ForeignKey("MenuItemDatabaseModel.name"))



# create all tables in database
BaseDatabaseModel.metadata.create_all(engine)
