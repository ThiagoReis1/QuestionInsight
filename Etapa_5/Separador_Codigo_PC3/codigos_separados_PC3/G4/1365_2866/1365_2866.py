from math import *

ang = float(input("qual o angulo: "))
dist = float(input("qual a distancia: "))

d = dist
alpha = radians(ang)
g = 9.8

x = (d * g / sin(2 * alpha))
vo = sqrt(x)

print(round(vo, 2))
