from fastapi import APIRouter, status

from src.models.api import UserAPI
from src.controllers import register


router = APIRouter(tags=["Main"])


@router.post("register", status_code=status.HTTP_201_CREATED)
def create_user(user: UserAPI):
    """
    Creates a new user by fiilling the following fields:
    - nome
    - handle
    - email
    - password
    - BIO
    """
    register.create_user(user=user)
    


@router.post("login", status_code=status.HTTP_202_ACCEPTED)
def login():
    pass
