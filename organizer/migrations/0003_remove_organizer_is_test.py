# Generated by Django 3.0.4 on 2020-03-06 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_organizer_is_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizer',
            name='is_test',
        ),
    ]