# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import get_user_model
from .forms import RegistroForm, InicioForm

# Create your views here.

User = get_user_model()

class RegistroView(FormView):
    template_name = 'accounts/singin.html'
    form_class = RegistroForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)

class InicioView(FormView):
    template_name = 'accounts/singin1.html'
    form_class = InicioForm
    success_url = '/inicio'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)
