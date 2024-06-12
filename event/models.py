from django.db import models

# Event Model

from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

# todo: set up default values for genre city, organiser
class Event(models.Model):
    # Fields
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    organiser = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_description = models.TextField()
    artists = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    music = models.URLField(max_length=200, blank=True, null=True)
    event_image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.event_name



    # if the event date is today, return today instead of the date, same with 'tomorrow'
    @property
    def formatted_date(self):
        # get today's date in the correct timezone
        today = timezone.localdate()
        # get the event's date
        event_date = self.date

        # if the event is today, return "Today"
        if event_date == today:
            return "Today"
        # if the event is tomorrow, return "Tomorrow"
        elif event_date == today + timezone.timedelta(days=1):
            return "Tomorrow"
        # if the event is in the same week as today, return the day name 
        elif event_date.isocalendar()[1] == today.isocalendar()[1]:
            return event_date.strftime('%A')
        # if the event is in the same year as today, return the month and day
        elif event_date.year == today.year:
            return event_date.strftime('%B %d')
        # if the event is in a different year, return the full date 
        else:
            return event_date.strftime('%B %d, %Y')
