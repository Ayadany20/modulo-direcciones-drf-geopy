from admin_geodany.models import Empleado
from rest_framework import  serializers
from admin_geodany.models import Auto

class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ['nombre_completo', 'puesto', 'fecha_registro']
       

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'