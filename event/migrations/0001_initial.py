# Generated by Django 5.0.6 on 2024-06-12 00:01

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=200)),
                ('event_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('genre', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('organiser', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('event_description', models.TextField()),
                ('artists', models.CharField(max_length=255)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('music', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
