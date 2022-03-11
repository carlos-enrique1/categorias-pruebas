from ast import expr_context
import re
from django.shortcuts import render
from .models import Categoria, Tarea

# Create your views here.

def tareasPendientes():
    '''
    Esta funcion devuelve una lista con las tareas pendientes
    '''
    pendientes=[]
    for item in Tarea.objects.all():
        if item.estado==0:
            pendientes.append(item)
    return pendientes

def tareasRealizadas():
    '''
    Esta funcion devuelve una lista con las tareas realizadas
    ''' 
    realizadas=[]
    for item in Tarea.objects.all():
        if item.estado==1:
            realizadas.append(item)
    return realizadas

def listarTareas(request,categoria,problemas):
    if categoria.nombre!="Todas":
        pendientes=[]
        realizadas=[]
        for item in tareasPendientes():
            if item.categoria_id==categoria.id:
                pendientes.append(item)
        for item in tareasRealizadas():
            if item.categoria_id==categoria.id:
                realizadas.append(item)
    else:
        pendientes=tareasPendientes()
        realizadas=tareasRealizadas()
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':categoria,'error':problemas})

def crearCategoriaTodas():
    try:
        Categoria.objects.get(nombre="Todas")
    except BaseException:
        Categoria(nombre="Todas").save()
    return Categoria.objects.get(nombre="Todas")
'''
Se añade un import a la clase de tu modelo y se añade la siguiente funcion
'''
def listaTareas(request):
    '''
    Creo los dos estados de las tareas para poder diferenciarlas
    Meto cada tarea en su correspondiente y en el return paso cada lista con un nombre
    concreto que se usa en el html
    '''
    return listarTareas(request,crearCategoriaTodas(),"")

def crearTarea(request):
    '''
    Esta funcion lo que hace es crear las tareas
    '''
    problema=""
    try:
        nombreDeLaTarea=request.POST['nombreTarea']
        categoriaDeLaTarea=Categoria.objects.get(nombre=request.POST['categoriasCrearTarea'])
        if len(nombreDeLaTarea)>30 and nombreDeLaTarea.count(' ')<1:
            problema="Texto no valido"
        elif nombreDeLaTarea != None and nombreDeLaTarea != "":
            Tarea(nombre=nombreDeLaTarea,categoria_id=categoriaDeLaTarea.id,estado=0).save()
        else:
            problema="No hay texto"
    except:
        categoriaDeLaTarea=Categoria.objects.get(nombre="Todas")
        problema="Todavia no hay categorias"
    return listarTareas(request,categoriaDeLaTarea,problema)

def crearCategoria(request):
    '''
    Esta funcion lo que hace es crear las categorias
    '''
    problemas=""
    try:
        nombreDeLaCategoria=request.POST['nombreCategoriaNueva']
        if nombreDeLaCategoria != None and nombreDeLaCategoria != "" and (len(nombreDeLaCategoria)<15 and nombreDeLaCategoria.count(' ')<1):
            try:
                Categoria(nombre=nombreDeLaCategoria).save()
                categoria=Categoria.objects.get(nombre=nombreDeLaCategoria)
            except:
                categoria=Categoria.objects.get(nombre="Todas")
                problemas="No hay texto"
        else:
            categoria=Categoria.objects.get(nombre="Todas")
            problemas="No hay texto"
    except:
        categoria=Categoria.objects.get(nombre="Todas")
    return listarTareas(request,categoria,problemas)

def borrarCategoria(request):
    problema=""
    try:
        try:
            categoria=Categoria.objects.get(nombre=request.POST['nombreCategoria'])
        except:
            categoria=Categoria.objects.get(nombre="Todas")
        try:
            borrado=Categoria.objects.get(nombre=request.POST['categoriaABorrar'])
        except:
            problema="No hay categorias"
            categoria=Categoria.objects.get(nombre="Todas")
            return listarTareas(request,categoria,problema)
        id=borrado.id
        borrado.delete()
        if categoria.id==id:
            categoria=Categoria.objects.get(nombre="Todas")
    except:
        problema="Esta categoria tiene tareas"
    return listarTareas(request,categoria,problema)

def seleccionarCategoria(request):
    try:
        categoria=Categoria.objects.get(nombre=(request.POST['seleccionCategorias']))
    except:
        categoria=Categoria.objects.get(nombre="Todas")
    return listarTareas(request,categoria,"")

def cambiarEstados(request):
    if request.POST.getlist('tarea'):
        for item in request.POST.getlist('tarea'):
            elemento=Tarea.objects.get(id=int(item))
            if elemento.estado is False:
                elemento.estado=True
            else:
                elemento.estado=False
            elemento.save()
    try:
        categoria=Categoria.objects.get(nombre=request.POST['nombreCategoria'])
    except:
        categoria=Categoria.objects.get(nombre="Todas")
    return listarTareas(request,categoria,"")

def borrarTareas(request):
    if request.POST.getlist('tarea'):
        for item in request.POST.getlist('tarea'):
            elemento=Tarea.objects.get(id=int(item))
            try:
                elemento.delete()
            except:
                pass
    try:
        categoria=Categoria.objects.get(nombre=request.POST['nombreCategoria'])
    except:
        categoria=Categoria.objects.get(nombre="Todas")
    return listarTareas(request,categoria,"")

def seleccionarModo(request):
    if request.POST.get('cambiar',False):
        return cambiarEstados(request)
    elif request.POST.get('crearTareaBoton',False):
        return crearTarea(request)
    elif request.POST.get('crearCategoriaBoton',False):
        return crearCategoria(request)
    elif request.POST.get('borrarCategoriaBoton',False):
        return borrarCategoria(request)
    elif request.POST.get('seleccionarCategoriaBoton',False):
        return seleccionarCategoria(request)
    elif request.POST.get('eliminar',False):
        return borrarTareas(request)
        