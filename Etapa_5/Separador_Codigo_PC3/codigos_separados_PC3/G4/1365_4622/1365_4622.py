from math import*
a = float(input("angulo: "))
d = float(input("distancia: "))
g = 9.8
v = (d*(g/sin(radians(2*a))))**0.5
print(round(v,2))