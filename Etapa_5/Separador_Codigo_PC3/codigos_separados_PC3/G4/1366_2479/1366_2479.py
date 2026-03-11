from math import *

alpha = radians(float(input("Ângulo: ")))
v = float(input("Velocidade inicial: "))


g = 9.8
d = ((v**2)*sin(2*alpha))/g

print(round(d, 2))