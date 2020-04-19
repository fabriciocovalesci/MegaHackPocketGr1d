
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.Registrar.as_view(), name='register'),
] 