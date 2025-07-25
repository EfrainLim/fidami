from django.urls import reverse
from django.db import models
from pages.mixins import ElimnacionImagenes
# Create your models here.
class Categoria(ElimnacionImagenes):
    nombre_categoria = models.CharField( unique=True , max_length=50)
    slug = models.SlugField(max_length=100,unique=True)
    def __str__(self) :
        return self.nombre_categoria
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def get_url(self):
            return reverse('productos_x_categoria', args=[self.slug])