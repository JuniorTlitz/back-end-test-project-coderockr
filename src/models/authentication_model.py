from pydantic import BaseModel


class AuthenticationModel(BaseModel):
    email: str
    password: str


class AuthenticationResponseModel(BaseModel):
    access_token: str
    name: str
