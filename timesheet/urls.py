from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CareerViewSet, FranchisorViewSet, TaskViewSet, FranchiseeViewSet, InvoiceViewSet

router = DefaultRouter()
router.register(r'careers', CareerViewSet)
router.register(r'franchisors', FranchisorViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'franchisees', FranchiseeViewSet)
router.register(r'invoices', InvoiceViewSet)

urlpatterns = router.urls