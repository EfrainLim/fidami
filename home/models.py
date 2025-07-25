from django.db import models
# Create your models here.
from pages.mixins import ElimnacionImagenes

class Empresa(ElimnacionImagenes):
    #modelo pagina nostros
    nombre = models.CharField('Nombres Empresa', max_length=70)
    logo  = models.ImageField(upload_to='Empresa',blank=True)
    logo_footer  = models.ImageField(upload_to='Empresa',blank=True)
    descripcion=models.TextField()
    disponible = models.BooleanField(default=True)
    direccion=models.CharField(("Direccion Empresa"), max_length=200,blank=True)
    direccion2=models.CharField(("Direccion Empresa"), max_length=200,blank=True)
    link_facebook=models.CharField(("Facebook Empresa"), max_length=200,blank=True)
    link_youtube=models.CharField(("Youtube Empresa"), max_length=200,blank=True)
    link_twitter=models.CharField(("Twitter Empresa"), max_length=200,blank=True)
    link_linkedln=models.CharField(("Linkedln Empresa"), max_length=200,blank=True)
    imagen_cabecera_paginas= models.ImageField(upload_to='Empresa',blank=True)
    telefono=models.IntegerField("Telefono Empresa",blank=True)
    correo=models.CharField(("Correo Empresa"), max_length=100,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Empresa'
        verbose_name_plural='Empresa'
    
    def __str__(self):
        return self.nombre

class Slider(ElimnacionImagenes):
    #modelo pagina nostros
    titulo_slider = models.CharField('Titulo Slider', max_length=70)
    imagen  = models.ImageField(upload_to='Empresa/Slider',blank=True)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Slider'
        verbose_name_plural='Slider'
    
    def __str__(self):
        return self.titulo_slider
