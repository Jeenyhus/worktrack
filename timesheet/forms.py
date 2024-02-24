from django import forms
from django.forms import ModelForm, DateInput, TimeInput, Select, TextInput, Textarea, CheckboxInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Career, Franchisor, Task, Franchisee, Invoice, INVOICE_CHOICES

class CareerForm(ModelForm):
    class Meta:
        model = Career
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'})
        }
    
class FranchisorForm(ModelForm):
    class Meta:
        model = Franchisor
        fields = ['name', 'description', 'category']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'})
        }
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'franchisor', 'description', 'date', 'start_time', 'end_time', 'billable', 'billed', 'invoice']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'validationCustom01', 'placeholder': 'Task Name', 'required': True}),
            'franchisor': Select(attrs={'class': 'form-control', 'id': 'validationCustom02', 'required': True}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Task Description', 'required': True}),
            'date': DateInput(attrs={'class': 'form-control', 'id': 'validationCustom03', 'placeholder': 'Task Date', 'required': True}),
            'start_time': TimeInput(attrs={'class': 'form-control', 'id': 'validationCustom04', 'placeholder': 'Start Time', 'required': True}),
            'end_time': TimeInput(attrs={'class': 'form-control', 'id': 'validationCustom05', 'placeholder': 'End Time', 'required': True}),
            'billable': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'invalidCheck', 'required': True}),
            'billed': CheckboxInput(attrs={'class': 'form-check-input'}),
            'invoice': Select(attrs={'class': 'form-control'}),
        }

class FranchiseeForm(forms.ModelForm):
    class Meta:
        model = Franchisee
        fields = ['name', 'email', 'hourly_rate', 'career', 'franchisor']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'hourly_rate': TextInput(attrs={'class': 'form-control'}),
            'career': Select(attrs={'class': 'form-control'}),
            'franchisor': Select(attrs={'class': 'form-control'}),
        }

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['franchisee', 'invoice_number', 'invoice_date', 'description_of_services', 'hours_worked', 'rate', 'other_expenses', 'amount_payable', 'payment_instructions']
        widgets = {
            'franchisee': Select(attrs={'class': 'form-control'}),
            'invoice_number': TextInput(attrs={'class': 'form-control'}),
            'invoice_date': DateInput(attrs={'class': 'form-control'}),
            'description_of_services': Textarea(attrs={'class': 'form-control'}),
            'hours_worked': TextInput(attrs={'class': 'form-control'}),
            'rate': TextInput(attrs={'class': 'form-control'}),
            'other_expenses': TextInput(attrs={'class': 'form-control'}),
            'amount_payable': TextInput(attrs={'class': 'form-control'}),
            'payment_instructions': Textarea(attrs={'class': 'form-control'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'password1': TextInput(attrs={'class': 'form-control'}),
            'password2': TextInput(attrs={'class': 'form-control'})
        }
