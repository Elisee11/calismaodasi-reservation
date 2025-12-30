from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Ajout du champ numéro d'étudiant demandé
    student_id = models.CharField(max_length=20, blank=True, null=True, verbose_name="Öğrenci Numarası")

    def __str__(self):
        return f"{self.username} ({self.student_id if self.student_id else 'No ID'})"


