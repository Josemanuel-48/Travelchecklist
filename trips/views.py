from django.shortcuts import render

# Create your views here.

def home(request): # crear funcion
    # renderiza(cargando en pantalla) la plantilla de inicio y la devuelve como respuesta HTTP
    return render(request, 'trips/home.html')