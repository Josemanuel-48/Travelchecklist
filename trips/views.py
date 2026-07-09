from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TripForm, TaskForm
from .models import Trip, Task


def home(request):
    # Home pública
    return render(request, 'trips/home.html')


def signup(request):
    # Registro de usuario
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trips:login')
    else:
        form = UserCreationForm()

    return render(request, 'trips/signup.html', {'form': form})


@login_required
def trip_list(request):  # hace peticion a la base dde datos para solitar las filas de trip.
    # Lista solo los viajes del usuario autenticado
    trips = Trip.objects.filter(user=request.user)  # trip.objets puedo filtar con filter. con los que sean de mi usuario. solicita a nuestro ORM la informacion
    return render(request, 'trips/trip_list.html', {'trips': trips})  # se crea list.html y trips muestra por pantalla.


@login_required
def trip_create(request):
    # Crear un nuevo viaje
    if request.method == 'POST':  # detecta si ahi un envio(si le ha dado al boton) si es si crea el formulario.
        form = TripForm(request.POST)  # se crea con toda la informacion que django recoge desde el forms.py detectando que hay un envio.
        if form.is_valid():   # comprueba que el form este bien, que cumpla las reglas definidas por nosotros.
            trip = form.save(commit=False)  # save----> crear un objeto de class Trip(forms.py),  commit false---que no guarde nada en la base de datos. queda en espera.
            trip.user = request.user   # accedo y le doy el usuario con el que estoy trabajando.
            trip.save()  # y ahora lo guarda. crea el objeto y esta ya en la base de datos.
            return redirect('trips:trip_list')  # se redirije al usuario a la lista de viajes.
    else:
        form = TripForm()  # crear formulario vacio si nadie lo ha creado

    return render(request, 'trips/trip_form.html', {'form': form, 'mode': 'create'}) 


@login_required
def trip_detail(request, pk):
    # Mostramos el viaje y todas sus tareas asociadas
    trip = get_object_or_404(Trip, pk=pk, user=request.user)
    tasks = trip.tasks.all()
    return render(request, 'trips/trip_detail.html', {'trip': trip, 'tasks': tasks}) 


@login_required
def trip_update(request, pk): # edita un viaje. hay que estar logueados. 
    # Editar un viaje existente
    trip = get_object_or_404(Trip, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():  # se comprueba la validez
            form.save()      # lo guardamos
            return redirect('trips:trip_detail', pk=trip.pk) # despues de editar, vamos a revisar lo que hemos cambiado. le (pk) pasamos la primary key del objeto a visualizar
    else:
        form = TripForm(instance=trip)

    return render(request, 'trips/trip_form.html', {'form': form, 'mode': 'update', 'trip': trip})


@login_required
def trip_delete(request, pk):
    # Borrar un viaje
    trip = get_object_or_404(Trip, pk=pk, user=request.user) # get_object_or_404: funcion con un error por defecto.

    if request.method == 'POST':
        trip.delete()
        return redirect('trips:trip_list')

    return render(request, 'trips/trip_confirm_delete.html', {'trip': trip})


@login_required
def task_create(request, trip_pk):
    # Crear una tarea asociada a un viaje concreto del usuario
    trip = get_object_or_404(Trip, pk=trip_pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.trip = trip
            task.save()
            return redirect('trips:trip_detail', pk=trip.pk)
    else:
        form = TaskForm()

    return render(request, 'trips/task_form.html', {'form': form, 'trip': trip, 'mode': 'create'})


@login_required
def task_update(request, pk):
    # Editar una tarea; comprobamos que el usuario sea dueño del viaje al que pertenece
    task = get_object_or_404(Task, pk=pk, trip__user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('trips:trip_detail', pk=task.trip.pk)
    else:
        form = TaskForm(instance=task)

    return render(request, 'trips/task_form.html', {'form': form, 'trip': task.trip, 'task': task, 'mode': 'update'})


@login_required
def task_delete(request, pk):
    # Borrar tarea y volver al detalle del viaje
    task = get_object_or_404(Task, pk=pk, trip__user=request.user)
    trip = task.trip

    if request.method == 'POST':
        task.delete()
        return redirect('trips:trip_detail', pk=trip.pk)

    return render(request, 'trips/task_confirm_delete.html', {'task': task, 'trip': trip})