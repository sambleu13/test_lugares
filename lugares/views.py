from django.shortcuts import render
from rest_framework import generics
from .models import Lugar
from .models import Direccion
from .serializers import LugarSerializer
from .serializers import DireccionSerializer

# Create your views here.

#escondido un get
#APIView recibe y responde en JSON
#View html
class ListaLugaresView(generics.ListAPIView):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

class ListaDireccionesView(generics.ListAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class DetalleLugarView(generics.ListAPIView):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

