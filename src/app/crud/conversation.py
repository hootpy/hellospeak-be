from asgiref.sync import sync_to_async

from app.models import User
from app.models.conversation import Conversation
from app.schemas.conversation import ConversationCreate


class ConversationCrud:
    @classmethod
    def get_all(cls) -> list[Conversation]:
        return list(Conversation.objects.filter())

    @classmethod
    async def get(cls, uuid: str) -> Conversation:
        return await Conversation.objects.filter(uuid=uuid).afirst()

    @classmethod
    async def create(cls, conversation: ConversationCreate) -> Conversation:
        return await Conversation.objects.acreate(**conversation.dict())

    @classmethod
    async def add_to_favorite(cls, uuid_: str, user: User) -> None:
        conversation = await cls.get(uuid_)
        await sync_to_async(user.favorite_conversations.add)(conversation)
        await user.asave()

    @classmethod
    async def remove_from_favorite(cls, uuid_: str, user: User) -> None:
        conversation = await cls.get(uuid_)
        await sync_to_async(user.favorite_conversations.remove)(conversation)
        await user.asave()
