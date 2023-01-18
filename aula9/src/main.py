from fastapi import FastAPI, Response
from src.models.api import UserAPIModel
from src.controllers import login

api = FastAPI()

@api.post("/register")
def create_new_user(user_api_model: UserAPIModel):
    

@api.post("/login")
async def login_endpoint(user_model: UserAPIModel, response: Response):
    if login.login.validade_user_and_password(user_api_model=user_model):
        return "Welcome {user_model.username}"
    return f"Someting went wrong to you {user_model.username}"
