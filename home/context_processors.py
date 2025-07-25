
from .models import Empresa,Slider
from pages.models import Blog
def empresa(request):
    
    empresa=Empresa.objects.all()
    ultimos_2_blogs = Blog.objects.order_by('-fecha_creacion')[:2]
    
    return {'empresa':empresa,'ultimos_2_blogs':ultimos_2_blogs,}