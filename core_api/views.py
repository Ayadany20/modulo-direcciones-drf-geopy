from django.shortcuts import render
from rest_framework import viewsets
from admin_geodany.models import Auto
from .Serializers.auto_serializer import AutoSerializer
from admin_geodany.models import Direccion
from .Serializers.direccion_serializer import DireccionSerializer
from rest_framework.permissions import AllowAny


class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [AllowAny]  
