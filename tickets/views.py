import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from event.models import Event
from .models import Ticket
from .forms import TicketPurchaseForm

# Set your Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def buy_ticket(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    remaining_tickets = event.remaining_tickets

    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            ticket_quantity = form.cleaned_data['quantity']
            if ticket_quantity <= remaining_tickets:
                try:
                    # create a Stripe Checkout Session
                    checkout_session = stripe.checkout.Session.create(
                        line_items=[
                            {
                                'price_data': {
                                    # change currency to gbp
                                    'currency': 'gbp',  
                                    # price in cents
                                    'unit_amount': int(event.ticket_price * 100),  
                                    'product_data': {
                                        # use event_name
                                        'name': event.event_name,  
                                    },
                                },
                                'quantity': ticket_quantity,
                            },
                        ],
                        mode='payment',
                        success_url=request.build_absolute_uri('/') + 'success/', 
                        cancel_url=request.build_absolute_uri('/') + 'cancel/', 
                    )
                    # store event_id and ticket_quantity in session
                    request.session['purchase_data'] = {
                        'event_id': event.event_id,
                        'quantity': ticket_quantity,
                    }
                    return redirect(checkout_session.url)

                except Exception as e:
                    messages.error(request, f'An error occurred: {e}')
                    return redirect('buy_ticket', event_id=event_id)

            else:
                messages.error(request, 'The requested number of tickets exceeds the available tickets.')
        else:
            messages.error(request, 'There was an error with your purchase. Please try again.')
    else:
        form = TicketPurchaseForm(initial={'quantity': 1})

    context = {
        'event': event,
        'form': form,
        'remaining_tickets': remaining_tickets,
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'buy_ticket.html', context)

def success(request):
    # retrieve purchase data from session
    purchase_data = request.session.get('purchase_data')

    if purchase_data:
        try:
            # create the ticket
            Ticket.objects.create(
                user=request.user,
                event=Event.objects.get(event_id=purchase_data['event_id']),
                quantity=purchase_data['quantity']
            )

            # clear the purchase data from the session
            del request.session['purchase_data']
            messages.success(request, 'Your ticket purchase was successful! Thank you.')
        except Exception as e:
            messages.error(request, f'An error occurred while creating your ticket: {e}')
    else:
        messages.warning(request, 'No purchase data found. Please try again.')

    return redirect('/mytickets')

def cancel(request):
    messages.warning(request, 'Your ticket purchase was canceled.')
    return redirect('/')

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
