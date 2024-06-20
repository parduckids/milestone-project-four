from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ContactMessage


def about(request):
    """ A view to return the about page with the contact form """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            # save the form data to the database
            contact_message = ContactMessage(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            contact_message.save()

            # send email to the default email that's set on settings.py
            recipients = [settings.DEFAULT_FROM_EMAIL]
            try:
                send_mail(subject, message, email, recipients)
                messages.success(
                    request, 'Your message has been sent successfully!')
                return redirect('about')
            except Exception as e:
                messages.error(
                    request, 'There was an error sending your message: ' + str(e))
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'about.html')
