from django.db import models

# Create your models here.

class PerfilUsuario(models.Model):
    nombre_usuario =models.TextField()
    contrasena = models.TextField()
    correo = models.TextField()
    
class Calendario(models.Model):
    fecha = models.DateField()
    actividad = models.TextField()
    notas = models.TextField()
    hora = models.TimeField()

class DesarrolloBebe(models.Model):
    semana = models.PositiveIntegerField(unique=True)
    descripcion = models.TextField()
    tamanoestimado = models.DecimalField(max_digits=5, decimal_places=2)
    pesoestimado = models.DecimalField(max_digits=5, decimal_places=2)
    ritmocardiaco = models.TextField()
    title = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='images/') 
    uploaded_at = models.DateTimeField(auto_now_add=True)

class SintomasMama(models.Model):
    semana = models.PositiveIntegerField()
    sintomas = models.TextField()
    descripcion = models.TextField()
    recomendaciones = models.TextField()
    title = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='images/') 
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    semana_recomendada = models.PositiveIntegerField()
    duracion = models.IntegerField()
    dificultad = models.IntegerField(choices=[(1, 'Baja'), (2, 'Media baja'), (3, 'Media'), (4, 'Alta baja'), (5, 'Alta')])
    title = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='images/') 
    uploaded_at = models.DateTimeField(auto_now_add=True)