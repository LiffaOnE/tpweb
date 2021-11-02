from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics

from api.models import Service
from api.serializers import ServiceSerializer, RegisterSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer