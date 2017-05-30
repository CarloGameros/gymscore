from django.contrib import admin
from libros.models import Libros
# Register your models here.

class LibrosAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Autor", "Editorial", "ISBN", "Precio")
    search_fields = ["Precio"]
    list_editable = ["Precio"]
    list_filter = ["Autor"]
    class meta:
        model = Libros

admin.site.register(Libros,LibrosAdmin)
