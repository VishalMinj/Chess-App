from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User= get_user_model()


class Room(models.Model):

    class RoomStates(models.TextChoices):
        WAITING = "waiting", "Waiting"
        PLAYING = "playing", "Playing"
        FINISHED = "finished", "Finished"

    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2', null=True)
    room_status = models.CharField(max_length=20, choices=RoomStates, default="waiting")

    
class Move(models.Model):
    by=models.ForeignKey(User, on_delete=models.CASCADE)
    off=models.CharField(max_length=2)
    to=models.CharField(max_length=2)
    room=models.ForeignKey(Room, on_delete=models.CASCADE,related_name='moves')

    def __str__(self):
        return f"from {self.off} to {self.to}"
    
