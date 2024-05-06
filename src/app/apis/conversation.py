from asgiref.sync import sync_to_async
from fastapi import APIRouter, Depends
from app.crud.conversation import ConversationCrud
from app.depends.user import get_current_user
from app.schemas.conversation import ConversationGet, ConversationCreate, ConversationCreateResponse, FavoriteResponse

router = APIRouter(
    prefix="/conversation",
    tags=["conversation"],
)


@router.get("/")
async def get_conversations(current_user=Depends(get_current_user)) -> list[ConversationGet]:
    conversations = await sync_to_async(ConversationCrud.get_all)()
    return [ConversationGet.model_validate(conversation) for conversation in conversations]


@router.get("/{uuid}")
async def get_conversation(uuid: str, current_user=Depends(get_current_user)) -> ConversationGet:
    conversation = await ConversationCrud.get(uuid)
    return ConversationGet.model_validate(conversation)


@router.post("/")
async def create_conversation(
    conversation: ConversationCreate, current_user=Depends(get_current_user)
) -> ConversationCreateResponse:
    conversation = await ConversationCrud.create(conversation)
    return ConversationCreateResponse.model_validate(conversation)


@router.post("/{uuid}/favorite")
async def add_to_favorite(uuid: str, current_user=Depends(get_current_user)) -> FavoriteResponse:
    try:
        await ConversationCrud.add_to_favorite(uuid, current_user)
    except Exception as e:
        return FavoriteResponse(success=False, detail=str(e))
    return FavoriteResponse(success=True)


@router.delete("/{uuid}/favorite")
async def remove_from_favorite(uuid: str, current_user=Depends(get_current_user)) -> FavoriteResponse:
    try:
        await ConversationCrud.remove_from_favorite(uuid, current_user)
    except Exception as e:
        return FavoriteResponse(success=False, detail=str(e))
    return FavoriteResponse(success=True, detail="Removed from favorite")
