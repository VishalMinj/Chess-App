from django.urls import path
from .consumers import CreateRoomConsumer

websocket_urlpatterns = [
    path("rooms/create-room/",CreateRoomConsumer.as_asgi()),
]
