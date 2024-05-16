from django.db import models
from schedule import Schedule
from doctor import Doctor

class doctorsSchedule(model.Model):
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        related_name='schedule'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='doctor'
    )

    def __str__(self):
        return f"{self.doctor.name} принимает в {self.schedule.day_of_week} с {self.schedule.date_start} до {self.schedule.date_finish}"
