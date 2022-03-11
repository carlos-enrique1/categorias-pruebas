from django.contrib import admin
from . import models
# Register your models here.
'''
Se indican las tablas de la base de datos
'''
admin.site.register(models.Tarea)
admin.site.register(models.Categoria)