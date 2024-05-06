from fastapi import APIRouter
from starlette.websockets import WebSocket, WebSocketDisconnect

from app.common.websocket.room_manager import MeetingManager

manager = MeetingManager()

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)


@router.websocket("/ws/{room_id}")
async def connect_websocket(websocket: WebSocket, room_id: str):
    await manager.join(room_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.rooms[room_id].broadcast(data, websocket)
    except WebSocketDisconnect:
        manager.leave(room_id, websocket)
