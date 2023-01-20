from pydantic import BaseModel, validator
import string
from src.utils.encrypt import encrypt_password


class UserAPIModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validation(cls, value):
        if not value:
            raise ValueError('username must not be empty')
        if set(value).difference(set(string.ascii_letters+string.digits)):
            raise ValueError(
                "username should only contain alfanumeric characters.")
        if 4 > value > 20:  # if value in range(4,20)
            raise ValueError("username must be between 4 and 20 characters")

        return value

    @validator('password')
    def password_not_empty(cls, value):
        if not value:
            raise ValueError('password must not be empty')
        if not set(value).difference(set(string.ascii_letters+string.digits+string.punctuation)):
            raise ValueError(
                "password should contain at least one uppercased character, one digit, and one punctuation character.")
        if 8 < value:
            raise ValueError("password must have at least 8 characters.")

        return encrypt_password(value)


class MenuItemAPIModel(BaseModel):

    name: str
    price: float
    description: str | None

    @validator("name")
    def validate_name(cls, value):
        if not value:
            raise ValueError("name field is required")
        if len(value) > 30:
            raise ValueError("name should not have more than 30 characters.")
        return value

    @validator("price")
    def validate_price(cls, value):
        if value < 0:
            raise ValueError("price should not be negative")
        return value
