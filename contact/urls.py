from django.urls import path
from . import views
# set up url for the about page where the contact form is located
urlpatterns = [
    path('about/', views.about, name='about'),
]
