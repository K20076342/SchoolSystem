from django.contrib import admin
from .models import Student, Request, Invoice, Payment

admin.site.site_header = 'MSMS Admin Page'
admin.site.index_title = 'MSMS ADMIN PORTAL'

@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email']

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'student_username', 'student_availability', 'number_of_lessons', 
    'frequency_lessons', 'lesson_duration', 'extra_information']
    
    list_display = ['id', 'student_username', 'booked', 'start_date']
    list_filter = ['booked', 'start_date']

# @admin.register(Invoice)
# class InvoiceAdmin(admin.ModelAdmin):
#     readonly_fields = [
#         'id',]
#     list_display = ['invoice_reference_number','is_paid']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = [
        'id']
    list_display = ['student_username','invoice_number','amount']