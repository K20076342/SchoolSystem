from django.core.management.base import BaseCommand, CommandError
from lessons.models import Student

class Command(BaseCommand):
    help = 'Seeds the database with sample data'
    def handle(self, *args, **options):
        Student.objects.filter(is_staff=False).delete()