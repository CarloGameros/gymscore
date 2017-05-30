from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistroForm(forms.Form):
    usuario = forms.CharField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-password form-control',
                                                            'placeholder': 'Nombres'}))
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-password form-control',
                                                            'placeholder': 'Correo electronico'}))
    password = forms.CharField(label="",
                             widget=forms.PasswordInput(attrs={'class': 'form-password form-control',
                                                            'placeholder': 'Password'}))
    password2 = forms.CharField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-password form-control',
                                                            'placeholder': 'Confirme'}))

    def clean_password2(self):
        print "Entro"
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            print "Error"
            raise forms.ValidationError("Password debe coincidir! ")
        return password

    def clean_username(self):
        usuario = self.cleaned_data.get('username')
        if User.objects.filter(usuario__icontains=usuario).exists():
            raise forms.ValidationError("Lo sentimos, este usuario ya existe.")
        return usuario

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("Esta cuenta ya esta registrada, seguro que no tienes una cuenta?")
        return email

class InicioForm(forms.Form):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-password form-control',
                                                            'placeholder': 'Correo electronico'}))
    password = forms.CharField(label="",
                             widget=forms.PasswordInput(attrs={'class': 'form-password form-control',
                                                            'placeholder': 'Password'}))
