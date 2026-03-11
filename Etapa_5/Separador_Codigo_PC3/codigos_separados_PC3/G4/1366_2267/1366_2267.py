from math import *
A = radians(float(input("ângulo da flecha: ")))
V = float(input("velocidade inicial: "))
g = 9.8

E = sin(2*A)

d = V**2*E/g
print(round(d, 2))
