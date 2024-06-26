from asgiref.sync import sync_to_async
from fastapi import APIRouter, Depends

from app.crud.user import UserCrud
from app.depends.user import get_current_user
from app.schemas.user import UserGet, ScoreboardGet

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/")
async def get_user(current_user=Depends(get_current_user)) -> UserGet:
    favorite_conversations_query = current_user.favorite_conversations.values_list("uuid", flat=True)
    favorite_conversations = await sync_to_async(list)(favorite_conversations_query)
    return UserGet(
        uuid=current_user.uuid,
        email=current_user.email,
        username=current_user.username,
        full_name=current_user.full_name,
        score=current_user.score,
        favorite_conversations=favorite_conversations,
    )


@router.post("/score")
async def update_score(score: int, current_user=Depends(get_current_user)):
    current_user.score += score
    await current_user.asave()
    return {
        "success": True,
    }


@router.get("/scoreboard")
async def get_scoreboard(page: int = 1, page_size: int = 10):
    scoreboard = await sync_to_async(UserCrud.get_scoreboard)(page, page_size)
    return [ScoreboardGet.model_validate(user) for user in scoreboard]
