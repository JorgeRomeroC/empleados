from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from applications.home.models import Prueba


class IndexView(TemplateView):
    template_name = 'home/home.html'

class PruebaListView(ListView):
    # Donde se mostrara esta lista
    template_name = 'home/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = 'home/pruebas.html'
    context_object_name = 'lista_prueba'