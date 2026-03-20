from rest_framework import serializers
from core_api.models import Auto

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'