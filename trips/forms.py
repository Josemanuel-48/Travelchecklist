from django import forms
from .models import Trip, Task


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'destination', 'start_date', 'end_date', 'notes'] # campos de tipo texto, no necesitan nada(no hay que decirle nada como str....)
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}), #forms.DateInput mejora la experiencia del usuario.
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
            }
    # Declara el método de validación general del formulario, accediendo a sus propios datos (self)
    def clean(self):
        # Ejecuta las validaciones predeterminadas de Django y obtiene el diccionario con los datos limpios
        cleaned_data = super().clean()  
        
        start_date = cleaned_data.get('start_date')  
        end_date = cleaned_data.get('end_date')     

        #  Verifica que ambos campos tengan datos válidos antes de proceder a compararlos
        if start_date and end_date:
            
            # Evalúa si la fecha de finalización ocurre cronológicamente antes que la fecha de inicio
            if end_date < start_date:
                
                # Registra el error, invalida el formulario y vincula el mensaje directamente al campo 'end_date'
                self.add_error(
                    'end_date', 
                    'La fecha de finalización no puede ser anterior a la fecha de inicio.'
                )


        return cleaned_data  # retornamos



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'priority', 'due_date', 'done']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }