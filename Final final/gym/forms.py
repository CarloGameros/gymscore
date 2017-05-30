from django import forms
from .models import Usuario

META_CHOICES = (
    ('A', 'Aumentar',),
    ('B', 'Bajar',),
)

SEX_CHOICES = (
    ('H', 'Hombre',),
    ('M', 'Mujer',),
    ('I', 'Indistinto',),
    )

class UsuarioAdd(forms.Form):
    Nombres = forms.CharField(label="Cuales son sus nombres?",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Introduzca sus nombres'}))
    email = forms.CharField(label="Cual es su correo?",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Introduzca sus nombres'}))
    password = forms.CharField(label="Cuales son sus nombres?",
                         widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Introduzca sus nombres'}))
    password2 = forms.CharField(label="Cuales son sus nombres?",
                         widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Introduzca sus nombres'}))
    Apeidos = forms.CharField(label="Cuales son sus apeidos?",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Introduzca sus apeidos'}))
    Edad = forms.CharField(label="Que edad tiene?",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Introduzca su edad'}))
    Pesoi = forms.DecimalField(label="Cual es su peso?",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Introduzca su peso'}))
    avance = forms.DecimalField(label="Cual es su peso?",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Introduzca su peso'}))
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    meta = forms.ChoiceField(choices=SEX_CHOICES)

    def clean_peso(self):
        Pesoi=self.cleaned_data.get("precio")
        if Pesoi <=30.00:
            raise forms.ValidationError("El Peso debe ser mayor a la cantidad de 30")
        elif Pesoi >=300.00:
            raise forms.ValidationError("El Peso sobrepasa el rango de 300")
        else:
            return Pesoi
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


class UsuariosModelForm(forms.ModelForm):
    Sex = forms.ChoiceField(choices=SEX_CHOICES)
    Meta = forms.ChoiceField(choices=META_CHOICES)
    class Meta:
        model = Usuario
        fields =[
            "Nombres",
            "Apeidos",
            "Edad",
            "Pesoi",
            "email",
            "password",
            "password2",
            "meta",

                    ]
        labels = {
            "Nombres": "Nombres",
            "Apeidos":"Sus Apeidos",
            "Edad":"Edad",
            "Pesoi":"Peso inicial",
            "email":"Su correo electronico",
            "password":"Elija un password",
            "password2":"Confirme su password",
            "meta":"Dinos tu proposito",
            }
        widgets = {
            "Nombres": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Introduzca el nombre'}),
            "email": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Introduzca el nombre'}),
            "password": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Introduzca el nombre'}),
            "password2": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Introduzca el nombre'}),
            "Apeidos": forms.TextInput(attrs={'class': 'form-control'}),
            "Edad": forms.TextInput(attrs={'class': 'form-control'}),
            "Pesoi":forms.NumberInput(attrs={'class':'form-control'}),
            }

    def clean_peso(self):
         Pesoi=self.cleaned_data.get("Peso")
         if Pesoi <=30.00:
             raise forms.ValidationError("El Peso debe ser mayor a la cantidad de 200")
         elif Pesoi >=19999.99:
             raise forms.ValidationError("El Peso sobrepasa el rango de 19999.99")
         else:
             return Pesoi
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
        if Usuario.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("Esta cuenta ya esta registrada, seguro que no tienes una cuenta?")
        return email

class UsuariosActualizarModelForm(forms.ModelForm):
    Meta = forms.ChoiceField(choices=META_CHOICES)
    class Meta:
        model = Usuario
        fields =[
            "Nombres",
            "Apeidos",
            "Edad",
            "Pesoa",
            "meta",

                    ]
        labels = {
            "Nombres": "Nombres",
            "Apeidos":"Sus Apeidos",
            "Edad":"Edad",
            "Pesoa":"Peso actual",
            "meta":"Dinos tu proposito",
             }
        widgets = {
            "Nombres": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Introduzca el nombre'}),
            "email": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Introduzca el nombre'}),
            "Apeidos": forms.TextInput(attrs={'class': 'form-control'}),
            "Edad": forms.TextInput(attrs={'class': 'form-control'}),
            "Pesoa":forms.NumberInput(attrs={'class':'form-control'}),
            }

    def clean_peso(self):
         Pesoa=self.cleaned_data.get("Peso")
         if Pesoa <=30.00:
             raise forms.ValidationError("El Peso debe ser mayor a la cantidad de 200")
         elif Pesoa >=19999.99:
             raise forms.ValidationError("El Peso sobrepasa el rango de 19999.99")
         else:
             return Pesoa

    @property
    def avance(self):
        return self.Pesoi - self.Pesoa
