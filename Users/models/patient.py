from django.db import models
from django.contrib.auth.models import AbstractUser

class Patient(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    benefits = models.TextField()

    def __str__(self):
        return self.full_name