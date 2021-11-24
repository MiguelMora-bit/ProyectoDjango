from django.contrib import admin
from django.urls import path
from .views import grafo

app_name = "grafo"

urlpatterns = [
    path('grafo/', grafo, name= "grafo")
]