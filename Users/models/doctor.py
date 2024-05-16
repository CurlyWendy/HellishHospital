from django.db import models
from django.contrib.auth.models import AbstractUser

class Doctor(AbstractUser):
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name='specialization'
    )

    def __str__(self):
        return f"Доктор {self.first_name} {self.last_name} - {self.specialization}"