# Generated by Django 4.1.3 on 2022-12-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0015_alter_request_startdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='Teacher',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
