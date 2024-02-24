from rest_framework import viewsets
from rest_framework.response import Response
from .models import Career, Franchisor, Task, Franchisee, Invoice
from .serializers import CareerSerializer, FranchisorSerializer, TaskSerializer, FranchiseeSerializer, InvoiceSerializer
from rest_framework.views import APIView, Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class LoginView(APIView):
    '''
    API endpoint that allows users to login.
    
    This view is used to authenticate users and return a token.
    
    The token is used to authenticate the user in subsequent requests.
    
    The token is returned in the response body.'''
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

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