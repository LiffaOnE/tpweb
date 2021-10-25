from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.models import Service
from api.serializers import ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()