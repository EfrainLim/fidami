from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Nosotros,Miembros,Empleo,Venta,FAQ,Historia,Blog,Portafolio,GaleriaPortafolio

def blog(request, categoria_slug=None):
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
    anuncio = Blog.objects.all().filter().order_by('id')
    contar_anuncio = anuncio.count()
    ultimos_tres_registros = Blog.objects.order_by('-fecha_creacion')[:3]

    context = {
        'anuncios': anuncio,
        'contar_productos': contar_anuncio,
        'ultimos_tres':ultimos_tres_registros,
    }
    return render(request, 'blog-classic.html', context)

def detalle_blog(request, blog_id):
    
    detalle_blog = get_object_or_404(Blog, id=blog_id)
    ultimos_tres_registros = Blog.objects.order_by('-fecha_creacion')[:3]
    context = {
        'blog': detalle_blog,
        'ultimos_tres':ultimos_tres_registros,
    }

    return render(request, 'blog-details.html',context)

def portafolio(request, categoria_slug=None):
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
    portafolios = Portafolio.objects.all().filter().order_by('id')
    contar_portafolios = portafolios.count()
    ultimos_tres_registros = Portafolio.objects.order_by('-fecha_creacion')[:3]

    context = {
        'portafolios': portafolios,
        'contar_productos': contar_portafolios,
        'ultimos_tres':ultimos_tres_registros,
    }
    return render(request, 'project-style1.html', context)

def detalle_Portafolio(request, blog_id):
    
    detalle_portafolio = get_object_or_404(Portafolio, id=blog_id)
    galeria_portafolio = GaleriaPortafolio.objects.filter(portafolio_id=detalle_portafolio.id)

    ultimos_tres_registros = Portafolio.objects.order_by('-fecha_creacion')[:3]
    context = {
        'portafolio': detalle_portafolio,
        'ultimos_tres':ultimos_tres_registros,
        'galeria_portafolio':galeria_portafolio,
    }

    return render(request, 'project-details.html',context)

def nosotros(request, categoria_slug=None):
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
    nosotros = Nosotros.objects.all().filter().order_by('id')
    contar_nosotros = nosotros.count()
    membros_alea = Miembros.objects.order_by('?')[:4]
    ultimos_tres_registros = Blog.objects.order_by('-fecha_creacion')[:3]

    context = {
        'nosotros': nosotros,
        'contar_nosotros': contar_nosotros,
        'membros_alea':membros_alea,
        'ultimos_tres':ultimos_tres_registros,
    }
    return render(request, 'about-us.html', context)

def miembros(request):
    miembros = Miembros.objects.all().filter().order_by('id')
    contar_miembros = miembros.count()
    #ultimos_tres_registros = Portafolio.objects.order_by('-fecha_creacion')[:3]

    context = {
        'miembros': miembros,
        'contar_miembros': contar_miembros,
        #'ultimos_tres':ultimos_tres_registros,
    }
    return render(request, 'our-team-member.html', context)

def detalle_miembros(request,miembros_id):
    miembros = get_object_or_404(Miembros, id=miembros_id)
    #ultimos_tres_registros = Portafolio.objects.order_by('-fecha_creacion')[:3]

    context = {
        'miembro': miembros,
    }
    return render(request, 'team-member-details.html', context)

def empleos(request):
    empleos = Empleo.objects.all().filter().order_by('id')
    contar_empleos = empleos.count()
    #ultimos_tres_registros = Portafolio.objects.order_by('-fecha_creacion')[:3]

    context = {
        'empleos': empleos,
        'contar_empleos': contar_empleos,
        #'ultimos_tres':ultimos_tres_registros,
    }
    return render(request, 'talent.html', context)

def ventas(request):
    ventas = Venta.objects.all().filter().order_by('id')
    contar_ventas = ventas.count()
    #ultimos_tres_registros = Portafolio.objects.order_by('-fecha_creacion')[:3]

    context = {
        'ventas': ventas,
        'contar_ventas': contar_ventas,
        #'ultimos_tres':ultimos_tres_registros,
    }
    return render(request, 'sales.html', context)


def preguntas(request):
    preguntas = FAQ.objects.all().filter().order_by('id')
    contar_preguntas = preguntas.count()
    ultimo_registro = FAQ.objects.order_by('-fecha_creacion')[:1]

    context = {
        'preguntas': preguntas,
        'contar_preguntas': contar_preguntas,
        'ultimo_registro':ultimo_registro,
    }
    return render(request, 'faq.html', context)

def historias(request):
    historias = Historia.objects.all().filter().order_by('id')
    contar_historias = historias.count()
    ultimo_registro = Historia.objects.order_by('-fecha_creacion')[:1]
    cabezado_nosotros=Nosotros.objects.all().filter().order_by('id')
    context = {
        'historias': historias,
        'contar_historias': contar_historias,
        'cabezado_nosotros':cabezado_nosotros,
    }
    return render(request, 'our-history.html', context)

def contactos(request):
    
    return render(request, 'contact-us.html')