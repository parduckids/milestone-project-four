from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name', 'date', 'start_time', 'end_time', 'city', 'address',
            'genre', 'organiser', 'event_description', 'artists', 'music', 'event_image', 'featured', 'ticket_price', "max_tickets"
        ]