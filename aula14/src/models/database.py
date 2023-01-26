from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Text

Base = declarative_base()


class UserDB(Base):
    __tablename__ = "users"

    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(300), nullable=True)
    handle = Column(String(30), primary_key=True)
    bio = Column(Text())
