from django.contrib import admin
# Register your models here.
from .models import Servicio
# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    list_display = ( 'titulo_servicio', 'resumen', 'categoria' ,'fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('titulo_servicio', 'categoria', 'fecha_creacion')

admin.site.register(Servicio,ServicioAdmin)


