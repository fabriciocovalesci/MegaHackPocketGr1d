from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def login(request):
    pass