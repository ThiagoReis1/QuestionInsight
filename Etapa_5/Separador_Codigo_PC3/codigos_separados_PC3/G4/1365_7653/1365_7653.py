from math import*
d = float(input("distancia:"))
s = float(input("angulo:"))
v = sqrt(d*9.8/sin(2*radians(s)))
print(round(v,2))