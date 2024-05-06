from fastapi import APIRouter
from app.apis.auth import router as auth_router
from app.apis.user import router as user_router
from app.apis.chat import router as chat_router
from app.apis.conversation import router as conversation_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(user_router)
router.include_router(chat_router)
router.include_router(conversation_router)
