"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from libros import views
from gym import views
from gym.views import ActualizarUsuario
from accounts.views import RegistroView, InicioView
#from libros.views import LibrosListView, LibrosDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    #url(r'^agregar_libro/$', views.agregar_libro, name='agregar_libro'),
    #url(r'^listaDeLibros/$', views.lista_libros, name='lista_libros'),
    #url(r'^actializar/(?P<pk>\d+)/editar/$', views.actualizar, name='actualizar'),
    #url(r'^detalle_libro/(?P<object_id>\d+)/editar/$', views.actualizar, name='actualizar'),
    #url(r'^Libros/lista/$', LibrosListView.as_view(), name='List_view'),
    #url(r'^Libros/(?P<pk>\d+)/$', LibrosDetailView.as_view(), name='detalle_view'),
    #url(r'^detalle_libro/(?P<object_id>\d+)/$', views.detalle_libro, name='detalle_libro'),
    url(r'^libros/', include("libros.urls", namespace='libros')),
    url(r'^gym/', include("gym.urls", namespace='gym')),
    url(r'^registro/$', RegistroView.as_view(), name='Registro'),
    url(r'^inicio/$', InicioView.as_view(), name='Inicio'),
    url(r'^(?P<pk>\d+)/editar/$', ActualizarUsuario.as_view(), name='actualizar'),
]
