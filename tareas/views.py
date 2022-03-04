from django.shortcuts import render
from .models import Tarea

# Create your views here.

'''
Se añade un import a la clase de tu modelo y se añade la siguiente funcion
'''
def listaTareas(request):
    '''
    Creo los dos estados de las tareas para poder diferenciarlas
    Meto cada tarea en su correspondiente y en el return paso cada lista con un nombre
    concreto que se usa en el html
    '''
    pendientes=[]
    realizadas=[]
    for item in Tarea.objects.all():
        if item.estado==0:
            pendientes.append(item)
        else:
            realizadas.append(item)
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas})