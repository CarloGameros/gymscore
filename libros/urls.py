from django.conf.urls import url
from django.contrib import admin
from libros import views
from libros.views import (ListaDeLibros, DetalleDeLibros, CrearLibro, ActualizarLibro)

urlpatterns = [
    url(r'^(?P<pk>\d+)/editar/$', ActualizarLibro.as_view(), name='actualizar'),
    url(r'^(?P<pk>\d+)/$', DetalleDeLibros.as_view(), name='detalle'),
    url(r'^crear/$', CrearLibro.as_view(), name='crear'),
    url(r'^lista/$', ListaDeLibros.as_view(), name='lista'),
    url(r'^(?P<slug>[\w-]+)/$', DetalleDeLibros.as_view(), name='detalle_slug'),
]
