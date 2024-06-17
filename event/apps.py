from django.apps import AppConfig

# set default pk field type
class EventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event'
