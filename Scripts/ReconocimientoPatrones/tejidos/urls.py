from django.contrib import admin
from django.urls import path
from .views import tejidos

app_name = "tejidos"

urlpatterns = [
    path('tejidos/', tejidos, name= "tejidos")
]