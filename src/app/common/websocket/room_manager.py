from starlette.websockets import WebSocket

from app.common.websocket.signal_manager import SignalManager


class MeetingManager:
    def __init__(self) -> None:
        self.rooms: dict[str, SignalManager] = {}

    async def join(self, id_: str, websocket: WebSocket):
        if id_ in self.rooms:
            await self.rooms[id_].connect(websocket)
        else:
            self.rooms[id_] = SignalManager()
            await self.rooms[id_].connect(websocket)
        await self.rooms[id_].broadcast({"type": "USER_JOIN"}, websocket)

    def leave(self, id_: str, websocket: WebSocket):
        self.rooms[id_].disconnect(websocket)
        if self.rooms[id_].is_empty:
            del self.rooms[id_]
