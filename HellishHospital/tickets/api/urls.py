from django.contrib import admin
from django.urls import path
from .ticket import TicketApiView

urlpatterns = [
    path('/tickets', TicketApiView.as_view(),),
    path('/tickets/<int:ticket_id>', TicketApiView.as_view(),),
]
