from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm 
from .models import Event


def index (request):
    """ A view to return the index page """
    return render(request, 'event/index.html')

def events (request):
    """ A view to return the events page """
    events = Event.objects.all()
    return render(request, 'event/events.html', {'events': events})

def create_event(request):
    """ A view to return the create event page """
    # todo: only allow this to the admin user
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events')
        else:
            print(form.errors)  
    else:
        form = EventForm()
    return render(request, 'event/create_event.html', {'form': form})


def event_detail(request, event_id):
    """ A view to return the event detail pages """
    event = get_object_or_404(Event, event_id=event_id)
    artist_list = event.artists.split(',')
    context = {
        'event': event,
        'artist_list': artist_list,
    }
    return render(request, 'event/event_detail.html', context)

    
