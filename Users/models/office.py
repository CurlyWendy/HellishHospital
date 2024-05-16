from django.db import models

class Office(models.Model):
    number = models.PositiveIntegerField(not_null=True)
    floor = models.PositiveIntegerField(not_null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"Название кабинета: {self.name}"