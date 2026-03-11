from math import *
var1=radians(float(input("angulo da fecha: ")))
var2=float(input("velocidade inicial: "))

#distancia
g=9.8
d= var2 ** 2 * (sin( 2 * var1) / g)

print(round(d, 2))