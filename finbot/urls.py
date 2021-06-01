"""finbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from dashboard.views import messenger_view, risktest_view


urlpatterns = [
    path('products/', include('products.urls')),
    path('', include('pages.urls')),
    path('finchat/<str:username>',messenger_view, name="finchat"),
    path('risktest/', risktest_view, name="risktest"),
    path('risktest/<str:username>', risktest_view, name="risktest-account"),
    path('admin/', admin.site.urls),
]
