from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.config import Settings
from src.models.database import Base

engine = create_engine(Settings().database_connection)


Base.metadata.create_all(engine)


def insert(models_to_add: list):
    with Session(engine) as db:
        db.add_all(models_to_add)
        db.commit()
