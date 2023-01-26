from pydantic import BaseModel, validator
import string

from src.utils.validation import EMAIL_REGEX


class UserAPI(BaseModel):
    name: str
    email: str
    handle: str
    password: str
    bio: str | None

    @validator("name")
    def validate_name(cls, value):
        if not value:
            raise ValueError("name should not be empty")
        if set(value).difference(set(string.ascii_letters+string.whitespace)):
            raise ValueError(
                "name should only contains letters and white spaces")
        if len(value) < 4:
            raise ValueError("name should have more than 4 characters.")
        return value

    @validator("email")
    def validate_email(cls, value):
        if not EMAIL_REGEX.fullmatch(value):
            raise ValueError("email provided is not compliant")
        return value
