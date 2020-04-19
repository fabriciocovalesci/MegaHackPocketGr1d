from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.Login.as_view(), name='register'),
]