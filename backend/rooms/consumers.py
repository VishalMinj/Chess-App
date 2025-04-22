import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async as db_async
from .models import Room


class CreateRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = f'{self.scope["user"].id}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        self.game_room = await db_async(Room.objects.create)(player1=self.scope["user"])
        await self.send(text_data=json.dumps({"room_code": f"{self.room_group_name}"}))
