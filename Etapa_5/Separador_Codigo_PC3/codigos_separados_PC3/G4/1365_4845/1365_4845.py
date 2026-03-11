from math import *
an = float(input("angulo: "))
d = float(input("distancia da saida da flecha: "))
ad = radians(an)
g = float(9.8)
v = float(sqrt(d*g/sin(2*ad)))
print(round(v,2))