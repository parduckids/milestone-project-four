from django.db import models
# set up db model for contact form
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
