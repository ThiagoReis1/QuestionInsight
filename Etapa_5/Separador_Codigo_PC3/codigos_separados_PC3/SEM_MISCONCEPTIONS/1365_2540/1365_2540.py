angulo = float(input("angulo da flecha:"))
distancia = float(input("distancia:"))

g = 9.8
from math import*
a = radians(angulo)

vo = sqrt(distancia*g/sin(2*a))




print(round(vo,2))