from datetime import date, timezone

from models.ticket import Ticket
from models.ticket_status import TicketStatus

class TicketService:

    @staticmethod
    def get_tickets_list(user_id: int, **filters: dict):

        if filter is None:
            return Ticket.objects.filter()

        return Ticket.objects.filter(patient__id=user_id, **filter)

    @staticmethod
    def create_ticket(user_id: int, doctor_id: int, date_of_receipt: date):
        ticket_status = 1  # статус заявки создана 
        ticket = Ticket.objects.create(patient=doctor_id, doctor=doctor_id, timestamp=timezone.now(), status=ticket_status, date_of_receipt=date_of_receipt)
        return ticket

    @staticmethod
    def get_ticket_by_id(ticket_id: int):
        try:
            return Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return None

    @staticmethod
    def delete_ticket(ticket_id: int):
        ticket = TicketService.get_ticket_by_id(ticket_id)
        if ticket:
            ticket.delete()
            return True
        return False