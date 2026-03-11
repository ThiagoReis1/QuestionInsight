from math import *
angulo = radians(float(input("angulo da flecha: ")))
v = float(input("velocidade inicial: "))
d = (v ** 2) * sin(2 * angulo) / 9.8
print(round(d, 2))