from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm 
from .models import Event

# todo: add actual events, show only free, the newest date ones
def index (request):
    """ A view to return the index page """
    return render(request, 'event/index.html')
# todo: filtering events 
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

# todo: filtering events 
def manage_events(request):
    """ A view to return the manage events page """
    events = Event.objects.all()
    return render(request, 'event/manage.html', {'events': events})

# todo: event data doesn't show on edit event page when normal layout is set, layout needs to be changed, image should be shown
def edit_event(request, event_id):
    """ A view to return the edit event page """
    event = get_object_or_404(Event, event_id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('manage')
    else:
        form = EventForm(instance=event)
    return render(request, 'event/edit_event.html', {'form': form})

# todo: event data doesn't show on delete event page
def delete_event(request, event_id):
    """ A view for deleting an event """
    event = get_object_or_404(Event, event_id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('manage')
    return render(request, 'event/delete_event.html', {'event': event})

# todo: set up tickets app
def event_detail(request, event_id):
    """ A view to return the event detail pages """
    event = get_object_or_404(Event, event_id=event_id)
    artist_list = event.artists.split(',')
    context = {
        'event': event,
        'artist_list': artist_list,
    }
    return render(request, 'event/event_detail.html', context)

    
