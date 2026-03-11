from math import *

ang = radians(float(input('angulo: ')))
V = float(input("velocidade: "))


d = (V ** 2) * sin((2 * ang)) / 9.8

print(round(d,2))