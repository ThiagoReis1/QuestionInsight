from math import *

angulo = radians(float(input("Informe o angulo: ")))
velocidade_inicial = float(input("Informe a velocidade inicial da flecha: "))

distancia = (velocidade_inicial**2)*sin(2*angulo)/9.8

print(round(distancia,2))