from math import *
velocidade_inicial = float(input("qual a velocidade inicial: "))
distancia = float(input("qual a distancia: "))
g = 9.8
a = asin(distancia * g/velocidade_inicial**2) * 90/pi
print(round(a,2))