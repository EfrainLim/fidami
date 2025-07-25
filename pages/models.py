from django.db import models
# Create your models here.
from categoria.models import Categoria
from  ckeditor_uploader.fields import RichTextUploadingField
from .mixins import ElimnacionImagenes

class Blog(ElimnacionImagenes):
    #modelo pagina nostros
    titulo_blog = models.CharField('Titulo Blog', max_length=50)
    resumen = models.TextField()
    contenido =RichTextUploadingField('Contenido')
    imagenes  = models.ImageField(upload_to='Blog/Fotos')
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Blog'
        verbose_name_plural='Blogs'
    
    def __str__(self):
        return self.titulo_blog

class Nosotros(ElimnacionImagenes):
    #modelo pagina nostros
    titulo_nosotros = models.CharField('Titulo Nosotros', max_length=70)
    descripcion = models.TextField()
    imagen  = models.ImageField(upload_to='Nosotros')
    gerente = models.CharField('Nombres Gerente', max_length=70)
    imagen_gerente  = models.ImageField(upload_to='Nosotros/Gerente',blank=True)
    disponible = models.BooleanField(default=True)
    link_video=models.CharField(("video"), max_length=200,blank=True)
    titulo_experiencia=models.CharField('Titulo Experiencia', max_length=70)
    contenido =models.TextField()
    cantidad_proyectos=models.IntegerField(("Cantidad de proyectos"))
    imagen_experiencia  = models.ImageField(upload_to='experiencia')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Nosotro'
        verbose_name_plural='Nosotros'
    
    def __str__(self):
        return self.titulo_nosotros
    
class Portafolio(ElimnacionImagenes):
    #modelo pagina nostros
    titulo_portafolio = models.CharField('Titulo Portafolio', max_length=70)
    resumen = models.TextField()
    imagenes  = models.ImageField(upload_to='Portafolio')
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    hicimos = models.TextField()
    resultados = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Portafolio'
        verbose_name_plural='Portafolios'
    
    def __str__(self):
        return self.titulo_portafolio

class GaleriaPortafolio(models.Model):
    portafolio = models.ForeignKey(Portafolio, default=None, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='Portafolio/imagenes', max_length=255)

    def __str__(self):
        return self.portafolio.titulo_portafolio

    class Meta:
        verbose_name = 'Galeria Portafolio'
        verbose_name_plural = 'Galeria Portafolios'
    
class Cargo(models.Model):
    #modelo pagina nostros
    nombre = models.CharField('Nombre Cargo', max_length=40)
    class Meta:
        verbose_name='Cargo'
        verbose_name_plural='Cargos'
    
    def __str__(self):
        return self.nombre
    
class Miembros(ElimnacionImagenes):
    #modelo pagina nostros
    nombres = models.CharField('Nombres de Miembro de Equipo', max_length=70)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    foto  = models.ImageField(upload_to='Miembros',blank=True)
    descripcion=models.TextField()
    disponible = models.BooleanField(default=True)
    link_facebook=models.CharField(("Facebook"), max_length=200,blank=True)
    link_youtube=models.CharField(("Youtube"), max_length=200,blank=True)
    link_twitter=models.CharField(("Twitter"), max_length=200,blank=True)
    link_linkedln=models.CharField(("Linkedln"), max_length=200,blank=True)
    link_telefono=models.IntegerField("Telefono",blank=True)
    link_correo=models.CharField(("Correo"), max_length=100,blank=True)
    trabajo =models.TextField('Mi funcion')
    contenido =RichTextUploadingField('Contenido')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Mienbro'
        verbose_name_plural='Miembros'
    
    def __str__(self):
        return self.nombres


class Empleo(ElimnacionImagenes):
    #modelo pagina empleo
    titulo_empleo = models.CharField('Titulo de Empleo', max_length=60)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    foto  = models.ImageField(upload_to='Empleo',blank=True)
    descripcion=models.TextField()
    disponible = models.BooleanField(default=True)
    contenido =RichTextUploadingField('Contenido')
    telefono=models.IntegerField(("Telefono Empresa"),blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Empleo'
        verbose_name_plural='Empleos'
    
    def __str__(self):
        return self.titulo_empleo
    
class Venta(ElimnacionImagenes):
    #modelo pagina empleo
    nombre_venta = models.CharField('Nombre x Vender', max_length=60)
    foto  = models.ImageField(upload_to='Venta',blank=True)
    descripcion=models.TextField()
    marca= models.CharField('Marca', max_length=30,blank=True)
    modelo= models.CharField('Modelo', max_length=30,blank=True)
    precio= models.DecimalField(("Precio"), max_digits=5, decimal_places=2)
    disponible = models.BooleanField(default=True)
    contenido =models.TextField('Contenido de Empleio',blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Venta'
        verbose_name_plural='Ventas'
    
    def __str__(self):
        return self.nombre_venta

class FAQ(models.Model):
    #modelo pagina empleo
    titulo_pregunta = models.CharField('Titulo Pregunta Frecuente', max_length=60)
    descripcion=models.TextField()
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Pregunta Frecuente'
        verbose_name_plural='Pregunta Frecuente'
    
    def __str__(self):
        return self.titulo_pregunta

class Historia(ElimnacionImagenes):
    #modelo pagina empleo
    titulo_historia = models.CharField('Titulo Historia', max_length=60)
    descripcion=models.TextField('Descripcion de Acontecimiento')
    foto  = models.ImageField(upload_to='Historia',blank=True)
    fecha_acontecimiento = models.IntegerField("Año de Historia")
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Historia'
        verbose_name_plural='Historias'
    
    def __str__(self):
        return self.titulo_historia
    

