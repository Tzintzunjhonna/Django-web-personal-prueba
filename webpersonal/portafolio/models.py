from django.db import models

# Create your models here.

class Project(models.Model):
    tittle = models.CharField(max_length=200, verbose_name = 'Titulo') #Campo de tipo de caracteres
    description = models.TextField(verbose_name = 'Descripcion') #Campo de texto
    image = models.ImageField(verbose_name = 'Imagen', upload_to="projects") #Campo de imagen
    link = models.URLField(verbose_name = 'Direccion web', null=True, blank=True) #link guardar vacio o no
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion') #Campo de fecha y hora // Al crear estancias de projecto
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de modificacion') #Campo de fecha y hora // Al modificar la estancia del projecto
    class Meta:
        verbose_name = 'proyecto' #Traducir nombre de Project
        verbose_name_plural = 'proyectos' #Cambiar nombre a plural
        ordering = ["-created"] #Ordenar proyectos por modificación

    def __str__(self):
        return self.tittle