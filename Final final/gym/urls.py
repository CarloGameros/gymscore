from django.conf.urls import url
from django.contrib import admin
from gym import views
from gym.views import (ListaDeUsuario, DetalleDeUsuario, CrearUsuario, ActualizarUsuario)

urlpatterns = [
    url(r'^tablas/$', ListaDeUsuario.as_view(), name='lista'),
    url(r'^(?P<pk>\d+)/$', DetalleDeUsuario.as_view(), name='detalle'),
    url(r'^crear/$', CrearUsuario.as_view(), name='crear'),
    url(r'^(?P<slug>[\w-]+)/$', DetalleDeUsuario.as_view(), name='detalle_slug'),
    url(r'^(?P<slug>[\w-]+)/editar/$', ActualizarUsuario.as_view(), name='actualizar'),
    url(r'^registrate/$', CrearUsuario.as_view(), name='registrate'),
    ]
