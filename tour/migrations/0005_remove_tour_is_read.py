# Generated by Django 3.0.4 on 2020-03-06 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_tour_is_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='is_read',
        ),
    ]
