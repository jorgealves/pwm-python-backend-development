from fastapi import FastAPI, Response
from src.models.api import UserAPIModel
from src.controllers import login


api = FastAPI()


@api.post("/login")
async def login_endpoint(user_model: UserAPIModel, response: Response):
    if login.validate_user_and_password(user_api_model=user_model):
        return f"Welcome {user_model.username}"
    return f"Something went wrong to you {user_model.username}"
