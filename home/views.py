from django.shortcuts import get_object_or_404, render
# Create your views here.
from pages.models import Nosotros,Blog,Portafolio
from services.models import Servicio
from .models import Empresa,Slider
#from s_tienda.models import Producto,Valoracion
def principal(request):
    
    cabezado_nosotros=Nosotros.objects.all().filter().order_by('id')
    ultimos_tres_servicios = Servicio.objects.order_by('-fecha_creacion')[:3]
    portafolios=Portafolio.objects.all().filter().order_by('id')
    ultimos_tres_blogs = Blog.objects.order_by('-fecha_creacion')[:3]
    sliders = Slider.objects.order_by('-fecha_creacion')[:1]
    sliders2 = Slider.objects.order_by('-fecha_creacion')[1:]
    context = {
        #'historias': historias,
        'ultimos_tres_servicios': ultimos_tres_servicios,
        'cabezado_nosotros':cabezado_nosotros,
        'portafolios':portafolios,
        'ultimos_tres_blogs':ultimos_tres_blogs,
        'sliders':sliders,
        'sliders2':sliders2,
    }
    
    return render(request, 'index.html',context)
