from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home_view, contact_view, register_form, update_view, test_view,dashboard_view, PasswordsChangeView, security_view

app_name = "pages"

urlpatterns = [
    path('',home_view, name="home"),
    path('sign-up/',register_form, name="sign-up"),
    path('dashboard/<str:username>', dashboard_view, name="profile"),
    path('dashboard/update/<str:username>', update_view, name="update"),
    # path('dashboard/security/<str:username>', auth_views.PasswordChangeView.as_view(template_name="credentials.html"), name="security"),
    # path('dashboard/security/<str:username>', PasswordsChangeView.as_view(template_name="credentials.html"), name="security"),
    path('dashboard/security/<str:username>',security_view , name="security"),
    path('test/<str:username>', test_view, name="test"),
    path('test/', test_view, name="test"),
    path('contact/<str:username>',contact_view, name="contact"),
]