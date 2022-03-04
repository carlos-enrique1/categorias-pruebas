from django.db import models


# Creamos el modelo de la base de datos

class Tarea (models.Model):
    '''
    Aqui creamos los campos de la Base de Datos
    '''
    nombre=models.CharField(max_length=150,blank=False)
    categoria=models.CharField(max_length=150,blank=False)
    estado=models.BooleanField(blank=False)
    
    def __str__(self) -> str:
        '''
        Esta función devuelve una cadena de texto 
        '''
        return super().__str__()