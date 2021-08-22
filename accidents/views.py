from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Accident
from .serializers import AccidentSerializer

# Create your views here.
class AccidentViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = []
    http_method_names = ['get','post','put']
    ordering_fields = ['id','fecha_nacimiento']
    search_fields = []
    serializer_class = AccidentSerializer
    queryset = Accident.objects.all()
