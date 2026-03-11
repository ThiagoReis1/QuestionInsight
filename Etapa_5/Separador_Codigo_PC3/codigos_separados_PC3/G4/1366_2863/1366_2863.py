from math import *

a = radians(float(input("Angulo: ")))
v = float(input("Velocidade inicial: "))
g = 9.8


d = v**2*sin(2*a)/g

print(round(d,2))