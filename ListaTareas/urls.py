from django.urls import path
from tareas import views
'''
Se hace un import a las vistas y se pone como vista principal la lista
'''
urlpatterns = [
    path('',views.listaTareas,name='listaTareas')
    #path('admin/', admin.site.urls),
]
