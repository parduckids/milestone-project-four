# tickets/urls.py
from django.urls import path
from . import views

# set up ticket app urls
urlpatterns = [
    path('buy/<int:event_id>/', views.buy_ticket, name='buy_ticket'),
    path('mytickets/', views.mytickets, name='mytickets'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]
