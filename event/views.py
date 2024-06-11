from django.shortcuts import render

# Create your views here.

def index (request):
    """ A view to return the index page """
    return render(request, 'event/index.html')

def events (request):
    """ A view to return the events page """
    return render(request, 'event/events.html')