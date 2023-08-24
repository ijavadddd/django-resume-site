from django.urls import path
from .views import TicketView


app_name = 'chat'
urlpatterns = [
    path('ticket/', TicketView.as_view(), name='ticket')
]
