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
    try:
        Categoria.objects.get(nombre="Todas")
    except BaseException:
        Categoria(nombre="Todas").save()
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
    '''
    Esta funcion lo que hace es crear las tareas
    '''
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
    '''
    Esta funcion lo que hace es crear las categorias
    '''
    
    nombreDeLaCategoria=request.POST['nombreCategoriaNueva']
    if nombreDeLaCategoria != None and nombreDeLaCategoria != "":
        try:
            Categoria(nombre=nombreDeLaCategoria).save()
        except:
            pass
    pendientes=tareasPendientes()
    realizadas=tareasRealizadas()
    categoria=Categoria.objects.get(nombre="Todas")
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':categoria})

def borrarCategoria(request):
    idDeLaCategoria=request.POST['categoriaABorrar']
    borrado=Categoria.objects.get(pk=idDeLaCategoria)
    try:
        borrado.delete()
    except:
        pass
    pendientes=tareasPendientes()
    realizadas=tareasRealizadas()
    categoria=Categoria.objects.get(nombre="Todas")
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':categoria})

def seleccionarCategoria(request):
    idDeLaCategoria=request.POST['seleccionCategorias']
    pendientes=[]
    realizadas=[]
    if Categoria.objects.get(pk=idDeLaCategoria).nombre=="Todas":
        pendientes=tareasPendientes()
        realizadas=tareasRealizadas()
    else:
        for item in tareasPendientes():
            if item.categoria_id==int(idDeLaCategoria):
                pendientes.append(item)
        for item in tareasRealizadas():
            if item.categoria_id==int(idDeLaCategoria):
                realizadas.append(item)
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':Categoria.objects.get(pk=idDeLaCategoria)})

def seleccionarModo(request):
    if request.POST.get('cambiar',False):
        return cambiarEstados(request)
    else:
        return borrarTareas(request)

def cambiarEstados(request):
    if request.POST.getlist('tarea'):
        for item in request.POST.getlist('tarea'):
            elemento=Tarea.objects.get(id=int(item))
            if elemento.estado is False:
                elemento.estado=True
            else:
                elemento.estado=False
            elemento.save()
    id=int(request.POST['nombreCategoria'])
    categoria=Categoria.objects.get(pk=id)
    pendientes=[]
    realizadas=[]
    if categoria.nombre=="Todas":
        pendientes=tareasPendientes()
        realizadas=tareasRealizadas()
    else:
        for item in tareasPendientes():
            if item.categoria_id==int(id):
                pendientes.append(item)
        for item in tareasRealizadas():
            if item.categoria_id==int(id):
                realizadas.append(item)
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':categoria})

def borrarTareas(request):
    if request.POST.getlist('tarea'):
        for item in request.POST.getlist('tarea'):
            elemento=Tarea.objects.get(id=int(item))
            try:
                elemento.delete()
            except:
                pass
    id=int(request.POST['nombreCategoria'])
    categoria=Categoria.objects.get(pk=id)
    pendientes=[]
    realizadas=[]
    if categoria.nombre=="Todas":
        pendientes=tareasPendientes()
        realizadas=tareasRealizadas()
    else:
        for item in tareasPendientes():
            if item.categoria_id==int(id):
                pendientes.append(item)
        for item in tareasRealizadas():
            if item.categoria_id==int(id):
                realizadas.append(item)
    return render(request,'listaTareas.html',{'tareasPendientes':pendientes,'tareasRealizadas':realizadas,'categorias':Categoria.objects.all(),'categoriaActiva':categoria})