from django.db import models

class Benefits(models.Model):
    name = CharField(max_length=200)

    def __str__(self):
        return f"Пациент - {self.name}"
