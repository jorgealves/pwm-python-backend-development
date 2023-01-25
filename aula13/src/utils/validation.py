import string

def validate_username(value: str):
    if not value:
        raise ValueError('username must not be empty')
    if set(value).difference(set(string.ascii_letters+string.digits)):
        raise ValueError(
            "username should only contain alfanumeric characters.")
    if 4 > len(value) > 20:  # if value in range(4,20)
        raise ValueError("username must be between 4 and 20 characters")

    return value

def validate_menu_item_name(value:str):
    if not value:
        raise ValueError("name field is required")
    if len(value) > 30:
        raise ValueError("name should not have more than 30 characters.")
    return value