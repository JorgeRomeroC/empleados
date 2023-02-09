from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView, FormView)
from .models import Empleado
from .forms import EmpleadoForm


class InicioView(TemplateView):
    """Vista qeu carga la pagina de inicio"""
    template_name = 'inicio.html'


# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un area de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    # FUNCION QUE NOS PERMITA UTILIZAR EL BUSCARDOS DE LA TABLA
    # LISTAR EMPLEADOS
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        # si full_name es jorge esto buscara todos lo empleados
        # que contengan ese letra
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

#==========================================
# Esta clase es utilizada por Departamento
# para listar por area
#==========================================

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
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
    form_class = EmpleadoForm
    #podemos solo pedir algunos campos
    #fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades',]

    #o pedimos todos los campos de ese modelo
    #fields = ('__all__')
    #con el uso de "reverse_lazy" para la redireccion
    # debemos agregar en las urls.py de la app el atributo name
    success_url = reverse_lazy('persona_app:empleados_admin')

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
    form_class = EmpleadoForm
    #fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', ]
    success_url = reverse_lazy('persona_app:empleados_admin')

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
    success_url = reverse_lazy('persona_app:empleados_admin')


