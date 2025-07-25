from django.urls import path
from . import views
urlpatterns = [

    path('blog',views.blog,name='blog'),
    path('detalle/<int:blog_id>/',views.detalle_blog,name='detalle_blog'),
    
    path('portafolio',views.portafolio,name='portafolio'),
    path('portafolio/detalle/<int:blog_id>/',views.detalle_Portafolio,name='detalle_portafolio'),
    
    path('nosotros',views.nosotros,name='nosotros'),
    path('miembros',views.miembros,name='miembros'),
    path('miembros/detalle/<int:miembros_id>/',views.detalle_miembros,name='detalle_miembros'),
    path('empleos',views.empleos,name='empleos'),
    path('ventas',views.ventas,name='ventas'),
    path('FAQ',views.preguntas,name='preguntas'),
    path('Historia',views.historias,name='historias'),
    path('Contacto',views.contactos,name='contactos'),
]
