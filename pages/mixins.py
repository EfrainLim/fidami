import os
from django.db import models

class ElimnacionImagenes(models.Model):
    class Meta:
        abstract = True  # Este modelo no se creará como tabla

    def delete(self, *args, **kwargs):
        # Borrar las imágenes del servidor
        for field in self._meta.get_fields():
            if isinstance(field, models.ImageField):
                image = getattr(self, field.name)
                if image and os.path.isfile(image.path):
                    os.remove(image.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el objeto ya existe
            old_instance = self.__class__.objects.get(pk=self.pk)
            # Borrar las imágenes anteriores si se han cambiado o limpiado
            for field in self._meta.get_fields():
                if isinstance(field, models.ImageField):
                    old_image = getattr(old_instance, field.name)
                    new_image = getattr(self, field.name)
                    if old_image and (new_image is None or old_image != new_image):
                        if os.path.isfile(old_image.path):
                            os.remove(old_image.path)
        super().save(*args, **kwargs)
