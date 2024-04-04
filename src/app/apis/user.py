from fastapi import APIRouter, Depends

from app.depends.user import get_current_user
from app.schemas.user import UserGet

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/")
async def get_user(current_user=Depends(get_current_user)) -> UserGet:
    return UserGet.model_validate(current_user)
