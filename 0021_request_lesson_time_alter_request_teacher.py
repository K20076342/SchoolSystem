# Generated by Django 4.1.3 on 2022-12-07 04:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0020_request_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='Lesson_Time',
            field=models.DateTimeField(blank=None, default=django.utils.timezone.now, null=None),
        ),
        migrations.AlterField(
            model_name='request',
            name='Teacher',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
