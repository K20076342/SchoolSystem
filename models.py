from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.utils import timezone
import uuid

class Student(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='Username must consist of @ followed by at least three alphanumericals')])
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)
    balance = models.CharField(max_length=10, blank=False, default=0)
    student_reference_number = models.CharField(default=uuid.uuid1,max_length=4)

class Request(models.Model):

    frequency_choices = (
    ("weekly", "Every week"),
    ("fortnightly", "Every 2 weeks"),
)
    duration_choices = (
    ("30", "30 mins"),
    ("60", "60 mins"),
)
    day_choices = (
        ('sunday','sunday'),
        ('monday','monday'),
        ('tuesday','tuesday'),
        ('wednesday','wednesday'),
        ('thursday','thursday'),
        ('friday','friday'),
        ('saturday','saturday'),
    )
    student_username = models.ForeignKey(Student,default=None,on_delete=models.CASCADE)
    student_availability = models.CharField(max_length=30,choices=day_choices,blank=False)
    number_of_lessons = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)],blank=False)

    frequency_lessons = models.CharField(max_length=20,choices=frequency_choices,blank=False)
    lesson_duration = models.CharField(max_length=2,choices=duration_choices,blank=False)
    extra_information = models.TextField(max_length=200,blank=True)

    booked = models.BooleanField(default=False)
    booked_day = models.CharField(max_length=30,choices=day_choices,default="monday")
    booked_interval = models.CharField(max_length=20,choices=frequency_choices,default="weekly")
    start_date =  models.DateTimeField(default=timezone.now,blank=None,null=None)

class Invoice(models.Model):
    '''needs to changed'''
    # invoice_reference_number = models.CharField(max_length=3, blank=False)
    # is_paid = models.BooleanField(default=False)

class Payment(models.Model):
    '''needs to be changed'''
    student_username = models.ForeignKey(Student,null=True,on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=4,blank=False,default=0000)
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
    is_paid = models.BooleanField(default=False)

