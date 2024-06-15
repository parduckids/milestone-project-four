from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm 
from .models import Event
# import allauth decorator to check if admin is logged in, add it to all admin restricted views
from django.contrib.auth.decorators import user_passes_test

# todo, add 404, 302 etc pages... 

# check if username is administrator
def is_administrator(user):
    """ A view to check if the user has admin rights """
    return user.is_authenticated and user.username == 'administrator'

def index(request):
    """ A view to return the index page with only featured events """
    featured_events = Event.objects.filter(featured=True)
    return render(request, 'event/index.html', {'events': featured_events})
# todo: filtering events 
def events(request):
    """ A view to return the events page with filtering """
    events = Event.objects.all()

    # get filter parameters from the request
    genre = request.GET.get('event_type')
    event_date = request.GET.get('event_date')
    city = request.GET.get('event_city')

    # apply filters if parameters are provided
    if genre:
        events = events.filter(genre=genre)
    if event_date:
        events = events.filter(date=event_date)
    if city:
        events = events.filter(city=city)

    # render the template with the filtered events
    return render(request, 'event/events.html', {'events': events})
@user_passes_test(is_administrator)
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
@user_passes_test(is_administrator)
def manage_events(request):
    """ A view to return the manage events page """
    events = Event.objects.all()
    return render(request, 'event/manage.html', {'events': events})

# todo: event data doesn't show on edit event page when normal layout is set, layout needs to be changed, image should be shown
@user_passes_test(is_administrator)
def edit_event(request, event_id):
    """ A view to return the edit event page """
    event = get_object_or_404(Event, event_id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('manage')  # Change 'manage' to your desired redirect URL
    else:
        form = EventForm(instance=event)
    return render(request, 'event/edit_event.html', {'form': form, 'event': event})


# todo: event data doesn't show on delete event page

@user_passes_test(is_administrator)
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

    
