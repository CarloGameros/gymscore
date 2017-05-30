from django.contrib import admin
from gym.models import Usuario
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("email","password","password2","id", "Nombres", "Apeidos", "Edad", "Pesoi", "sex", "Pesoa","avance","meta","fecha")
    search_fields = ["Pesoi"]
    list_editable = ["Pesoi"]
    list_filter = ["Nombres"]
    class meta:
        model = Usuario

admin.site.register(Usuario,UsuarioAdmin)
