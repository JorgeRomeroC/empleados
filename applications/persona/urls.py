from django.urls import path
from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-por_area/<shortname>/', views.ListByAreaEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
]