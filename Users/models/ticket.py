from django.db import models
from .doctor import Doctor
from .patient import Patient
from .ticket_status import TicketStatus

class Ticket(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f"Талон: #{self.id} - Пациент: {self.patient.user.username}, Доктор: {self.doctor.user.username}, Статус: {self.status.name}"