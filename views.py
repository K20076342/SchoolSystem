from django.shortcuts import render, redirect
from .forms import LogInForm, SignUpForm, RequestForm, PayForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Request, Invoice, Payment, Student

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def get_lessons(request):
    current_user = request.user
    all_lessons = Request.objects.filter(student_username=current_user,booked = True)
    #all_lessons = Request.objects.filter(booked = True)
    return render(request, 'booked_lessons.html', {'all':all_lessons})

def get_unbooked_lessons(request):
    current_user = request.user
    unbooked_lessons = Request.objects.filter(student_username=current_user,booked = False)
    return render(request, 'pending.html', {'unbooked':unbooked_lessons})

def log_out(request):
    logout(request)
    return redirect('home')

def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    return render(request, 'log_in.html', {'form':form})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form':form})

def make_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            current_user = request.user
            student_availability = form.cleaned_data.get('student_availability')
            number_of_lessons = form.cleaned_data.get('number_of_lessons')
            frequency_lessons = form.cleaned_data.get('frequency_lessons')
            lesson_duration = form.cleaned_data.get('lesson_duration')
            extra_information = form.cleaned_data.get('extra_information')
            lesson_request = Request.objects.create(
                student_username=current_user,
                student_availability=student_availability,
                number_of_lessons=number_of_lessons,
                frequency_lessons=frequency_lessons,
                lesson_duration=lesson_duration,
                extra_information=extra_information,
            )
            return redirect('dashboard')
        else:
            form = RequestForm()
        return render(request, 'make_request.html', {'form':form})

def update_request(request, pk):
    rq_id = Request.objects.get(id=pk)
    form = RequestForm(request.POST or None, instance=rq_id)
   
    if form.is_valid():
        form = form.save()
        return redirect('pending')
    return render(request, 'update_request.html',{'form':form})
    
def delete_request(request, pk):
    request = Request.objects.get(id=pk)
    request.delete()
    return redirect('dashboard')

def payments(request):
    return render(request, 'invoice.html')

def balance(request):
    return render(request, 'balance.html')

def make_payment(request):
    if request.method == 'POST':
        form = PayForm(request.POST)
        current_user = request.user
        if form.is_valid():
            invoice_number = form.cleaned_data.get('invoice_number')
            amount = form.cleaned_data.get('amount')
            pay = Payment.objects.create(
                student_username = current_user,
                invoice_number=invoice_number,
                amount = amount,
                is_paid=True
            )
            invoice = Payment.objects.filter(is_paid = True)
            return redirect('dashboard')
        return render(request, 'pay_form.html', {'form':form})


def show_payments(request):
    if request.method == 'POST':
        current_user = request.user
        all_payments = Payment.objects.filter(student_username=current_user)
        obj = Student.objects.first()
        stu_number = getattr(obj, 'student_reference_number')
        return render(request, 'payments.html', {'payments':all_payments, 'stu_number':stu_number})

def show_invoices(request):
    if request.method == 'POST':
        current_user = request.user
        all_invoices = Request.objects.filter(student_username=current_user,booked = True)
        count = 0
        obj = Student.objects.first()
        inv_messages = []
        for i in all_invoices:
            inv_num = str(getattr(obj, 'student_reference_number')) + " -" + str(count)
            cost = int(str(i.number_of_lessons))* int(str(i.lesson_duration))
            count += 1
            inv_messages.append(inv_num + "     Total Cost:   " + str(cost) )
        return render(request,'show_invoices.html', {'invoices':inv_messages})