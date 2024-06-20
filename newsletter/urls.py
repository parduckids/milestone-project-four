from django.urls import path
from . import views

# set up url for when user subscribed
urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
]
