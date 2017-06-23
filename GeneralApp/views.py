# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm, UserForm
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from ProfileApp.models import Profile


# Create your views here.

class LoginFormView(View):
    form_class = LoginForm
    context = ""

    def get(self, request):
        form = self.form_class(None)
        context = ""
        return render(request, 'GeneralApp/login.html', {'form': form, 'context': context})

    def post(self, request):
        form = self.form_class(None)
        # cleaned (normalized) data

        context = ""
        username = request.POST['username']
        password = request.POST['password']

        # returns User objects if credentials are correct
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            else:
                context = "User is banned"
        else:
            context = "Incorrect username or password"

        return render(request, 'GeneralApp/login.html', {'form': form, 'context': context})


class UserFormView(View):
    form_class = UserForm
    context = ""

    def get(self, request):
        form = self.form_class(None)
        context = ""
        return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})

    def post(self, request):
        form = self.form_class(request.POST)
        context = ""

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username1 = form.cleaned_data['username1']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                context = "Passwords do not match."
                return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})
            user.set_password(password1)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username1, password=password1)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard')
                else:
                    context = "Existing user is banned."

        else:
            context = "Please select a unique username."

        return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})


def redirect_to_dashboard(request):
    return HttpResponseRedirect('/dashboard/')


class Tnc(generic.TemplateView):
    template_name = 'GeneralApp/tnc.html'


class AboutUs(generic.TemplateView):
    template_name = 'GeneralApp/about.html'
    

def SymptomHead(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='head')
        return  render(request,'GeneralApp/symptomhead.html',{'x': a})

def SymptomAbdomen(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='abdomen')
        return  render(request,'GeneralApp/symptomabdomen.html',{'x': a})

def SymptomArms(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='arms')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})


def SymptomChest(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='chest')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

def SymptomFeet(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='feet')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})


def SymptomHands(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='hands')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

def SymptomHips(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='hips')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

def SymptomLegs(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='legs')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

def SymptomNeck(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='neck')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

def SymptomPelvis(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='pelvis')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})



def SymptomShoulder(request):
    if request.method == 'GET':
        a = Symptom.objects.filter(bodypart__bodypart='shoulder')
        return  render(request,'GeneralApp/symptomlist.html',{'x': a})

