from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name', 'genre', 'city', 'address', 
            'organiser', 'date', 'start_time', 'end_time', 
            'event_description', 'artists', 'music'
        ]