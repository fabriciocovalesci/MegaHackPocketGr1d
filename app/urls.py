"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
import app.web.views

from app.web.views import ( home)

urlpatterns = [
    path('', app.web.views.home),
    path('admin/', admin.site.urls),
    path('conta/', include('app.web.urls')),
    path('conta/', include('django.contrib.auth.urls')),
  
] 


# chave api d453aa14-2997-40c6-94f8-4fd73ea37e3e

