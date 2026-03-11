from math import *

angulo=float(input())
velocidade=float(input())

g=9.8
d=(velocidade**2)*(sin(radians(2*angulo)))/g

print(round(d,2))