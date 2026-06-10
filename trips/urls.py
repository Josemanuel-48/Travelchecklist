from django.urls import path  # funcion para definir rutas
from . import views            # importamos las vistas de esta misma app

app_name  = "trips"           # espacio de nombres para usar rutas como trips:home

urlpatterns = [
    path('', views.home, name='home'), # ruta raiz de la app: llama a la vista home
]