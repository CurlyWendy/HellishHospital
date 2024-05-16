from django.db import models

class Schedule(models.Model):
    day_of_week = models.CharField(max_length=15)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"В {self.day_of_week}"