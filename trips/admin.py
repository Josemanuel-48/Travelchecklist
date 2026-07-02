from django.contrib import admin
from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista del admin
    list_display = ('id', 'title', 'destination', 'start_date', 'end_date', 'user')

    # Campos sobre los que se puede buscar desde la caja de búsqueda
    search_fields = ('title', 'destination', 'notes', 'user__username') # con doble guion bajo, accedes a los atributos internos de esa tabla.

    # Filtros laterales
    list_filter = ('destination', 'start_date') # el destino que buscar, y por el principio(por ejemplo)

