from django.shortcuts import render
from home.models import Tejido
import math
import numpy as np

def grafo(request):

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