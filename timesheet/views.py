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
    # Retrieve all invoices from the database
    invoices = Invoice.objects.all()
    # Render the template with invoices
    return render(request, 'invoice.html', {'invoices': invoices})

def generate_invoice(request, time_sheet_entry_id):
    # Retrieve the time sheet entry based on the provided ID
    time_sheet_entry = get_object_or_404(TimeSheetEntry, pk=time_sheet_entry_id)
    
    # Perform operations to generate an invoice based on the time sheet entry
    total_hours_worked = time_sheet_entry.duration.total_seconds() / 3600  # Convert duration to hours
    rate_per_hour = time_sheet_entry.franchisee.hourly_rate
    amount_payable = total_hours_worked * rate_per_hour

    # Create an Invoice object
    invoice = Invoice(
        franchisee=time_sheet_entry.franchisee,
        invoice_number='',  # You may generate or assign an invoice number here
        invoice_date=time_sheet_entry.date,
        description_of_services=time_sheet_entry.task.description,
        hours_worked=time_sheet_entry.duration,
        rate=rate_per_hour,
        other_expenses=0,  # Update if there are other expenses
        amount_payable=amount_payable,
        payment_instructions='Please pay within 30 days.',  # Example payment instructions
    )

    # Save the invoice to the database
    invoice.save()

    # Optionally, you can update the time sheet entry to mark it as invoiced
    time_sheet_entry.invoiced = True
    time_sheet_entry.save()

    # Redirect to the invoice detail page
    return redirect('invoice_detail', invoice_id=invoice.pk)

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
