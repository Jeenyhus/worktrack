from django.db import models
from django.core.exceptions import ValidationError


INVOICE_CHOICES= [
    ('BILLED', 'Billed'),
    ('NOT_BILLED', 'Not Billed'),
]

class Career(models.Model):
    '''
    Career model for the career

    Attributes:
    name: A string representing the name of the career
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Franchisor(models.Model):
    '''
    Franchisor model for the franchisor

    Attributes:
    name: A string representing the name of the franchisor
    email: A string representing the email of the franchisor
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Career, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    '''
    Task model for the franchisor

    Attributes:
    name: A string representing the name of the task
    franchisor: A foreign key to the Franchisor model
    description: A text field representing the description of the task
    date: A date field representing the date of the task
    start_time: A time field representing the start time of the task
    end_time: A time field representing the end time of the task
    duration: A duration field representing the duration of the task
    billable: A boolean field representing if the task is billable
    billed: A boolean field representing if the task is billed
    invoice: A string field representing the invoice status of the task
    '''
    name = models.CharField(max_length=100)
    franchisor = models.ForeignKey(Franchisor, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField()
    billable = models.BooleanField()
    billed = models.BooleanField()
    invoice = models.CharField(max_length=100, choices=INVOICE_CHOICES)

    def __str__(self):
        return self.name

class Franchisee(models.Model):
    '''
    Franchisee model for the franchisee
    
    Attributes:
    name: A string representing the name of the franchisee
    email: A string representing the email of the franchisee
    hourly_rate: A decimal representing the hourly rate of the franchisee
    career: A foreign key to the Career model
    franchisor: A foreign key to the Franchisor model

    '''
    name = models.CharField(max_length=100)
    email= models.EmailField()
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    franchisor = models.ForeignKey(Franchisor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name    

class TimeSheetEntry(models.Model):
    '''
    TimeSheetEntry model for the franchisee
    
    Attributes:
    franchisee: A foreign key to the Franchisee model
    task: A foreign key to the Task model
    date: A date field representing the date of the time sheet entry
    start_time: A time field representing the start time of the time sheet entry
    end_time: A time field representing the end time of the time sheet entry
    duration: A duration field representing the duration of the time sheet entry
    description: A text field representing the description of the time sheet entry
    '''
    franchisee = models.ForeignKey(Franchisee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField()
    description = models.TextField()

    def __str__(self):
        return f"Time Sheet Entry for {self.date}"
    
class WorkDay(models.Model):
    '''
    WorkDay model for the franchisee
    
    Attributes:
    franchisee: A foreign key to the Franchisee model
    task: A foreign key to the Task model
    date: A date field representing the date of the work day
    start_time: A time field representing the start time of the work day
    end_time: A time field representing the end time of the work day
    duration: A duration field representing the duration of the work day
    billable: A boolean field representing if the work day is billable
    billed: A boolean field representing if the work day is billed
    invoice: A string field representing the invoice status of the work day
    comment: A text field representing the comment of the work day
    '''
    franchisee = models.ForeignKey(Franchisee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField()
    billable = models.BooleanField()
    billed = models.BooleanField()
    invoice = models.CharField(max_length=100, choices=INVOICE_CHOICES)
    comment = models.TextField(blank=True)

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        # Check if the duration exceeds 8 hours
        if self.duration.total_seconds() > 8 * 3600:
            # Prompt the user to leave a comment
            comment = input("Please leave a comment for working more than 8 hours: ")
            self.comment = comment

        if self.duration.total_seconds() > 8 * 3600 and not self.comment:
            raise ValidationError("A comment is required for working more than 8 hours.")

        super().save(*args, **kwargs)

class Invoice(models.Model):
    '''
    Invoice model for the franchisee
    
    Attributes:
    franchisee: A foreign key to the Franchisee model
    invoice_number: A string field representing the invoice number
    invoice_date: A date field representing the invoice date
    description_of_services: A text field representing the description of the services
    hours_worked: A duration field representing the hours worked
    rate: A decimal field representing the rate
    other_expenses: A decimal field representing the other expenses
    amount_payable: A decimal field representing the amount payable
    payment_instructions: A text field representing the payment instructions
    '''
    franchisee = models.ForeignKey(Franchisee, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100)
    invoice_date = models.DateField()
    description_of_services = models.TextField()
    hours_worked = models.DurationField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    other_expenses = models.DecimalField(max_digits=8, decimal_places=2)
    amount_payable = models.DecimalField(max_digits=8, decimal_places=2)
    payment_instructions = models.TextField()

    def __str__(self):
        return f"Invoice #{self.invoice_number}"
