from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class Patient(AbstractUser):
    benefits = models.TextField()
    groups = models.ManyToManyField(Group, related_name='doctor_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='doctor_permissions')

    def __str__(self):
        return self.full_name