# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from event.models import Event
from .models import Ticket
from .forms import TicketPurchaseForm

@login_required
def buy_ticket(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.event = event
            ticket.user = request.user
            ticket.save()
            messages.success(request, 'Ticket bought successfully!')
            return redirect('/')
        else:
            messages.error(request, 'There was an error with your purchase. Please try again.')
    else:
        form = TicketPurchaseForm()
    return render(request, 'buy_ticket.html', {'event': event, 'form': form})


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
