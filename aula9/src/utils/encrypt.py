import hashlib

def encrypt_password(password_value: str):
    password_encoded = password_value.encode('utf-8')
    return hashlib.md5(password_encoded).hexdigest()