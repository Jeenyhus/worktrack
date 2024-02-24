from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TimeSheetEntry, Invoice, Career, Franchisor, Task, Franchisee, INVOICE_CHOICES
from .forms import TaskForm, FranchiseeForm, InvoiceForm

def home(request):
    return render(request, 'home.html')

def time_sheet(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('time_sheet')
    else:
        form = TaskForm()
    time_sheet_entries = TimeSheetEntry.objects.all()
    return render(request, 'time_sheet.html', {'form': form, 'time_sheet_entries': time_sheet_entries})

def invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice')
    else:
        form = InvoiceForm()
    invoices = Invoice.objects.all()
    return render(request, 'invoice.html', {'form': form, 'invoices': invoices})

def invoice_detail(request, invoice_id):
    # Retrieve the invoice based on the provided ID
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    # Render the template with the invoice details
    return render(request, 'invoice_detail.html', {'invoice': invoice})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('time_sheet')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def create_franchisee(request):
    if request.method == 'POST':
        form = FranchiseeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('time_sheet')
    else:
        form = FranchiseeForm()
    return render(request, 'create_franchisee.html', {'form': form})

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice')
    else:
        form = InvoiceForm()
    return render(request, 'create_invoice.html', {'form': form})
