from django.db import models
from django.contrib.auth.models import User

class GuiaPrimerosAuxilios(models.Model):
    titulo = models.CharField(max_length=100)
    categoria_id = models.CharField(max_length=50, unique=True)
    pasos = models.TextField(help_text="Escribe los pasos separados por saltos de línea")

    def __str__(self):
        return self.titulo

class Incidente(models.Model):
    TIPO_CHOICES = [
        ('medico', 'Emergencia Médica'),
        ('incendio', 'Incendio'),
        ('seguridad', 'Seguridad / Robo'),
        ('otro', 'Otro'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidentes')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    afectados = models.IntegerField(default=1)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ContactoEmergencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contactos')
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)