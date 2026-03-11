from math import *

a = radians(float(input("Angulo da flecha: ")))
v = float(input("velocidade inicial: "))

d = (v**2)*sin(2*a)*(1/9.8)

print(round(d,2))