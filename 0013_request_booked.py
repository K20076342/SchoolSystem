# Generated by Django 4.1.3 on 2022-12-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0012_alter_request_extra_information_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='Booked',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
