from django.contrib.auth import views as auth_views  # Vistas genéricas de autenticación
from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('', views.home, name='home'),  # Home pública
    path('signup/', views.signup, name='signup'),  # Registro de usuario

    # Login usando la vista genérica de Django y nuestro template personalizado
    path('login/', auth_views.LoginView.as_view(template_name='trips/login.html'), name='login'),

    # Logout usando la vista genérica de Django
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]