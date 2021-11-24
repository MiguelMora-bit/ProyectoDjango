from django.shortcuts import render
from home.models import Tejido

# Create your views here.
def tejidos(request):
    tejidos = Tejido.objects.get_queryset()

    diccionario = {"lista": tejidos}

    return render(request, "tejidos.html", diccionario)