from django.contrib import admin
from django.urls import path, include
from applications.home.views import IndexView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
]
