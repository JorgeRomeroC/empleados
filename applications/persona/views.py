from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView)

from .models import Empleado

# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un area de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    model = Empleado


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
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleados = Empleado.objects.get(id=8)
        return empleados.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

#==========================================
# Quiero que cuando se envie el formulario
# de registro de nuevo empleado, me redirija
# a  otra pagina
#==========================================
class SuccessView(TemplateView):
    template_name = "persona/success.html"


#==========================================
# Creacion de nuevo empleado
#==========================================
class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    #podemos solo pedir algunos campos
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades',]

    #o pedimos todos los campos de ese modelo
    #fields = ('__all__')
    #con el uso de "reverse_lazy" para la redireccion
    # debemos agregar en las urls.py de la app el atributo name
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        #super tambien se utiliza para indicar que voy a sibreecribir
        #un funcion pre-establecida como en este caso "form_valid"
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', ]
    success_url = reverse_lazy('persona_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:correcto')


