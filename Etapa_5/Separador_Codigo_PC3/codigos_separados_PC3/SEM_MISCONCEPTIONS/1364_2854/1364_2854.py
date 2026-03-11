from math import *
v0 = float(input("velocidade inicial: "))
d = float(input("distancia: "))
angulo = asin(d * (9.8/v0**2))*(90/pi)

print(round(angulo,2))