# tickets/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from event.models import Event
from .models import Ticket
from unittest.mock import patch

class TicketModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.event = Event.objects.create(
            event_name="Test Event",
            genre="Test Genre",
            city="Test City",
            address="123 Test St",
            organiser="Test Organiser",
            date=timezone.localdate() + timezone.timedelta(days=1),
            start_time=timezone.now().time(),
            end_time=(timezone.now() + timezone.timedelta(hours=2)).time(),
            event_description="This is a test event.",
            artists="Test Artist",
            music="http://testmusic.com",
            event_image="http://testimage.com",
            ticket_price=50.00,
            max_tickets=100
        )

    def test_ticket_creation(self):
        """Test that a Ticket instance is created successfully."""
        ticket = Ticket.objects.create(
            event=self.event,
            user=self.user,
            quantity=2
        )
        self.assertEqual(ticket.event, self.event)
        self.assertEqual(ticket.user, self.user)
        self.assertEqual(ticket.quantity, 2)
        self.assertIsNotNone(ticket.purchase_date)

    def test_ticket_str_method(self):
        """Test the __str__ method of the Ticket model."""
        ticket = Ticket.objects.create(
            event=self.event,
            user=self.user,
            quantity=2
        )
        self.assertEqual(str(ticket), f'{self.user.username} - {self.event.event_name}')

class TicketViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.admin_user = User.objects.create_superuser(
            username='administrator', password='password')
        self.event = Event.objects.create(
            event_name="Test Event",
            genre="Test Genre",
            city="Test City",
            address="123 Test Street",
            organiser="Test Organiser",
            date=timezone.localdate() + timezone.timedelta(days=1),
            start_time=timezone.now().time(),
            end_time=(timezone.now() + timezone.timedelta(hours=2)).time(),
            event_description="This is a test event.",
            artists="Test Artist",
            music="http://testmusic.com",
            event_image="http://testimage.com",
            ticket_price=50.00,
            max_tickets=100
        )

    @patch('tickets.views.stripe.checkout.Session.create')
    def test_buy_ticket_view_get(self, mock_stripe_session_create):
        """Test the buy ticket view GET request."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('buy_ticket', args=[self.event.event_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'buy_ticket.html')
        self.assertContains(response, 'Test Event')

    def test_cancel_view(self):
        """Test the cancel view."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('cancel'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Your ticket purchase was canceled.')

    def test_mytickets_view(self):
        """Test the my tickets view."""
        self.client.login(username='testuser', password='password')
        Ticket.objects.create(user=self.user, event=self.event, quantity=2)
        response = self.client.get(reverse('mytickets'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_tickets.html')
        self.assertContains(response, 'Test Event')