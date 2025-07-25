from django.urls import path
from . import views
urlpatterns = [
    path('',views.servicio,name='servicio'),
    path('detalle/<int:servicio_id>/',views.detalle_servicio,name='detalle_servicio'),
]
