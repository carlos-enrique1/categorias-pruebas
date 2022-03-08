from http.client import HTTPResponse
from unicodedata import category
from django.shortcuts import render
from .models import Categoria, Tarea

# Create your views here.

def tareasPendientes():
    pendientes=[]
    for item in Tarea.objects.all():
        if item.estado==0:
            pendientes.append(item)
    return pendientes

def tareasRealizadas():
    realizadas=[]
    for item in Tarea.objects.all():
        if item.estado==1:
            realizadas.append(item)
    return realizadas

'''
Se añade un import a la clase de tu modelo y se añade la siguiente funcion
'''
def listaTareas(request):
    '''
    Creo los dos estados de las tareas para poder diferenciarlas
    Meto cada tarea en su correspondiente y en el return paso cada lista con un nombre
    concreto que se usa en el html
    '''
    pendientes=tareasPendientes()
    realizadas=tareasRealizadas()
    categoria=Categoria.objects.get(nombre="Todas")
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':categoria})

def listaTareasC(request,id):
    '''
    Cada vez que se llama a una categoria concreta se llama a esta funcion que seleciona
    todas las tareas pendientes y realizadas y las envia al html
    '''
    pendientes=[]
    realizadas=[]
    for item in tareasPendientes():
        if item.categoria_id==id:
            pendientes.append(item)
    for item in tareasRealizadas():
        if item.categoria_id==id:
            realizadas.append(item)
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':Categoria.objects.get(pk=id)})

def crearTarea(request):
    nombreDeLaTarea=request.POST['nombreTarea']
    categoriaDeLaTarea=request.POST['categoriasCrearTarea']
    if nombreDeLaTarea != None and nombreDeLaTarea != "":
        Tarea(nombre=nombreDeLaTarea,categoria_id=categoriaDeLaTarea,estado=0).save()
    pendientes=[]
    realizadas=[]
    for item in tareasPendientes():
        if item.categoria_id==int(categoriaDeLaTarea):
            pendientes.append(item)
    for item in tareasRealizadas():
        if item.categoria_id==int(categoriaDeLaTarea):
            realizadas.append(item)
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':Categoria.objects.get(pk=categoriaDeLaTarea)})

def crearCategoria(request):
    nombreDeLaCategoria=request.POST['nombreCategoriaNueva']
    if nombreDeLaCategoria != None and nombreDeLaCategoria != "":
        Categoria(nombre=nombreDeLaCategoria).save()
    pendientes=tareasPendientes()
    realizadas=tareasRealizadas()
    categoria=Categoria.objects.get(nombre="Todas")
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':categoria})

def borrarCategoria(request):
    return


def modificarTarea(request):
    return