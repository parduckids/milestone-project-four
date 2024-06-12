from django.db import models

# Event Model

from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

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
    music = models.URLField(max_length=200, blank=True, null=True)  # Links to music platforms

    def __str__(self):
        return self.event_name


    @property
    # If the event date is today, return today instead of the date, same with 'tomorrow'
    def formatted_date(self):
        today = timezone.now().date()
        if self.date == today:
            return "Today"
        elif self.date == today + timezone.timedelta(days=1):
            return "Tomorrow"
        else:
            return self.date.strftime('%Y-%m-%d')
