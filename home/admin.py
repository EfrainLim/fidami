from django.contrib import admin
# Register your models here.
from .models import Empresa,Slider

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'direccion' ,'telefono','fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('nombre', 'direccion', 'fecha_creacion')
class SliderAdmin(admin.ModelAdmin):
    list_display = ( 'titulo_slider' ,'fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('titulo_slider',  'fecha_creacion')
admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Slider,SliderAdmin)