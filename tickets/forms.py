# forms.py
from django import forms
from .models import Ticket

class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})