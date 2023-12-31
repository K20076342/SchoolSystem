from django import forms
from .models import Student, Request, Invoice, Payment
from django.core.validators import RegexValidator

class SignUpForm(forms.ModelForm):

    class Meta:

        model = Student
        fields = ['first_name', 'last_name', 'username', 'email']

    new_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        validators=[RegexValidator(
            regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
            message= "Password must contain an uppercase character, a lowercase character and a number")])
    password_confirmation = forms.CharField(label="Password confirmation", widget=forms.PasswordInput())

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password.')
        
    def save(self):
        super().save(commit=False)
        user = Student.objects.create_user(
            self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('new_password'))
        return user
   
class LogInForm(forms.Form):
        username = forms.CharField(label="Username")
        password = forms.CharField(label="Password", widget=forms.PasswordInput())

class RequestForm(forms.ModelForm):
    
    class Meta:

        model = Request
        fields = ['student_availability', 'number_of_lessons', 
        'frequency_lessons', 'lesson_duration', 'extra_information']

# class InvoiceForm(forms.ModelForm):
#     '''needs to be changed'''
#     class Meta:
#         model = Invoice
#         fields = ['invoice_reference_number', 'is_paid']
    
class PayForm(forms.ModelForm):
    '''needs to be changed'''
    class Meta:
        model = Payment
        fields = ['invoice_number','amount']