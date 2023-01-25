from pydantic import BaseModel, validator
import string
from src.utils.encrypt import encrypt_password
from src.utils.validation import validate_username, validate_menu_item_name

class UserAPIModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validation(cls, value):
        return validate_username(value=value)

    @validator('password')
    def password_not_empty(cls, value):
        if not value:
            raise ValueError('password must not be empty')
        if set(value).difference(set(string.ascii_letters+string.digits+string.punctuation)):
            raise ValueError(
                "password should contain at least one uppercased character, one digit, and one punctuation character.")
        if 8 < len(value):
            raise ValueError("password must have at least 8 characters.")

        return encrypt_password(value)


class MenuItemAPIModel(BaseModel):

    name: str
    price: float
    description: str | None

    @validator("name")
    def validate_name(cls, value):
        return validate_menu_item_name(value=value)
        
    @validator("price")
    def validate_price(cls, value):
        if value < 0:
            raise ValueError("price should not be negative")
        return value


class CreateOrderAPIModel(BaseModel):
    
    username: str
    menu_item_name: str

    @validator("username")
    def validate_user(cls, value):
        return validate_username(value=value)

    @validator("menu_item_name")
    def validate_menu_item(cls, value):
        return validate_menu_item_name(value=value)
