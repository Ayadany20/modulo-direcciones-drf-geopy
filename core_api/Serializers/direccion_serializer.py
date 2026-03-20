from rest_framework import serializers
from admin_geodany.models import Direccion
from geopy.geocoders import Nominatim

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

    def create(self, validated_data):
        lat = validated_data.get('latitud')
        lon = validated_data.get('longitud')

        if lat is None or lon is None:
            raise serializers.ValidationError("Latitud y longitud son requeridas")

        geolocator = Nominatim(user_agent="mi_app")

        try:
            location = geolocator.reverse((lat, lon))
            direccion = location.address if location else "Dirección no encontrada"
        except Exception as e:
            direccion = "Error al obtener dirección"
            print("Error Geopy:", e)

        print("Dirección obtenida:", direccion)

        validated_data.pop('direccion', None)

        instance = Direccion.objects.create(**validated_data)

        # asignar dirección después
        instance.direccion = direccion
        instance.save()

        return instance
