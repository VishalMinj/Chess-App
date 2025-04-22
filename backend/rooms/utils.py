from django.db import models

class RoomStates(models.TextChoices):
    WAITING = "waiting", "Waiting"
    PLAYING = "playing", "Playing"
    FINISHED = "finished", "Finished"
