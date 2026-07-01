from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

def home(request): # crear funcion
    # renderiza(cargando en pantalla) la plantilla de inicio y la devuelve como respuesta HTTP
    return render(request, 'trips/home.html')

def signup(request):
    # si el usuario envia el formulario procesamos datos.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # si el formulario es valido, guardamos el nuevo usuario.
        if form.is_valid():
            form.save()
            return redirect('trips:login') # tras registrarse, lo enviamos al login
        
    else:
        # si entra pot GET; mostramos el formulario vacio
        form = UserCreationForm()

        # renderizamos el template pasando el formulario al contexto
        return render(request, 'trips/signup.html', {'form': form})