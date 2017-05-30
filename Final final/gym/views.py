from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.db.models import Q
from biblioteca.multipleslug import MultiSlugMixin
import os
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Usuario
from .forms import UsuarioAdd, UsuariosModelForm, UsuariosActualizarModelForm
from django.conf import settings
from mimetypes import guess_type
from wsgiref.util import FileWrapper
from django.views.generic.detail import DetailView

# Create your views here.
def home(request):

    context=locals()
    template='home.html'
    return render(request,template,context)

class ActualizarUsuario(UpdateView):
    model = Usuario
    form_class = UsuariosActualizarModelForm
    success_url = "/gym/tablas"
    print model.email
    def get_context_data(self, *args, **kwargs):
        context = super(ActualizarUsuario, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Actualizar"
        return context

class DetalleDeUsuario(MultiSlugMixin,DetailView):
    model = Usuario

class ListaDeUsuario(ListView):
    model = Usuario

    def get_queryset(self, *args, **kwargs):
        consulta = super(ListaDeUsuario, self).get_queryset(**kwargs)
        query = self.request.GET.get("q",'')
        consulta =consulta.filter(
                      Q(Nombres__icontains=query)).order_by("Nombres")
        print query
        return consulta

class CrearUsuario(CreateView):
    model = Usuario
    form_class = UsuariosModelForm
    success_url = "/gym/crear/"

    def get_context_data(self, *args, **kwargs):
        context = super(CrearUsuario, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Registrar"
        return context

def lista_Usuario(request):
    use = Usuario.objects.all()
    print request
    mens = "Usuarios Registrados Actualmente"
    template = "listaDeUsuarios.html"
    contexto= {"Mensaje": mens,
               "Usuario": use }
    return render(request, template, contexto)

def detalle_slug(request, slug=None):
    #Logico de negocio alias hechizo
    print "hola"
    try:
        gym = get_object_or_404(Libros, slug=slug)
    except Libros.MultipleObjectsReturned:
        gym = Libros.objects.filter(slug=slug).order_by("-Apeidos").first()

    print gym
    mens = "Usuarios nuevos"
    template = "detalle_usuario.html"
    contexto= {"mensaje":mens,
           "Usuario": usuario }
    return render(request, template, contexto)

def detalle_s(request, slug=None):
    #Logico de negocio alias hechizo
    try:
        gym = get_object_or_404(Producto, slug=slug)
    except Libros.MultipleObjectsReturned:
        gym = Libros.objects.filter(slug=slug).order_by("-Apeidos").first()
    mens = "Usuario nuevos"
    template = "detalle_slug.html"
    contexto= {"mensaje":mens,
           "Usuario": usuario }
    return render(request, template, contexto)

def actualizar(request, object_id=None):
    #Logico de negocio alias hechizo
    gym = get_object_or_404(Libros, id=object_id)
    form = UsuarioModelForm(request.POST or None, instance=gy)
    if form.is_valid():
        form.save()
        print "Actualizacion exitosa!"
    template = "actualizarusuario.html"
    contexto= {
           "Usuarios": Usuario,
           "form":form,
           "titulo":"Actualizar Libro"
           }
    return render(request, template, contexto)

def detalle_libro(request, object_id=None):

    use = get_object_or_404(Libros, id=object_id)
    mens = "Usuarios Registrados Actualmente"
    template = "detalle_usuario.html"
    contexto= {"Mensaje":mens,
           "Usuario": use }
    return render(request, template, contexto)


def agregar_usuario(request):
    form = UsuarioAdd(request.POST or None)
    if form.is_valid():
        form.save()
        print "Alta hecha"
    #if request.method == "POST":
    #    print request.POST
    #if form.is_valid():
    #    data = form.cleaned_data
    #    nombre = data.get("nombre")
    #    autor = data.get("autor")
    #    editorial= data.get("editorial")
    #    isbn= data.get("isbn")
    #    precio= data.get("precio")

    #    nuevo_libro = Libros()
    #    nuevo_libro.Nombre = nombre
    #    nuevo_libro.Autor = autor
    #    nuevo_libro.Editorial = editorial
    #    nuevo_libro.ISBN = isbn
    #    nuevo_libro.Precio = precio
    #    nuevo_libro.save()

    template = "agregar_usuario.html"

    context = {
    "titulo":"Crear Usuario",
    "form":form
    }

    return render(request, template, context)
