from django.core.management.base import BaseCommand
from faker import Faker
from lessons.models import Student
from django.core.management.base import BaseCommand
from random import randint



class Command(BaseCommand):
    USER_COUNT = 100
    DEFAULT_PASSWORD = 'Password123'
    help = 'Seeds the database with sample data'

    def __init__(self):
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        self.create_users()
        self.users = Student.objects.all()

    def create_users(self):
        self.create_johndoe()
        user_count = 1
        while user_count < self.USER_COUNT:
            print(f"Seeding student {user_count}/{self.USER_COUNT}", end='\r')
            try:
                self.create_user()
            except:
                continue
            user_count += 1
        print("Student seeding complete.      ")

    def create_johndoe(self):
        Student.objects.create_user(
            username='@janedoe',
            email='janedoe@example.org',
            password=self.DEFAULT_PASSWORD,
            first_name='Jane',
            last_name='Doe',
        )

    def create_user(self):
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = create_email(first_name, last_name)
        username = create_username(first_name, last_name)
        Student.objects.create_user(
            username=username,
            email=email,
            password=Command.DEFAULT_PASSWORD,
            first_name=first_name,
            last_name=last_name,
        )

    def get_random_user(self):
        index = randint(0,self.users.count()-1)
        return self.users[index]

def create_username(first_name, last_name):
    return '@' + first_name.lower() + last_name.lower()

def create_email(first_name, last_name):
    return first_name + '.' + last_name + '@example.org'