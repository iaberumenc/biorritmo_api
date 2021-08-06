from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Employee
from .employeesSerializer import EmployeeSerializer

# Create your views here.
class EmployeeViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = []
    http_method_names = ['get','post','put']
    ordering_fields = ['id','fecha_nacimiento','fecha_accidente']
    search_fields = []
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()