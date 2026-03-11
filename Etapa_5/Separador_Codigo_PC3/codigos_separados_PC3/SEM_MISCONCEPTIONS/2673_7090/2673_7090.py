from math import *

raio = float(input("Valor do raio: "))
nlados = int(input("Numero de lados do poligono: "))

lado = 2 * raio * sin(pi / nlados)
print(round(lado,2))