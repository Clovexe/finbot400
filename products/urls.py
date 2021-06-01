from django.contrib import admin
from django.urls import path
from products.views import product_detail_view, product_create_view, delete_product, list_product, buy_product


app_name = "products"

urlpatterns = [
    path('detail/<int:id>/', product_detail_view, name="product-detail"),
    path('<str:username>/buy/<str:id>', buy_product, name="product-buy"),
    path('create/', product_create_view, name="product-create"), 
    path('delete/<int:id>/', delete_product, name="product-delete"),
    path('<str:username>/', list_product, name="product-list"),
]