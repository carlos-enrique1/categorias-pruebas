from django.urls import path
from tareas import views
'''
Se hace un import a las vistas y se pone como vista principal la lista
'''
urlpatterns = [
    path('',views.listaTareas,name='listaTareas'),
    path('<int:id>',views.listaTareasC,name='listaTareasC'),
    path('crearTarea',views.crearTarea,name='crearTarea'),
    path('crearCategoria',views.crearCategoria,name='crearCategoria'),
    path('borrarCategoria',views.borrarCategoria,name='borrarCategoria'),
    path('cambiarEstados',views.cambiarEstados,name='cambiarEstados'),
    path('borrarTareas',views.borrarTareas,name='borrarTareas'),
    path('seleccionarCategoria',views.seleccionarCategoria,name='seleccionarCategoria')
    
    
    #path('admin/', admin.site.urls),
]
