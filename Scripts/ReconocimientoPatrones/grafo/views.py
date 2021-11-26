from django.shortcuts import redirect, render
from home.models import Tejido
import math
import numpy as np


distancias = []

def grafo(request):
    global distancias
    tejidos = Tejido.objects.get_queryset()
    matrizPropiedades = []
    for tejido in tejidos:
        tejido = vars(tejido)
        keys = [key for key in tejido if not key.startswith('_') and not key.startswith('id') and not key.endswith('id')]
        tejidoPropiedades = []
        for k in keys:
            tejidoPropiedades.append(tejido[k]);
        matrizPropiedades.append(tejidoPropiedades)
    
    dimension = len(matrizPropiedades)
   
    distancias = np.zeros((dimension,dimension))

    for i in range(dimension):
        for j in range(i,dimension):
            if i != j:
                distancia = distanciaEuclideana(matrizPropiedades[i], matrizPropiedades[j])
                distancias[i][j] = distancia
                distancias[j][i] = distancia

    diccionario = {"distancias": distancias}
    return render(request, "grafo.html", diccionario)

    
def distanciaEuclideana(p,q):
	distancia = math.dist(p,q)
	return distancia


def procesaGrafo(request):
    umbrales = []
    umbral = request.GET["umbral"]
    tamañoDistancias = len(distancias)

    if not(umbral):
        umbral = 0
    else:
        umbral = float(umbral)

    for i in range(tamañoDistancias):
        for j in range(i, tamañoDistancias):
            dist = float(distancias[i,j])
            if i == j:
                umbrales.append([i,j,dist, "Sí" ])
            elif (dist > umbral):
                umbrales.append([i,j,dist, "Sí" ])
            else:
                umbrales.append([i,j,dist, "No" ])
    
    diccionario = {"umbrales": umbrales}
    return render(request, 'umbral.html', diccionario)