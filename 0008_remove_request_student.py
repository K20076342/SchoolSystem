# Generated by Django 4.1.3 on 2022-11-29 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_request_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='student',
        ),
    ]
