#Angulo da flecha

from math import *

velocidade_inicial = float(input("Digite a velocidade inicial: "))

distancia = float(input("Digite a distancia: "))
g = 9.8

angulo = asin(distancia * g/(velocidade_inicial**2)) * 90/pi
									
print(round(angulo,2))