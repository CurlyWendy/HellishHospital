from django.db import models
from django.contrib.auth.models import AbstractUser

class Patient(AbstractUser):
    user = models(AbstractUser, on_delete=models.CASCADE)
    benefits = models.ForeignKey(
        Benefits,
        on_delete=models.CASCADE,
        related_name='benefits'
    )
    age = models.PositiveIntegerField(default=NULL)
    snils = models.CharField(max_length=30)
    policy_number = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name