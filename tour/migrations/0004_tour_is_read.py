# Generated by Django 3.0.4 on 2020-03-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_auto_20200306_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='is_read',
            field=models.CharField(default='', max_length=31),
            preserve_default=False,
        ),
    ]