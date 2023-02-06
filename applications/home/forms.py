from django import forms
#==========================================
# Archivo con el fin de dar esilos
# al los formularios de esta app
#==========================================
from .models import Prueba

class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder':'Ingrese el titulo'})
        }

    #==========================================
    # Validacion de datos
    #==========================================
    def clean_cantidad(self):
        #recueprar el datos ingresado en el campo
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad