from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from rooms.models import Room

# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.user} - {self.room} - {self.date} {self.start_time}-{self.end_time}"

