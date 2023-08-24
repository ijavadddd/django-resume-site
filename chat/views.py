from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import TicketForm


class TicketView(FormView):
    template_name = 'chat/contact_me_include.html'
    form_class = TicketForm
    success_url = '/'

    def form_valid(self, form):
        print('salam')
        form.save()
        return super().form_valid(form)
