# Generated by Django 4.1.3 on 2022-12-05 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0018_alter_request_booked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='Lesson_Time',
        ),
        migrations.RemoveField(
            model_name='request',
            name='Teacher',
        ),
    ]
