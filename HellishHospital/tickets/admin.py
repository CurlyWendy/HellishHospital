from django.contrib import admin
from tickets.models.ticket import Ticket
from tickets.models.ticket_status import TicketStatus
# Register your models here.
admin.site.register(Ticket)
admin.site.register(TicketStatus)