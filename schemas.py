from typing import Optional

from pydantic import BaseModel

class new_users_schema(BaseModel):

    username: str
    password: str
    email: str

class post_schema(BaseModel):

    title: str
    content: str

# for response schema
class UserSchemaResponse(BaseModel):

    username: str
    email: str
    username: str

# Log in

class UserLogin(BaseModel):
    email: str
    password: str


# Recieve data request using token

class UserToken(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None