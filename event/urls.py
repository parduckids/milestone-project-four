
from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('events', views.events, name='events'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('create-event', views.create_event, name='create'),
    path('manage-events', views.manage_events, name='manage'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
