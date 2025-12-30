from django.db import models
from django.conf import settings
from rooms.models import Room

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Beklemede'),
        ('confirmed', 'Onaylandı'),
        ('canceled', 'İptal Edildi'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Kullanıcı")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Oda")
    date = models.DateField(verbose_name="Tarih")
    start_time = models.TimeField(verbose_name="Başlangıç Saati")
    end_time = models.TimeField(verbose_name="Bitiş Saati")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Durum")

    class Meta:
        verbose_name = "Rezervasyon"
        verbose_name_plural = "Rezervasyonlar"

    def __str__(self):
        return f"{self.user.username} - {self.room.name} ({self.date})"