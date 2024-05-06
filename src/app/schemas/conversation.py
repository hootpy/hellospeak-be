from pydantic import BaseModel
import uuid


class ConversationGet(BaseModel):
    uuid: uuid.UUID
    title: str
    messages: list
    topic: list[str]
    level: str

    class Config:
        from_attributes = True


class Message(BaseModel):
    speaker: str
    gender: str
    text: str


class ConversationCreate(BaseModel):
    title: str
    messages: list[Message]
    topic: list[str]
    level: str

    class Config:
        from_attributes = True


class ConversationCreateResponse(BaseModel):
    uuid: uuid.UUID
    title: str

    class Config:
        from_attributes = True


class FavoriteResponse(BaseModel):
    success: bool
    detail: str = "Added to favorite"
