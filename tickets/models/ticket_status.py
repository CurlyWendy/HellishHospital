from django.db import models

class TicketStatus(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name