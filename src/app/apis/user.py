from fastapi.routing import APIRouter
from pydantic.main import BaseModel
from asgiref.sync import sync_to_async
from app.models.car import Car


class CarSchema(BaseModel):
    name: str
    brand: str
    year: int


router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/")
async def create_user(user: CarSchema):
    return await sync_to_async(Car.objects.create)(**user.dict())
