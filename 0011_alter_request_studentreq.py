# Generated by Django 4.1.3 on 2022-11-30 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0010_request_studentreq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='studentReq',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
