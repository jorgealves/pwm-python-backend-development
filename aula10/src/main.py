from fastapi import FastAPI, Response, status
from src.models.api import UserAPIModel
from src.controllers import login, register
from src.routes import menu

api = FastAPI()

routers = [
    menu.router
]

for router in routers:
    api.include_router(router)


@api.post("/register", status_code=status.HTTP_201_CREATED)
def create_new_user(user_api_model: UserAPIModel):
    register.create_new_user(user_api_model=user_api_model)


@api.post("/login")
async def login_endpoint(user_model: UserAPIModel, response: Response):
    if login.login.validade_user_and_password(user_api_model=user_model):
        return "Welcome {user_model.username}"
    return f"Someting went wrong to you {user_model.username}"
