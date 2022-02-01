from typing import Optional
from pydantic import BaseModel
from . import seller

class Auth(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    strtoken_type: str

class TokenData(BaseModel):
    username: Optional[str] = None