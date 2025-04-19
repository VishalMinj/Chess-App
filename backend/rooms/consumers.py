import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CreateRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message":"hello"}))