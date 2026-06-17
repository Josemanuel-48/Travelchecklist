from django.contrib.auth import views as auth_views
from django.urls import path  # funcion para definir rutas
from . import views            # importamos las vistas de esta misma app

app_name  = "trips"           # espacio de nombres para usar rutas como trips:home

urlpatterns = [
    path('', views.home, name='home'), # ruta raiz de la app: llama a la vista home
    
    path('signup/', views.signup, name='signup'), # ruta para el registro de usuarios.

    # login usando la vista generica de Django y nuestro template personalizado.
    path('login/', auth_views.LoginView.as_view(template_name='trips/login.html'), name='login'),

    # path('logout/', views.logout, name='logout'), # ruta para el logout de usuarios
]