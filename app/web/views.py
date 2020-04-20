from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import requests
from django.contrib.auth.decorators import login_required
from app.cliente.models import Cliente

def home(request):
    return render(request, 'index.html')


class Login(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required(login_url='/conta/login')
def Corretor(request):
    return render(request, 'index.html')

@login_required(login_url='/conta/login')
def DadosAPI(requests):
    url = 'https://gateway.gr1d.io/sandbox/dadoscadastrais/v1/consultas/v1/L0011/'
    cpf_cliente = Cliente.cpf
    headers = {
   'Content-Type': 'application/json',
   'Authorization': '19904100-ab50-4b0b-88aa-e23940426c31'
}
    response = requests.request("GET", url, headers=headers, data = cpf_cliente)
    if response.status_code == 200:
        return response.json()
    else:
        return redirect ('index.html')
