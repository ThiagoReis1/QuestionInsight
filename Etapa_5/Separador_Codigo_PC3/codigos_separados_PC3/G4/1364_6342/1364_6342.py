from math import *
v0 = float(input("Escreva a velocidade inicial da flecha: "))
d = float(input("A distancia: "))
g = 9.8
a = asin(d * g/v0**2) * 90/pi
print(round(a, 2))