from rest_framework import serializers
from .models import Career, Franchisor, Task, Franchisee, TimeSheetEntry, WorkDay, Invoice

class CareerSerializer(serializers.ModelSerializer):
    """
    Serializer for Career model.
    """
    class Meta:
        model = Career
        fields = '__all__'

class FranchisorSerializer(serializers.ModelSerializer):
    """
    Serializer for Franchisor model.
    """
    class Meta:
        model = Franchisor
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    """
    class Meta:
        model = Task
        fields = '__all__'

class FranchiseeSerializer(serializers.ModelSerializer):
    """
    Serializer for Franchisee model.
    """
    class Meta:
        model = Franchisee
        fields = '__all__'

class TimeSheetEntrySerializer(serializers.ModelSerializer):
    """
    Serializer for TimeSheetEntry model.
    """
    class Meta:
        model = TimeSheetEntry
        fields = '__all__'

class WorkDaySerializer(serializers.ModelSerializer):
    """
    Serializer for WorkDay model.
    """
    class Meta:
        model = WorkDay
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Invoice model.
    """
    class Meta:
        model = Invoice
        fields = '__all__'