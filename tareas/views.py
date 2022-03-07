from django.shortcuts import render
from .models import Categoria, Tarea

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
    categoria=Categoria.objects.get(nombre="Todas")
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':categoria})

def listaTareasC(request,id):
    '''
    Cada vez que se llama a una categoria concreta se llama a esta funcion que seleciona
    todas las tareas pendientes y realizadas y las envia al html
    '''
    pendientes=[]
    realizadas=[]
    for item in Tarea.objects.filter(categoria_id=id).all():
        if item.estado==0:
            pendientes.append(item)
        else:
            realizadas.append(item)
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':Categoria.objects.get(pk=id)})