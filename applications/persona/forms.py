from ckeditor.fields import RichTextField
from django import forms

from applications.persona.models import Empleado, Habilidades


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'job': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'departamento': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'habilidades': forms.SelectMultiple(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if(first_name < 5):
            raise forms.ValidationError('El nombre debe ser tener mas de 5 caracteres')
        return first_name
        
