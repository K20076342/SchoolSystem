# Generated by Django 4.1.3 on 2022-12-08 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0025_payment_student_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='student_payment',
            new_name='student_username',
        ),
    ]
