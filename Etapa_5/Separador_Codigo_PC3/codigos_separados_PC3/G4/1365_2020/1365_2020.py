from math import*

a = radians(float(input("angulo: ")))
d = float(input("distancia: "))

g = 9.8

vo = sqrt(d * (g / sin(2 * a)))

print(round(vo,2))