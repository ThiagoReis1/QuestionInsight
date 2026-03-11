from math import *
a = radians(float(input()))
d = float(input())

g = 9.8 
velocidade_inicial = sqrt((d * 9.8)/sin(2 * a))

print(round(velocidade_inicial, 2))