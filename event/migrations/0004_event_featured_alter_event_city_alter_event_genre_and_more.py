# Generated by Django 5.0.6 on 2024-06-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.CharField(default='Unknown City', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='genre',
            field=models.CharField(default='Unknown Genre', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='organiser',
            field=models.CharField(default='Unknown Organiser', max_length=100),
        ),
    ]
