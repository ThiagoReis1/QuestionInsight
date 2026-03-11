from math import *

raio = float(input("Raio: "))
numero_lados = int(input("Numeros de lados: "))
area = 1/2 * ((raio * cos(pi/numero_lados)) ** 2 * tan(pi/numero_lados))

print(round(area, 2))