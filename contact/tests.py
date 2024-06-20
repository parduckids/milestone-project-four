# contact/tests.py
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.core import mail
from django.conf import settings
from unittest.mock import patch
from .models import ContactMessage

class ContactMessageModelTests(TestCase):

    def setUp(self):
        self.contact_message = ContactMessage.objects.create(
            name="Adam V",
            subject="Test Subject",
            message="This is a test message.",
            email="test@test.com"
        )
    
    def test_contact_message_creation(self):
        """Test that a ContactMessage instance is created successfully."""
        contact_message = ContactMessage.objects.get(id=self.contact_message.id)
        self.assertEqual(contact_message.name, "Adam V")
        self.assertEqual(contact_message.subject, "Test Subject")
        self.assertEqual(contact_message.message, "This is a test message.")
        self.assertEqual(contact_message.email, "test@test.com")
        self.assertIsNotNone(contact_message.created_at)
        
    def test_contact_message_str_method(self):
        """Test the __str__ method of the ContactMessage model."""
        contact_message = ContactMessage.objects.get(id=self.contact_message.id)
        self.assertEqual(str(contact_message), "Test Subject")
        
    def test_contact_message_email_field(self):
        """Test the email field validation."""
        invalid_email = "not_an_email"
        contact_message = ContactMessage(
            name="Hello W",
            subject="Invalid Email Test",
            message="This message should not be created.",
            email=invalid_email
        )
        with self.assertRaises(ValidationError):
            contact_message.full_clean()

class AboutViewTests(TestCase):

    def test_about_page_get(self):
        """Test the about page GET request."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_about_page_post_valid_data(self):
        """Test the about page POST request with valid data."""
        valid_data = {
            'name': 'Adam V',
            'email': 'test@test.com',
            'subject': 'Test Subject',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse('about'), data=valid_data)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('about'))
        self.assertTrue(ContactMessage.objects.filter(subject='Test Subject').exists())
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Test Subject')

    def test_about_page_post_missing_data(self):
        """Test the about page POST request with missing data."""
        invalid_data = {
            'name': 'Adam V',
            'email': 'test@test.com',
            'subject': 'Test Subject',
        }
        response = self.client.post(reverse('about'), data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ContactMessage.objects.filter(subject='Test Subject').exists())
        self.assertEqual(len(mail.outbox), 0)
        self.assertContains(response, 'Please fill out all fields.')

    @patch('contact.views.send_mail')
    def test_about_page_post_email_failure(self, mock_send_mail):
        """Test the about page POST request with email sending failure."""
        mock_send_mail.side_effect = Exception("SMTP error")

        invalid_email_data = {
            'name': 'Adam V',
            'email': 'test@test.com',
            'subject': 'Test Subject',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse('about'), data=invalid_email_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ContactMessage.objects.filter(subject='Test Subject').exists())
        self.assertEqual(len(mail.outbox), 0)
        self.assertContains(response, 'There was an error sending your message')