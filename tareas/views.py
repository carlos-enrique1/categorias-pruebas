from django.shortcuts import render
from .models import Tarea

# Create your views here.

'''
Se añade un import a la clase de tu modelo
'''
def listaTareas(request):
    return render(request,'listaActivos.html',{'tareas':Tarea.objects.all()})