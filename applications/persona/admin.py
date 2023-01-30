from django.contrib import admin

from .models import Empleado, Habilidades

admin.site.register(Habilidades)

#==========================================
# LOS DATOS QUE QUIERO APAREZCAN EN LA TABLA
# DEL ADMIN
#==========================================
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    #
    def full_name(self, obj):
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name

    #incorporar un buscador
    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades',)
    #==========================================
    # Este tipo de filtro sirve solo para los
    # campos muchos a muchos
    #==========================================
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)