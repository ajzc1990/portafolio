from django.contrib import admin
from .models import Proyecto, Contacto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    # Esto hace que en la lista se vea el título y la fecha
    list_display = ('titulo', 'fecha_creacion')
    # Permite buscar proyectos por título o tecnologías
    search_fields = ('titulo', 'tecnologias')

    def mostrar_miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 5px;" />', obj.imagen.url)
        return "Sin imagen"

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    # Agregamos 'contestado' a la lista visible
    list_display = ('nombre', 'email', 'fecha_envio', 'contestado')
    
    # Esto permite marcar el check directamente en la tabla:
    list_editable = ('contestado',)
    
    # Agregamos un filtro lateral para ver rápidamente cuáles faltan
    list_filter = ('contestado', 'fecha_envio')
    
    # Hacemos que los datos del usuario sean de solo lectura para no borrarlos por error
    readonly_fields = ('nombre', 'email', 'mensaje', 'fecha_envio')