from rest_framework import viewsets
from core_api.Serializers.empleado_serializer import EmpleadoSerializer
from core_api.models import Empleado


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer