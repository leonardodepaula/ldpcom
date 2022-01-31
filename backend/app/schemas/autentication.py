from typing import Optional

from pydantic import BaseModel

from .user import User


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None

class Login(Token):
    user: User