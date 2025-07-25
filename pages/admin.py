from django.contrib import admin
admin.site.site_header = "Minera Fidami S.A"
admin.site.site_title = "Principal"
admin.site.index_title = "Bienvenido a Dasboard"

from .models import Nosotros,Miembros,Cargo,Empleo,Venta,FAQ,Historia,Blog,Portafolio,GaleriaPortafolio
# Register your models here.

class ModeloAdmin(admin.ModelAdmin):
    list_display = ['id', 'texto', 'imagen1', 'imagen2']
    search_fields = ['texto']

    # Solo permitir la edición de imágenes
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:  # Si el objeto ya existe, ocultar los campos de texto
            form.base_fields['texto'].widget.attrs['readonly'] = True
        return form


class BlogAdmin(admin.ModelAdmin):
    list_display = ( 'titulo_blog', 'resumen', 'categoria' ,'fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('titulo_blog', 'categoria', 'fecha_creacion')
class PortafoliAdmin(admin.ModelAdmin):
    list_display = ( 'titulo_portafolio', 'resumen', 'categoria' ,'fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('titulo_portafolio', 'categoria', 'fecha_creacion')
class NosotrosAdmin(admin.ModelAdmin):
    list_display = ( 'titulo_nosotros', 'descripcion','fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('titulo_nosotros', 'fecha_creacion')
class MiembrosAdmin(admin.ModelAdmin):
    list_display = ( 'nombres', 'cargo','fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('nombres', 'cargo')
class EmpleoAdmin(admin.ModelAdmin):
    list_display = ( 'titulo_empleo', 'cargo','fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('titulo_empleo', 'cargo')
class VentaAdmin(admin.ModelAdmin):
    list_display = ( 'nombre_venta', 'marca','precio','fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('nombre_venta', 'marca','precio')
class FaqAdmin(admin.ModelAdmin):
    list_display = ( 'titulo_pregunta','fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('titulo_pregunta', 'fecha_modificacion')
class HistoriaAdmin(admin.ModelAdmin):
    list_display = ( 'titulo_historia','fecha_modificacion', 'disponible')
    #prepopulated_fields = {'slug': ('titulo_blog',)}
    listt_filter = ('titulo_historia', 'fecha_modificacion')
admin.site.register(Blog,BlogAdmin)
admin.site.register(Portafolio,PortafoliAdmin)
admin.site.register(GaleriaPortafolio)
admin.site.register(Nosotros,NosotrosAdmin)
admin.site.register(Miembros,MiembrosAdmin)
admin.site.register(Cargo)
admin.site.register(Empleo,EmpleoAdmin)
admin.site.register(Venta,VentaAdmin)
admin.site.register(FAQ,FaqAdmin)
admin.site.register(Historia,HistoriaAdmin)
