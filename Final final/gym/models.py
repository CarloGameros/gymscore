from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class Usuario(models.Model):
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    password2 = models.CharField(max_length=200, blank=False)

    Nombres = models.CharField(max_length=200, blank = False)
    Apeidos = models.CharField(max_length=200, blank=False)
    Edad = models.CharField(max_length=200, blank=False)
    Pesoi = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
    Pesoa = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
    avance = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(blank=True)
    fecha = models.DateTimeField(auto_now=True)
    META_CHOICES = (
        ('A', 'Aumentar',),
        ('B', 'Bajar',),
    )
    meta = models.CharField(
        max_length=1,
        choices=META_CHOICES,default='B'
    )
    SEX_CHOICES = (
        ('H', 'Hombre',),
        ('M', 'Mujer',),
        ('I', 'Indistinto',),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,default='I'
    )

    def __unicode_(self):
        return self.Nombres

    @property
    def avance(self):
        return self.Pesoi - self.Pesoa

    def clean_password2(self):
        print "Entro"
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            print "Error"
            raise forms.ValidationError("Password debe coincidir! ")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email.exists():
            raise forms.ValidationError("Esta cuenta ya esta registrada, seguro que no tienes una cuenta?")
        return email

def libros_pre_save_reciever(sender, instance, *args, **kwargs):
    print sender
    print instance

    if not instance.slug:
        instance.slug = slugify(instance.Nombres)

pre_save.connect(libros_pre_save_reciever, sender=Usuario)
