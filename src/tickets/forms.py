# TODO : I'm not familiar with floppyforms. So I'm using regular Django
#        forms and we need to convert them.

from django import forms

from .models import Ticket, TicketComment

class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
