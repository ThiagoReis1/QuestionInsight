from math import *

#entradas
ang = radians(float(input("Angulo da flecha: ")))
v0 = float(input("Velocidade inicial da flecha (m/s): "))

#saidas
distancia = v0**2*sin(2*ang)/9.8
print(round(distancia, 2))