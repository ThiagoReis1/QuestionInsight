from math import *

ang = float(input("angulo: "))
dist = float(input("distancia: "))

g = 9.8

Vo = sqrt((dist * g) / sin (2 * radians(ang)))

print(round(Vo, 2))