from django.db import models
from django.utils.text import slugify

class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name="Oda Adı")
    # Utilisation de blank=True pour éviter les erreurs lors de la création manuelle
    slug = models.SlugField(unique=True, blank=True, null=True)
    capacity = models.PositiveIntegerField(verbose_name="Kapasite")
    location = models.CharField(max_length=200, verbose_name="Konum", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi?")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name