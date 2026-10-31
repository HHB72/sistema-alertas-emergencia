from django.db import models
from django.contrib.auth.models import User

# Tabla: Guía de Primeros Auxilios
# Almacena el contenido informativo de asistencia médica con sus respectivos pasos.
class GuiaPrimerosAuxilios(models.Model):
    titulo = models.CharField(max_length=100)                    # Título visible de la guía de auxilio
    categoria_id = models.CharField(max_length=50, unique=True)  # Identificador único de la categoría
    pasos = models.TextField(help_text="Escribe los pasos separados por saltos de línea") # Pasos detallados de asistencia

    def __str__(self):
        return self.titulo

# Tabla: Incidente
# Permite registrar los reportes de emergencias generados vinculados a un usuario.
class Incidente(models.Model):
    TIPO_CHOICES = [
        ('medico', 'Emergencia Médica'),
        ('incendio', 'Incendio'),
        ('seguridad', 'Seguridad / Robo'),
        ('otro', 'Otro'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidentes') # Usuario que reporta el incidente
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)                           # Categoría o tipo de emergencia
    afectados = models.IntegerField(default=1)                                           # Cantidad numérica de personas afectadas
    descripcion = models.TextField()                                                       # Detalle de lo ocurrido
    fecha_creacion = models.DateTimeField(auto_now_add=True)                               # Fecha y hora automática del reporte

# Tabla: Contacto de Emergencia
# Guarda la agenda de números útiles o contactos de confianza asociados a cada usuario.
class ContactoEmergencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contactos') # Usuario propietario del contacto
    nombre = models.CharField(max_length=100)                                           # Nombre o entidad del contacto útil
    telefono = models.CharField(max_length=30)                                          # Número telefónico de llamada rápida