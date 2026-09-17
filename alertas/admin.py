from django.contrib import admin
from .models import GuiaPrimerosAuxilios, Incidente, ContactoEmergencia

@admin.register(GuiaPrimerosAuxilios)
class GuiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria_id')

@admin.register(Incidente)
class IncidenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'tipo', 'afectados', 'fecha_creacion')
    list_filter = ('tipo',)

@admin.register(ContactoEmergencia)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'telefono')