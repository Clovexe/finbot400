from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_list_or_404
from users.models import Costumer
from .forms import CostumerForms,UpdateForms, PasswordForms
from django.forms import ModelForm
import requests
import json
from django import template
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

registered = template.Library()

@registered.filter
def index(indexable, i):
    return indexable[i]

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello</h1>")
    username = "Hello"
    stat = "Hey"
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        obj = Costumer.objects.get(email=email)
        stat = obj.check_password(password)
        if stat:
            return redirect('finchat', username=obj.username)
    context = {
        "name": username,
        "stat": stat,
    }
    return render(request, "home.html", context)

def register_form(request):
    
    # if request.method == "POST":
    form = CostumerForms(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        form = CostumerForms()
        return  redirect('messenger', username=user)
    context={
        "form": form,
    }
    return render(request, "register.html", context)

def contact_view(request, username):
    obj = Costumer.objects.get(username = username)
    context ={
        "obj": obj
    }
    return render(request, "product/detail.html", context)

status = ["not registered", "conservative", "aggressive"]

def dashboard_view(request, username):
    obj = ""    
    if Costumer.objects.filter(username=username).exists():
        obj = Costumer.objects.get(username=username)
    else: return HttpResponse("<h1 style=\"font-family: Consolas;\">Error username not found </h1>")
    form = UpdateForms(initial={
        "firstname":obj.firstname,
        "lastname": obj.lastname,
        "contact": obj.contact,
        "about": obj.about
        })
    context = {
        "form":form,
        "obj" : obj,
        "username" : username,
        "status": status[obj.investing_style],
    }
    return render(request, "dashboard.html", context)


def test_view(request, username):
    response = requests.get("http://phisix-api4.appspot.com/stocks.json")
    context = {
        "response": response.json()["stock"],
    }
    return render(request, "test.html", context)


def update_view(request, username):
    obj = 0    
    if Costumer.objects.filter(username=username).exists():
        obj = Costumer.objects.get(username=username)
    else: return HttpResponse("<h1 style=\"font-family: Consolas;\">Error username not found </h1>")
    form = UpdateForms(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        print(username+"superman")
        return HttpResponseRedirect("/dashboard/"+username)
    context = {
        "form":form,
        "obj" : obj,
        "username" : username,
        "status": status[obj.investing_style],
    }
    return render(request, "update.html", context)


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')



def security_view(request, username):
    obj = 0    
    if Costumer.objects.filter(username=username).exists():
        obj = Costumer.objects.get(username=username)
    else: return HttpResponse("<h1 style=\"font-family: Consolas;\">Error username not found </h1>")
    form = PasswordForms(request.POST or None)
    if request.method == "POST":
        print(request.get("password"))
    context = {
        "form":form,
        "obj" : obj,
        "username" : username,
    }
    return render(request, "credentials.html", context)


