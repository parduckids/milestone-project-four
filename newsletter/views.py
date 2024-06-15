from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import SubscribeForm

def subscribe(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            # set session variable to check subscription
            request.session['subscribed'] = True
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, 'There was an error with your submission.')

    return redirect(request.META.get('HTTP_REFERER', '/'))