from django.urls import path
from tareas import views
'''
Se definen los enlaces y a quien llaman
'''
urlpatterns = [
    path('',views.listaTareas,name='listaTareas'),
    path('seleccionarModo',views.seleccionarModo,name='seleccionarModo')
    
    #path('admin/', admin.site.urls),
]
