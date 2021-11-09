from django.contrib import admin
from django.urls import path
from .views import about

app_name = "about"

urlpatterns = [
    path('about/', about, name= "about")
]