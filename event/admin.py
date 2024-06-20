from django.contrib import admin
from .models import Event
# add Event model to the admin portal
admin.site.register(Event)
