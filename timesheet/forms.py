from models import Career, Franchisor, Task, Franchisee, Invoice, INVOICE_CHOICES
from django import forms
from django.forms import ModelForm, DateInput, TimeInput, Select, TextInput, Textarea, CheckboxInput, DurationField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
    
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'franchisor', 'description', 'date', 'start_time', 'end_time', 'duration', 'billable', 'billed', 'invoice']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'franchisor': Select(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
            'start_time': TimeInput(attrs={'class': 'form-control'}),
            'end_time': TimeInput(attrs={'class': 'form-control'}),
            'duration': DurationField(attrs={'class': 'form-control'}),
            'billable': CheckboxInput(attrs={'class': 'form-control'}),
            'billed': CheckboxInput(attrs={'class': 'form-control'}),
            'invoice': Select(attrs={'class': 'form-control'})
        }

class FranchiseeForm(ModelForm):
    class Meta:
        model = Franchisee
        fields = ['name', 'email', 'description', 'category']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'})
        }

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['name', 'franchisee', 'description', 'date', 'start_time', 'end_time', 'duration', 'billable', 'billed', 'invoice']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'franchisee': Select(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
            'start_time': TimeInput(attrs={'class': 'form-control'}),
            'end_time': TimeInput(attrs={'class': 'form-control'}),
            'duration': DurationField(attrs={'class': 'form-control'}),
            'billable': CheckboxInput(attrs={'class': 'form-control'}),
            'billed': CheckboxInput(attrs={'class': 'form-control'}),
            'invoice': Select(attrs={'class': 'form-control'})
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