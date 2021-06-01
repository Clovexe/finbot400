from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect
from .models import product
# Create your views here.
from .forms import product_form, raw_product_form 
import json
import requests

def render_initial_data(request):
    initial_data={
        'title': "This is a product title"
    }
    form = raw_product_form(request.POST or None, initial=initial_data)
    context = {
        'form': form
    }
    return render(request,"product/create.html", context)


def product_detail_view(request, id, username):
   # obj = product.objects.get(id=id)  
    obj = get_object_or_404(product, id=id)

   # context ={
   #     "title":obj.title,
   #     "description": obj.description,
   #     "price": obj.price,
   # }
    context = {
       "obj": obj,
       "username": username
    }
    return render(request, "product/detail.html", context)

def product_create_view(request):
    initial_data={
        'title': "This is a product title"
    }
    obj = product.objects.get(id=1)
    form = product_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = product_form()
    context = {
       "form": form,
   }
    return render(request, "product/create.html", context)


def delete_product(request, id, username):
    obj = get_object_or_404(product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context={
        "obj": obj
    }
    return render(request, "products/delete.html", context)

def list_product(request, username):
    response = requests.get("http://phisix-api4.appspot.com/stocks.json")
    context = {
        "objects":response.json()["stock"],
        "username" : username,
    }
    return render(request, "products/products.html", context)

def buy_product(request, id, username):
    response = requests.get("http://phisix-api4.appspot.com/stocks/"+id+".json")
    context = {
        "object": response.json()["stock"][0],
        "username" : username,
    }
    return render(request, "products/product_buy.html", context)
# def product_create_view(request):
#    if request.method == "POST":
#        title = request.POST.get("title")
#        print(title)
#    context = {}
#    return render(request, "product/create.html", context)

#def product_create_view(request):
#    form = raw_product_form()
#    if request.method == "POST":
#        form = raw_product_form(request.POST)
#        if form.is_valid():
#            print(form.cleaned_data)
#            product.objects.create(**form.cleaned_data)
#        else: print(form.errors)
#    context = {
#        "form": form
#    }
#    return render(request, "product/create.html", context)