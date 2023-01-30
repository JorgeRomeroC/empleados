from django.contrib import admin
from django.urls import path, include, re_path
from applications.home.views import IndexView
urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path('', include('applications.departamento.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.persona.urls')),
]
