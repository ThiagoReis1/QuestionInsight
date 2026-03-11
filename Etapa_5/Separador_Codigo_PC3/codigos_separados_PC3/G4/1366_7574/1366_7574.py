from math import*

a=float(input("angulo: "))
v=float(input("velocidade incial: "))

d= (v **2) * (sin(2 *(radians(a)))/9.8)

print(round(d,2))