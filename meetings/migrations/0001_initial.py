# Generated by Django 3.0.3 on 2020-04-24 07:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('floor_number', models.IntegerField()),
                ('room_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('start_time', models.TimeField(default=datetime.time(9, 0))),
                ('duration', models.IntegerField(default=1)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Room')),
            ],
        ),
    ]
