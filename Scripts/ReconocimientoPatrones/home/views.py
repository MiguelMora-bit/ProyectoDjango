from django.shortcuts import render
from django.http import HttpResponse
from .models import Tejido

# Create your views here.
def home(request):
    tejidos = Tejido.objects.get_queryset()
    return render(request, "home.html", {"lista": tejidos})