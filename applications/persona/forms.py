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
            'avatar',
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
            'habilidades': forms.CheckboxSelectMultiple(
                attrs={
                    'type': 'checkbox',
                    'class': 'form-check-input'
                }
            ),
            'avatar': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

