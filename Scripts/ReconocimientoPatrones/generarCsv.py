import random
import csv

nregistros=int(input("Ingreso el numero de registros a generar: "))
valmax=int(input("valor numerico maximo a generar en las columnas: "))

with open('bdmatutino.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(0,nregistros):
        texto= [random.randint(0, valmax), random.randint(0, valmax), random.randint(0, valmax)]
        writer.writerow(texto)