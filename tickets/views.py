# views.py
import stripe
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import TicketPurchaseForm
from .models import Event, Ticket


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
                try:
                    # create a stripe checkout session
                    session = stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        line_items=[{
                            'price_data': {
                                'currency': 'gbp',
                                'unit_amount': int(event.ticket_price * 100), 
                                'product_data': {
                                    'name': event.event_name,
                                },
                            },
                            'quantity': ticket_quantity,
                        }],
                        mode='payment',
                        # redirect to "my tickets" page after successful payment
                        success_url=request.build_absolute_uri('/mytickets/'),  
                         # redirect back to event page if cancelled
                        cancel_url=request.build_absolute_uri(f'/event/{event_id}/'), 
                        # pass event id, user id, and ticket quantity as reference
                        client_reference_id=f"{event_id}_{request.user.id}_{ticket_quantity}",  
                    )
                    
                    # redirect user to stripe checkout page
                    return redirect(session.url)
                except stripe.error.StripeError as e:
                    # handle any stripe related errors
                    messages.error(request, f'There was an error with your payment: {str(e)}')
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

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        # retrieve the event id, user id, and ticket quantity from the client_reference_id
        reference_id = session.client_reference_id
        event_id, user_id, ticket_quantity = reference_id.split('_')
        
        event = get_object_or_404(Event, event_id=event_id)
        user = get_object_or_404(User, id=user_id)

        try:
            # create and save the ticket purchase
            ticket = Ticket.objects.create(
                event=event,
                user=user,
                quantity=ticket_quantity,
            )
            
            # add a success message
            messages.success(request, 'Payment successful! Your tickets have been booked.')
        except Exception as e:
            # handle any ticket creation errors
            messages.error(request, f'There was an error creating your ticket: {str(e)}')

    return HttpResponse(status=200)

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
