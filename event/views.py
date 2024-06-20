from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from .models import Event
# import timezone to check if event is in the past
from django.utils import timezone
# import allauth decorator to check if admin is logged in, add it to all admin restricted views
from django.contrib.auth.decorators import user_passes_test
# import messages
from django.contrib import messages


# check if username is administrator
def is_administrator(user):
    """ A view to check if the user has admin rights """
    return user.is_authenticated and user.username == 'administrator'

# home page


def index(request):
    """ A view to return the index page with only featured events """
    featured_events = Event.objects.filter(featured=True)
    return render(request, 'event/index.html', {'events': featured_events})

# all events page


def events(request):
    """ A view to return the events page with filtering """
    # check if event is in the past, only return current or future ones
    events = Event.objects.filter(date__gte=timezone.now())

    # get filter parameters from the request
    genre = request.GET.get('event_type')
    date = request.GET.get('date')
    city = request.GET.get('event_city')

    # apply filters if parameters are provided
    if genre:
        events = events.filter(genre=genre)
    if date:
        events = events.filter(date=date)
    if city:
        events = events.filter(city=city)

    # render the template with the filtered events
    return render(request, 'event/events.html', {'events': events})

# create event page for the administrator


@user_passes_test(is_administrator)
def create_event(request):
    """ A view to return the create event page """
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New event uploaded successfully.')
            return redirect('manage')
        else:
            messages.error(request, 'There was an error uploading the event.')
    else:
        form = EventForm()
    return render(request, 'event/create_event.html', {'form': form})

# manage event page for the administrator


@user_passes_test(is_administrator)
def manage_events(request):
    """ A view to return the manage events page """
    events = Event.objects.all()
    return render(request, 'event/manage.html', {'events': events})

# edit each event page for the administrator


@user_passes_test(is_administrator)
def edit_event(request, event_id):
    """ A view to return the edit event page """
    event = get_object_or_404(Event, event_id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event edited successfully.')
            return redirect('manage')
        else:
            messages.error(request, 'There was an error editing the event.')
    else:
        form = EventForm(instance=event)
    return render(request, 'event/edit_event.html', {'form': form, 'event': event})

# delete event page for the administrator with confirmation


@user_passes_test(is_administrator)
def delete_event(request, event_id):
    """ A view for deleting an event """
    event = get_object_or_404(Event, event_id=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully.')
        return redirect('manage')
    return render(request, 'event/delete_event.html', {'event': event})

# event detail page for each event


def event_detail(request, event_id):
    """ A view to return the event detail pages """
    event = get_object_or_404(Event, event_id=event_id)
    artist_list = event.artists.split(',')
    context = {
        'event': event,
        'artist_list': artist_list,
    }
    return render(request, 'event/event_detail.html', context)
