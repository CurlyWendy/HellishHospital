from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

from .specialization import Specialization

class Doctor(AbstractUser):
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name='specialization'
    )

    groups = models.ManyToManyField(Group, related_name='patient_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='patient_permissions')

    def __str__(self):
        return f"Доктор {self.first_name} {self.last_name} - {self.specialization}"