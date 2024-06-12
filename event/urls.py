
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('events', views.events, name='events'),
    path('create-event', views.create_event, name='create')
]
