# Generated by Django 3.0.4 on 2020-03-11 12:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'beach'), (2, 'hiking'), (3, 'mountain')], max_length=3, null=True),
        ),
    ]