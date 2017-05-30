from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Libros(models.Model):
    Nombre = models.CharField(max_length=200, blank = False)
    Autor = models.CharField(max_length=200, blank=False)
    Editorial = models.CharField(max_length=200, blank=False)
    ISBN = models.CharField(max_length=200, blank=False)
    Precio = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(blank=True)

    def __unicode_(self):
        return self.Nombre

def libros_pre_save_reciever(sender, instance, *args, **kwargs):
    print sender
    print instance

    if not instance.slug:
        instance.slug = slugify(instance.Nombre)

pre_save.connect(libros_pre_save_reciever, sender=Libros)
