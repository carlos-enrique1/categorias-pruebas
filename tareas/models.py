from django.db import models


# Creamos el modelo de la base de datos

class Categoria (models.Model):
    '''
    Tabla que complementa la tabla principal
    '''
    nombre=models.CharField(max_length=100,blank=False, unique=True)

    def __str__(self) -> str:
        return super().__str__()

class Tarea (models.Model):
    '''
    Aqui creamos los campos de la Base de Datos
    '''
    nombre=models.CharField(max_length=150,blank=False)
    categoria=models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    estado=models.BooleanField(blank=False)
    
    def __str__(self) -> str:
        '''
        Esta función devuelve una cadena de texto 
        '''
        return super().__str__()
