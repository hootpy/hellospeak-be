from pydantic import BaseModel
import uuid


class UserSignUp(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserSignUpResponse(BaseModel):
    uuid: uuid.UUID
    email: str

    class Config:
        from_attributes = True


class UserGet(BaseModel):
    uuid: uuid.UUID
    email: str

    class Config:
        from_attributes = True
