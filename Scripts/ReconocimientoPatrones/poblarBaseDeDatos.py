import csv
from home.models import Tejido

fields = ["temperatura", "color", "inflammation"]

for row in csv.reader(open('bdmatutino.csv')):
    Tejido.objects.create(**dict(zip(fields, row)))