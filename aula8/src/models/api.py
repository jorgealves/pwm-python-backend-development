from pydantic import BaseModel, validator


class UserAPIModel(BaseModel):
    username: str
    password: str

    @validator("username")
    def username_not_empty(cls, value):
        if not value:
            raise ValueError("username must not be empty")
        return value

    @validator("password")
    def password_not_empty(cls, value):
        if not value:
            raise ValueError("password must not be empty")
        return value