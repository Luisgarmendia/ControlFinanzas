"""ControlFinanzas URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app_login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Clientes/',include('Clientes.urls')),# URL CLIENTES
    path('',views.index),
    path('registro/',views.registro_cliente,name="registro_cliente"),#URL DE REGISTRO DE USUARIOS DE LA APLICACION LOGIN
    path('login/',views.log_in,name='login_view'),#URL LOGIN
    path('logout/',views.log_out,name='logout_view'),#URL LOGOUT
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)