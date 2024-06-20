# event/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Event
from .forms import EventForm


class EventModelTests(TestCase):

    def setUp(self):
        # set up date
        self.event = Event.objects.create(
            event_name="Test Event",
            genre="Test Genre",
            city="Test City",
            address="123 Test St",
            organiser="Test Organiser",
            date=timezone.localdate(),
            start_time=timezone.now().time(),
            end_time=(timezone.now() + timezone.timedelta(hours=2)).time(),
            event_description="This is a test event.",
            artists="Test Artist",
            music="http://testmusic.com",
            event_image="http://testimage.com",
            ticket_price=50.00,
            max_tickets=100
        )

    def test_event_creation(self):
        """Test that an Event instance is created successfully."""
        event = Event.objects.get(event_id=self.event.event_id)
        self.assertEqual(event.event_name, "Test Event")
        self.assertEqual(event.genre, "Test Genre")
        self.assertEqual(event.city, "Test City")
        self.assertEqual(event.address, "123 Test St")
        self.assertEqual(event.organiser, "Test Organiser")
        self.assertEqual(event.event_description, "This is a test event.")
        self.assertEqual(event.artists, "Test Artist")
        self.assertEqual(event.music, "http://testmusic.com")
        self.assertEqual(event.event_image, "http://testimage.com")
        self.assertEqual(event.ticket_price, 50.00)
        self.assertEqual(event.max_tickets, 100)

    def test_event_str_method(self):
        """Test the __str__ method of the Event model."""
        event = Event.objects.get(event_id=self.event.event_id)
        self.assertEqual(str(event), "Test Event")

    def test_formatted_date_today(self):
        """Test the formatted_date property when the event is today."""
        event = Event.objects.get(event_id=self.event.event_id)
        self.assertEqual(event.formatted_date, "Today")

    def test_formatted_date_tomorrow(self):
        """Test the formatted_date property when the event is tomorrow."""
        event = Event.objects.create(
            event_name="Tomorrow Event",
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
        self.assertEqual(event.formatted_date, "Tomorrow")


    def test_formatted_date_this_year(self):
        """Test the formatted_date property when the event is later this year."""
        event = Event.objects.create(
            event_name="This Year Event",
            genre="Test Genre",
            city="Test City",
            address="123 Test St",
            organiser="Test Organiser",
            date=timezone.localdate().replace(month=12, day=31),
            start_time=timezone.now().time(),
            end_time=(timezone.now() + timezone.timedelta(hours=2)).time(),
            event_description="This is a test event.",
            artists="Test Artist",
            music="http://testmusic.com",
            event_image="http://testimage.com",
            ticket_price=50.00,
            max_tickets=100
        )
        self.assertEqual(event.formatted_date, event.date.strftime('%B %d'))

    def test_remaining_tickets(self):
        """Test the remaining_tickets property."""
        event = Event.objects.get(event_id=self.event.event_id)
        self.assertEqual(event.remaining_tickets, 100)


class EventViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_user(
            username='administrator', password='password')
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
            max_tickets=100,
            featured=True
        )

    def test_index_view(self):
        """Test the index view returns the featured events."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/index.html')
        self.assertContains(response, 'Test Event')
        self.assertQuerysetEqual(
            response.context['events'], [self.event],
            transform=lambda x: x
        )

    def test_events_view(self):
        """Test the events view returns current or future events."""
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/events.html')
        self.assertContains(response, 'Test Event')
        self.assertQuerysetEqual(
            response.context['events'], [self.event],
            transform=lambda x: x
        )

    def test_create_event_view(self):
        """Test the create event view for an administrator."""
        self.client.login(username='administrator', password='password')
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/create_event.html')

        # test POST request
        data = {
            'event_name': 'New Test Event',
            'genre': 'New Genre',
            'city': 'New City',
            'address': '456 Test Ave',
            'organiser': 'New Organiser',
            'date': timezone.localdate() + timezone.timedelta(days=2),
            'start_time': (timezone.now() + timezone.timedelta(hours=3)).time(),
            'end_time': (timezone.now() + timezone.timedelta(hours=5)).time(),
            'event_description': 'This is a new test event.',
            'artists': 'New Artist',
            'ticket_price': 60.00,
            'max_tickets': 200,
        }
        response = self.client.post(reverse('create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('manage'))
        self.assertTrue(Event.objects.filter(event_name='New Test Event').exists())

    def test_manage_events_view(self):
        """Test the manage events view for an administrator."""
        self.client.login(username='administrator', password='password')
        response = self.client.get(reverse('manage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/manage.html')
        self.assertContains(response, 'Test Event')

    def test_edit_event_view(self):
        """Test the edit event view for an administrator."""
        self.client.login(username='administrator', password='password')
        response = self.client.get(reverse('edit_event', args=[self.event.event_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/edit_event.html')

        # test POST request
        data = {
            'event_name': 'Updated Test Event',
            'genre': 'Updated Genre',
            'city': 'Updated City',
            'address': '789 Test Street',
            'organiser': 'Updated Organiser',
            'date': self.event.date,
            'start_time': self.event.start_time,
            'end_time': self.event.end_time,
            'event_description': 'This is an updated test event.',
            'artists': 'Updated Artist',
            'ticket_price': 70.00,
            'max_tickets': 300,
        }
        response = self.client.post(reverse('edit_event', args=[self.event.event_id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('manage'))
        self.event.refresh_from_db()
        self.assertEqual(self.event.event_name, 'Updated Test Event')

    def test_delete_event_view(self):
        """Test the delete event view for an administrator."""
        self.client.login(username='administrator', password='password')
        response = self.client.get(reverse('delete_event', args=[self.event.event_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/delete_event.html')

        # test POST request
        response = self.client.post(reverse('delete_event', args=[self.event.event_id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('manage'))
        self.assertFalse(Event.objects.filter(event_id=self.event.event_id).exists())

    def test_event_detail_view(self):
        """Test the event detail view."""
        response = self.client.get(reverse('event_detail', args=[self.event.event_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/event_detail.html')
        self.assertContains(response, 'Test Event')
        self.assertContains(response, 'Test Artist')