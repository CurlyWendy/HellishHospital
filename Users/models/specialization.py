from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"Специализация доктора {self.name}"
