from django import forms
from .models import Libros

OPCIONES_TIPO = (
    ('editorial solar', "Editorial Solar"),
    ('editorial portavoz', "Editorial Portavoz"),
    ('editorial rino', "Editorial Rino"),
)

class LibroAddForm(forms.Form):
    Nombre=forms.CharField(label="Cual es nombre del libro",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Introduzca el nombre del libro'}))

    Autor=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    Editorial=forms.ChoiceField(choices=OPCIONES_TIPO)
    ISBN=forms.CharField()
    Precio=forms.DecimalField()

    def clean_precio(self):
        precio=self.cleaned_data.get("precio")
        if precio <=200.00:
            raise forms.ValidationError("El precio debe ser mayor a la cantidad de 200")
        elif precio >=19999.99:
            raise forms.ValidationError("El precio sobrepasa el rango de 19999.99")
        else:
            return precio



class LibrosModelForm(forms.ModelForm):
    Editorial = forms.ChoiceField(choices=OPCIONES_TIPO)
    class Meta:
        model = Libros
        fields =[
            "Nombre",
            "Autor",
            "Editorial",
            "ISBN",
            "Precio",
        ]
        labels = {
            "Nombre": "Cual es nombre del libro",
            "Autor":"Quien es el autor del libro",
            "Editorial":"Cual es la editorial del libro",
            "ISBN":"Cual es el isbn del libro",
            "Precio":"Cual es el precio del libro",
        }
        widgets = {
            "Nombre": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Introduzca el nombre'}),
            "Autor": forms.Textarea(attrs={'class': 'form-control'}),
            "Editorial": forms.TextInput(attrs={'class': 'form-control'}),
            "ISBN":forms.TextInput(attrs={'class':'form-control'}),
            "Precio":forms.NumberInput(attrs={'class':'form-control'}),
        }

    def clean_precio(self):
         precio=self.cleaned_data.get("precio")
         if precio <=200.00:
             raise forms.ValidationError("El precio debe ser mayor a la cantidad de 200")
         elif precio >=19999.99:
             raise forms.ValidationError("El precio sobrepasa el rango de 19999.99")
         else:
             return precio
