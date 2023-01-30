from django.shortcuts import render
from django.views.generic import (ListView)

from .models import Empleado

# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un area de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    context_object_name = 'lista'

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name=area
    )
        return lista

class ListEmpleadosByKword(ListView):
    """Lista empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print("*****************")
        palabra_clave = self.request.GET.get("kword", '')
        print('============', palabra_clave)
        return[]