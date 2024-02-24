from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('time-sheet/', views.time_sheet, name='time_sheet'),
    path('invoice/', views.invoice, name='invoice'),
    path('generate-invoice/<int:time_sheet_entry_id>/', views.generate_invoice, name='generate_invoice'),
    path('invoice/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
]
