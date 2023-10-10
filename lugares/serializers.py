from rest_framework import serializers
from .models import Lugar
from .models import Direccion

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ['id','nombre', 'descripcion']

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ['id','sitio', 'calle', 'numero', 'codigo_postal', 'colonia', 'ciudad', 'estado']