from django.shortcuts import render
from rest_framework import viewsets
from .models import PerfilUsuario,Calendario, DesarrolloBebe, SintomasMama, Ejercicio
from .serializers import PerfilUsuarioSerializer, CalendarioSerializer, DesarrolloBebeSerializer, SintomasMamaSerializer, EjercicioSerializer
# Create your views here.


class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    
class CalendarioViewSet(viewsets.ModelViewSet):
    queryset = Calendario.objects.all()
    serializer_class = CalendarioSerializer

class DesarrolloBebeViewSet(viewsets.ModelViewSet):
    queryset = DesarrolloBebe.objects.all()
    serializer_class = DesarrolloBebeSerializer

class SintomasMamaViewSet(viewsets.ModelViewSet):
    queryset = SintomasMama.objects.all()
    serializer_class = SintomasMamaSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer
