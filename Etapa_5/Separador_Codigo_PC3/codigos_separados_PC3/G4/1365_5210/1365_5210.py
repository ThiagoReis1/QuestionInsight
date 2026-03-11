from math import*
ang = radians(float(input("angulo: ")))
d = float(input("distancia: "))

from math import*
v = sqrt( d * (9.8 / sin(2 * ang)))
print (round(v, 2))
