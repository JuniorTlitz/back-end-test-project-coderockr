from pydantic import BaseModel


class CreateAccountDbModel(BaseModel):
    name: str
    email: str
    password: str
