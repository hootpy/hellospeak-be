from fastapi.websockets import WebSocket


class SignalManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    @property
    def is_empty(self):
        return len(self.active_connections) == 0

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    @staticmethod
    async def send_personal_message(message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: dict, websocket: WebSocket):
        for connection in self.active_connections:
            if connection != websocket:
                await connection.send_json(message)
