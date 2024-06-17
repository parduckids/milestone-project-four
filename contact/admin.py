from django.contrib import admin
from .models import ContactMessage
# add ContactMessage model to the admin portal
admin.site.register(ContactMessage)