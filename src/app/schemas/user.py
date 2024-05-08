from pydantic import BaseModel
import uuid


class UserSignUp(BaseModel):
    email: str
    password: str
    username: str
    full_name: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserSignUpResponse(BaseModel):
    uuid: uuid.UUID
    email: str
    username: str
    full_name: str

    class Config:
        from_attributes = True


class Conversation(BaseModel):
    uuid: uuid.UUID

    class Config:
        from_attributes = True


class UserGet(BaseModel):
    uuid: uuid.UUID
    email: str
    username: str
    full_name: str
    score: int
    favorite_conversations: list

    class Config:
        from_attributes = True


class ScoreboardGet(BaseModel):
    uuid: uuid.UUID
    full_name: str | None
    score: int

    class Config:
        from_attributes = True
