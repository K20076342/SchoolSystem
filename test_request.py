from django.core.exceptions import ValidationError
from django.test import TestCase
from lessons.models import Request, Student
from lessons.forms import RequestForm

class RequestTest(TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        self.user = Student.objects.create_user(
            '@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            password='Password123',
        )
        self.request = Request(
            studentReq=self.user,
            Student_Availability='sunday',
            Number_Of_Lessons=5,
            Frequency_Lessons="Every week",
            Lesson_Duration="30 mins",
            Extra_Information="Good teacher",
        )

    def test_student_must_not_be_blank(self):
        self.request.studentReq = None
        with self.assertRaises(ValidationError):
            self.request.full_clean()

    def test_availability_must_not_be_blank(self):
        self.request.Student_Availability = None
        with self.assertRaises(ValidationError):
            self.request.full_clean()     

    def test_lessonsnumber_must_not_be_blank(self):
        self.request.Number_Of_Lessons = None
        with self.assertRaises(ValidationError):
            self.request.full_clean()    

    def test_lessonfrequency_must_not_be_blank(self):
        self.request.Frequency_Lessons = None
        with self.assertRaises(ValidationError):
            self.request.full_clean()    
    def test_lessonduration_must_not_be_blank(self):
        self.request.Lesson_Duration= None
        with self.assertRaises(ValidationError):
            self.request.full_clean()    