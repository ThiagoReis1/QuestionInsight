from math import *

g = 9.8
a = radians(float(input("Valor de a:")))
vo = float(input("Velocidade inicial:"))

d = ((vo ** 2) * sin(2 * a))/g

print(round(d, 2))
