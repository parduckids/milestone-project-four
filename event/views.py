from django.shortcuts import render, redirect
from .forms import EventForm 

# Create your views here.

def index (request):
    """ A view to return the index page """
    return render(request, 'event/index.html')

def events (request):
    """ A view to return the events page """
    return render(request, 'event/events.html')

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events')
        else:
            print(form.errors)  # Print form errors if form is not valid
    else:
        form = EventForm()
    return render(request, 'event/create_event.html', {'form': form})
