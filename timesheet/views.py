from rest_framework import viewsets
from rest_framework.response import Response
from .models import Career, Franchisor, Task, Franchisee, Invoice
from .serializers import CareerSerializer, FranchisorSerializer, TaskSerializer, FranchiseeSerializer, InvoiceSerializer

class CareerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows careers to be viewed or edited.
    """
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class FranchisorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows franchisors to be viewed or edited.
    """
    queryset = Franchisor.objects.all()
    serializer_class = FranchisorSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class FranchiseeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows franchisees to be viewed or edited.
    """
    queryset = Franchisee.objects.all()
    serializer_class = FranchiseeSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows invoices to be viewed or edited.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer