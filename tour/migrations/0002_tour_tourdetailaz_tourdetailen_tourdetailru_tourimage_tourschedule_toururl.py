# Generated by Django 3.0.4 on 2020-03-06 13:45

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('descriptionaz', models.TextField(blank=True, null=True)),
                ('descriptionen', models.TextField(blank=True, null=True)),
                ('descriptionru', models.TextField(blank=True, null=True)),
                ('type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[], max_length=3, null=True)),
                ('country', models.CharField(default='Azerbaijan', max_length=31)),
                ('city', models.CharField(blank=True, max_length=31, null=True)),
                ('adress', models.CharField(blank=True, max_length=63, null=True)),
                ('price', models.IntegerField()),
                ('pricefor', models.IntegerField(default=1)),
                ('currency', models.CharField(default='AZN', max_length=31)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('distance', models.CharField(blank=True, max_length=31, null=True)),
                ('durationday', models.IntegerField(blank=True, null=True)),
                ('durationnight', models.IntegerField(blank=True, null=True)),
                ('datefrom', models.DateField()),
                ('dateto', models.DateField(blank=True, null=True)),
                ('viewcount', models.IntegerField(default=0)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='tour/avatar/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='tour/cover/')),
                ('guide', models.CharField(blank=True, max_length=31, null=True)),
                ('status', models.IntegerField(choices=[(1, 'publish'), (2, 'draft'), (3, 'past')], default=1)),
                ('organizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizer.Organizer')),
            ],
        ),
        migrations.CreateModel(
            name='TourUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour/schedule/')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour/image/')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourDetailRU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31)),
                ('text', models.TextField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourDetailEN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31)),
                ('text', models.TextField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourDetailAZ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31)),
                ('text', models.TextField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.Tour')),
            ],
        ),
    ]
