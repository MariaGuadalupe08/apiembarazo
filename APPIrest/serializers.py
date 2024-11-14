from rest_framework import serializers
from .models import PerfilUsuario,Calendario, DesarrolloBebe, SintomasMama, Ejercicio


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = '__all__'

class CalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendario
        fields = '__all__'

class DesarrolloBebeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesarrolloBebe
        fields = '__all__'

class SintomasMamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SintomasMama
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'
