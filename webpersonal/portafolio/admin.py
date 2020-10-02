from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #Para leer en Administracion

admin.site.register(Project, ProjectAdmin) # configurar el modelo