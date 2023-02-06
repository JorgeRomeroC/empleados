from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from applications.home.models import Prueba

from .forms import PruebaForm
class IndexView(TemplateView):
    template_name = 'home/pruebas.html'

class PruebaListView(ListView):
    # Donde se mostrara esta lista
    template_name = 'home/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = 'home/pruebas.html'
    context_object_name = 'lista_prueba'

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'