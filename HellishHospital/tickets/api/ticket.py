from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from tickets.service.ticket_service import TicketService

class TicketApiView(APIView):
    ticket_service = TicketService
    permission_classes = (IsAuthenticated)
    


    def get(self, request, ticket_id=None):  # Добавляем параметр ticket_id по умолчанию со значением None
        user_id = request.user.id
        if ticket_id is not None:  # Если идентификатор тикета указан в URL-адресе
            ticket = self.ticket_service.get_ticket(ticket_id=ticket_id, user_id=user_id)
            if not ticket:
                return Response({"error": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(ticket)
        else:  # Если идентификатор тикета не указан в URL-адресе
            tickets = self.ticket_service.get_tickets_list(user_id=user_id)
            return Response(tickets)    

    def post(self, request):
        user_id = request.user.id
        ticket = self.ticket_service.create_ticket(user_id=user_id, **request.data)
        
        return Response(ticket)
    
    def delete(self, request):
        user_id = request.user.id
        ticket_deleted = self.ticket_service.delete_ticket(user_id=user_id, **request.data)
        
        if not ticket_deleted:
            return Response(ticket_deleted, status=400)

        return Response(ticket_deleted)