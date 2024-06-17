from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import SubscribeForm

# if user clicked the subscribe button
def subscribe(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            # save data 
            form.save()
            messages.success(request, 'Thank you for subscribing!')
             # send confirmation email
            subject = 'Subsurface | Subscription Confirmation'
            message = 'Thank you for subscribing to our newsletter! Have a great day!'
            recipient_email = form.cleaned_data['email']
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = [recipient_email]

            try:
                send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            except Exception as e:
                messages.error(request, 'There was an error sending the confirmation email: {}'.format(e))
            # set session variable to check subscription
            request.session['subscribed'] = True
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, 'There was an error with your submission.')

    return redirect(request.META.get('HTTP_REFERER', '/'))