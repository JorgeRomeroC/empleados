#==========================================
# a traves de este formulario necesitamos
# enviar datos a dos modelos o tablas
# distintas
#==========================================
from django import forms
class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control'
                             }))
    apellido = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'
                               }))
    departamento = forms.CharField(max_length=50,
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control'
                                   }))
    shortname = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'
                                }))

