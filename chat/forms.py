from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Name *"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':"Email *"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Phone"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Message"}))

    class Meta:
        model = Ticket
        exclude = ['created_at']
