# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from event.models import Event
from .models import Ticket
from .forms import TicketPurchaseForm

@login_required
def buy_ticket(request, event_id):
    # get the event object based on the provided event_id
    event = get_object_or_404(Event, event_id=event_id)
    
    # calculate the remaining tickets for the event
    remaining_tickets = event.remaining_tickets

    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        
        if form.is_valid():
            # get the quantity of tickets from the form data
            ticket_quantity = form.cleaned_data['quantity']
            
            # check if the requested quantity is available
            if ticket_quantity <= remaining_tickets:
                # create a new ticket instance without saving it to the database
                ticket = form.save(commit=False)
                ticket.event = event
                ticket.user = request.user
                ticket.save()
                
                # add a success message
                messages.success(request, 'Ticket bought successfully!')
                
                # redirect to the home page
                return redirect('/')
            else:
                # add an error message 
                messages.error(request, 'The requested number of tickets exceeds the available tickets.')
        else:
            # add an error message if the form is not valid
            messages.error(request, 'There was an error with your purchase. Please try again.')
    else:
        # create an empty form instance with the quantity set to 1
        form = TicketPurchaseForm(initial={'quantity': 1})

    # add context to it
    context = {
        'event': event,
        'form': form,
        'remaining_tickets': remaining_tickets,
    }
    
    return render(request, 'buy_ticket.html', context)

@login_required
def mytickets(request):
    user = request.user
    tickets = Ticket.objects.filter(user=user).select_related('event')
     # create a list of numbers for each ticket
    for ticket in tickets:
        ticket.number_range = range(1, ticket.quantity + 1)
        
    context = {
        'tickets': tickets
    }
    return render(request, 'my_tickets.html', context)
