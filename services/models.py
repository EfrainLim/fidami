from django.db import models
from categoria.models import Categoria
from  ckeditor_uploader.fields import RichTextUploadingField
from pages.mixins import ElimnacionImagenes
# Create your models here.
class Servicio(ElimnacionImagenes):
    #modelo pagina nostros
    titulo_servicio = models.CharField('Titulo Blog', max_length=70)
    resumen = models.TextField()
    imagen  = models.ImageField(upload_to='Servicios')
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido =RichTextUploadingField('Contenido')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
    
    def __str__(self):
        return self.titulo_servicio