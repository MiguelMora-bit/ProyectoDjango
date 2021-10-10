from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return render(request, "home.html")

def despedida(request):
    return render(request, "adios.html")

def contacto(request):
    return HttpResponse("mi numero de contacto")