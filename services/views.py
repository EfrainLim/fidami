from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Servicio
def servicio(request, categoria_slug=None):
    categorias = None
    productos = None

    # if categoria_slug != None:
    #     categorias = get_object_or_404(Categoria, slug=categoria_slug)
    #     productos = Producto.objects.filter(categoria=categorias, es_disponible=True)
    #     paginador = Paginator(productos, 1)
    #     pagina = request.GET.get('pagina')
    #     productos_paginados = paginador.get_page(pagina)
    #     contar_productos = productos.count()
    # else:
    servicios = Servicio.objects.all().filter().order_by('id')
    contar_servicios = servicios.count()
    #ultimos_tres_registros = Portafolio.objects.order_by('-fecha_creacion')[:3]

    context = {
        'servicios': servicios,
        'contar_servicios': contar_servicios,
        #'ultimos_tres':ultimos_tres_registros,
    }
    return render(request, 'services.html', context)

def detalle_servicio(request, servicio_id):
    detalle_servicio = get_object_or_404(Servicio, id=servicio_id)
    servicios = Servicio.objects.all().filter().order_by('id')
    #ultimos_tres_registros = Servicio.objects.order_by('-fecha_creacion')[:3]
    context = {
        'detalle_servicio': detalle_servicio,
        'servicios':servicios,
    }

    return render(request, 'services-details.html',context)