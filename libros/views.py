from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.db.models import Q
from biblioteca.multipleslug import MultiSlugMixin
from .models import Libros
from .forms import LibroAddForm, LibrosModelForm
import os
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import LibroAddForm, LibrosModelForm
from .models import Libros
from django.conf import settings
from mimetypes import guess_type
from wsgiref.util import FileWrapper
from django.views.generic.detail import DetailView


# Create your views here.

def home(request):

    context=locals()
    template='home.html'
    return render(request,template,context)

class ActualizarLibro(UpdateView):
    model = Libros
    form_class = LibrosModelForm
    success_url = "/libros/lista/"

    def get_context_data(self, *args, **kwargs):
        context = super(ActualizarLibro, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Actualizar"
        return context

class DetalleDeLibros(MultiSlugMixin,DetailView):
    model = Libros

class ListaDeLibros(ListView):
    model = Libros

    def get_queryset(self, *args, **kwargs):
        consulta = super(ListaDeLibros, self).get_queryset(**kwargs)
        query = self.request.GET.get("q",'')
        consulta =consulta.filter(
                      Q(Nombre__icontains=query)).order_by("Nombre")
        print query
        return consulta

class CrearLibro(CreateView):
    model = Libros
    form_class = LibrosModelForm
    success_url = "/libros/crear/"

    def get_context_data(self, *args, **kwargs):
        context = super(CrearLibro, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Registrar"
        return context

def lista_libros(request):
    lib = Libros.objects.all()
    print request
    mens = "Libros Registrados Actualmente"
    template = "listaDeLibros.html"
    contexto= {"Mensaje": mens,
               "Libros": lib }
    return render(request, template, contexto)

def detalle_slug(request, slug=None):
    #Logico de negocio alias hechizo
    print "hola"
    try:
        libros = get_object_or_404(Libros, slug=slug)
    except Libros.MultipleObjectsReturned:
        libros = Libros.objects.filter(slug=slug).order_by("-Autor").first()

    print libros
    mens = "Libros nuevos"
    template = "detalle_slug.html"
    contexto= {"mensaje":mens,
           "Libros": libros }
    return render(request, template, contexto)

def detalle_s(request, slug=None):
    #Logico de negocio alias hechizo
    try:
        libros = get_object_or_404(Producto, slug=slug)
    except Libros.MultipleObjectsReturned:
        libros = Libros.objects.filter(slug=slug).order_by("-Autor").first()
    mens = "Libros nuevos"
    template = "detalle_slug.html"
    contexto= {"mensaje":mens,
           "Libros": libros }
    return render(request, template, contexto)

def actualizar(request, object_id=None):
    #Logico de negocio alias hechizo
    libros = get_object_or_404(Libros, id=object_id)
    form = LibrosModelForm(request.POST or None, instance=libros)
    if form.is_valid():
        form.save()
        print "Actualizacion exitosa!"
    template = "actualizar.html"
    contexto= {
           "libros": Libros,
           "form":form,
           "titulo":"Actualizar Libro"
           }
    return render(request, template, contexto)

def detalle_libro(request, object_id=None):

    lib = get_object_or_404(Libros, id=object_id)
    mens = "Libros Registrados Actualmente"
    template = "detalle_libro.html"
    contexto= {"Mensaje":mens,
           "Libros": lib }
    return render(request, template, contexto)


def agregar_libro(request):
    form = LibroAddForm(request.POST or None)
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

    template = "agregar_libro.html"

    context = {
    "titulo":"Crear Producto",
    "form":form
    }

    return render(request, template, context)
