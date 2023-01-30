from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.models.api import UserAPI, ApiToken
from src.controllers import register, login


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
def authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    new_token: ApiToken = login.authenticate_user(
        username=form_data.username, password=form_data.password)
    if not new_token:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Login not valid")
    return new_token
