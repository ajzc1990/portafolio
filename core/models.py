from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion_corta = models.TextField(max_length=300, verbose_name="Descripción Corta")
    descripcion_detallada = models.TextField(verbose_name="Descripción Detallada")
    tecnologias = models.CharField(max_length=200, verbose_name="Tecnologías (Ej: Django, React)")
    
    # La imagen se guardará en media/proyectos/
    imagen = models.ImageField(upload_to='proyectos/', verbose_name="Imagen de Portada")
    video = models.FileField(upload_to='proyectos/videos/', null=True, blank=True) # Nuevo campo
    # Enlaces opcionales
    link_github = models.URLField(verbose_name="Enlace GitHub", blank=True, null=True)
    link_video = models.URLField(verbose_name="Enlace Video (YouTube)", blank=True, null=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-fecha_creacion"] # Los más nuevos primero

    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    # Nuevo campo:
    contestado = models.BooleanField(default=False, verbose_name="¿Fue contestado?")

    class Meta:
        verbose_name = "mensaje de contacto"
        verbose_name_plural = "mensajes de contacto"
        ordering = ["-fecha_envio"]

    def __str__(self):
        return f"Mensaje de {self.nombre}"